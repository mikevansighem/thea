"""Sky colour functions retrived from: https://repository.tudelft.nl/
islandora/object/uuid:4789c552-5dad-4d91-8aad-d47608097947/datastream/
OBJ/download"""

import warnings
import numpy as np
from colormath.color_conversions import convert_color
from colormath.color_objects import XYZColor, sRGBColor, xyYColor
from ..defenitions import env_updater
from collections import namedtuple


@env_updater
def irradiance_to_lux(clear_sky_global_horizontal_irradiance, **unused):
    # Based on: https://www.researchgate.net/post/
    # Please_i_would_like_to_knwo_how_to_convert_lux_to_W_m2

    warnings.warn("Irradinace to lux function needs better citing.")

    lux = clear_sky_global_horizontal_irradiance / 0.0079

    return {"lux": lux}


RGBColour = namedtuple("RGBColour", ["red", "green", "blue"])


class SkyMap:
    def __init__(self, compression_factor, colour_updater):

        self.compression_factor = compression_factor
        self.colour_updater = colour_updater
        self.skymap_coloured = np.zeros(
            (int(90 / compression_factor), int(360 / compression_factor), 3), np.uint8
        )

    def populate(self, solar_azimuth, solar_zenith):

        for sky_element_zenith in range(0, 90, self.compression_factor):
            for sky_element_azimuth in range(0, 360, self.compression_factor):

                r, g, b = self.colour_updater(
                    solar_zenith,
                    solar_azimuth,
                    sky_element_zenith,
                    sky_element_azimuth,
                    output_format="RGB",
                )

                self.skymap_coloured[
                    int(sky_element_zenith / self.compression_factor),
                    int(sky_element_azimuth / self.compression_factor),
                ] = (b, g, r)


def haversine(azi1, alt1, azi2, alt2):
    """ Calculate the great circle distance between two points """

    # Check if the input is between 0 and 360
    if not 0 <= azi1 <= 360:
        raise ValueError("Input angle needs to be between 0 and 360 degrees")
    if not 0 <= alt1 <= 360:
        raise ValueError("Input angle needs to be between 0 and 360 degrees")
    if not 0 <= azi2 <= 360:
        raise ValueError("Input angle needs to be between 0 and 360 degrees")
    if not 0 <= alt2 <= 360:
        raise ValueError("Input angle needs to be between 0 and 360 degrees")

    # convert decimal degrees to radians
    azi1, alt1, azi2, alt2 = map(np.deg2rad, [azi1, alt1, azi2, alt2])

    # haver-sine formula
    dlon = azi2 - azi1
    dlat = alt2 - alt1
    a = np.sin(dlat / 2) ** 2 + np.cos(alt1) * np.cos(alt2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    angular_diffrence = np.rad2deg(c)

    return angular_diffrence


def xyY_to_XYZ(x, y, Y):
    """ Convert xyY to XYZ """

    xyY_color = xyYColor(x, y, Y)
    XYZ_color = convert_color(xyY_color, XYZColor)

    return XYZ_color.xyz_x, XYZ_color.xyz_y, XYZ_color.xyz_z


def uniform(solar_zenith, output_format="xyY"):
    """"The uniform sky model has the same luminance and chromaticity
        values for all sky elements corresponding to a given sun angle.
        The exact values are based on a linear least square error fit
        to the existing models. """

    # Get xyY values
    x = .00048616 * solar_zenith + 0.2441
    y = .00059239 * solar_zenith + 0.2505
    Y = -100.6861 * solar_zenith + 13194

    if output_format is "xyY":
        return x, y, Y

    # Get XYZ values
    X, Y, Z = xyY_to_XYZ(x, y, Y)

    if output_format is "XYZ":
        return X, Y, Z

    # Convert to RGB
    XYZ_color = XYZColor(X, Y, Z)
    RGB_color = convert_color(XYZ_color, sRGBColor)

    if output_format is "RGB":
        return RGB_color.rgb_r, RGB_color.rgb_g, RGB_color.rgb_b

    # Catch wrong input
    raise ValueError("Unsupported output_format entered")


def linear(
    solar_zenith,
    solar_azimuth,
    sky_element_zenith,
    sky_element_azimuth,
    output_format="RGB",
):
    """The linear sky model has its highest luminance value close to
    the sun and its lowest at the angle farthest away from the sun.
    The values of the sky elements between those angles are linearly
    interpolated. The chromaticity values are uniform for a given sun
    angle, as in the uniform sky model. """

    # Get raw output
    Ymin = -66.4924 * solar_zenith + 80293
    Ymax = 38.7158 * solar_zenith + 25648
    x = 0.00048616 * solar_zenith + 0.2441
    y = 0.00059239 * solar_zenith + 0.2505

    # Get difference between element and sun
    angular_diffrence = haversine(
        solar_azimuth, solar_zenith, sky_element_azimuth, sky_element_zenith
    )
    # at difference 0 color is max
    # at difference 180 color is min

    adjusted_diffrence = angular_diffrence - 180

    if adjusted_diffrence < 0:
        adjusted_diffrence = 360 + adjusted_diffrence

    Y = ((Ymax - Ymin) / 180) * adjusted_diffrence + Ymin

    if output_format is "xyY":
        return x, y, Y

    # Get XYZ values
    X, Y, Z = xyY_to_XYZ(x, y, Y)

    if output_format is "XYZ":
        return X, Y, Z

    # Convert to RGB
    XYZ_color = XYZColor(X, Y, Z)
    RGB_color = convert_color(XYZ_color, sRGBColor, target_illuminant="e")

    if output_format is "RGB":
        return RGB_color.rgb_r, RGB_color.rgb_g, RGB_color.rgb_b

    # Catch unsupported input
    raise ValueError("Unsupported output_format entered")


@env_updater
def uniform_sky_colour(solar_zenith, **unused):

    r, g, b = uniform(solar_zenith, output_format="RGB")
    uniform_sky_colour_rgb = RGBColour(red=r, green=g, blue=b)

    return {"uniform_sky_colour": uniform_sky_colour_rgb}


@env_updater
def linear_sky_colour(solar_zenith, solar_azimuth, **unused):

    linear_sky_colour_map = SkyMap(1, linear).populate(solar_azimuth, solar_zenith)

    print(linear_sky_colour_map)

    return {"linear_sky_colour_map": linear_sky_colour_map}
