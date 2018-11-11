# Notepad

## Quick todo
-   Environment factory with location presets.
-   Lunar: face https://pylunar.readthedocs.io/en/latest/usage.html
-   Handle warnings in logging
-   Main calls CLI, CLI maps directly to calls to Thea world and its stores

## Notes
-   timezone according to IANA timezone
-   https://pypi.org/project/pycountry/ for country handling

## Snippets
### Location preset
location = Location(latitude=52.370216, longitude=4.895168, tz='Europe/Amsterdam', altitude=-2, name='Amsterdam')
location.country = 'The Netherlands'

## Longterm todo
-   Lunar: GHI, DNI, DHI
-   List of environment settings and variables including units and allowed ranges.
-   Markdown linter in precommit
-   add https://github.com/PyCQA/bandit
-   Toga or qt gui
-   https://www.researchgate.net/post/Please_i_would_like_to_knwo_how_to_convert_lux_to_W_m2
