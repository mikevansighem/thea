import arrow


def time_to_seconds(time) -> float:

    return (time.hour * 60 + time.minute) * 60 + time.second


class StackedLinearModel:
    def __init__(self, time_basis) -> None:

        self.data_points = []
        self.time_basis = time_basis

    def __repr__(self) -> str:

        return "An instance of {} with {} datapoints".format(
            self.__class__.__name__, len(self.data_points)
        )

    def __str__(self) -> str:

        return "{} with {} datapoints".format(
            self.__class__.__name__, len(self.data_points)
        )

    def add_point(self, date_time, value) -> None:

        if self.time_basis == "day":
            self.data_points.append((time_to_seconds(date_time.time()), value))

        elif self.time_basis == "year":
            self.data_points.append((date_time.day_of_year(), value))

        else:
            raise NotImplementedError(
                'Time basis "{}" is not implemented.'.format(self.time_basis)
            )

        # Sort the list based on time
        self.data_points = sorted(self.data_points)

    def get_value(self, date_time) -> float:

        # Normalize time
        if isinstance(date_time, int):
            # Normalization is not required
            pass

        elif self.time_basis == "day":
            date_time = time_to_seconds(date_time.time())

        else:
            raise NotImplementedError(
                'Time basis "{}" is not implemented.'.format(self.time_basis)
            )

        # Find ranges
        for i, data_point in enumerate(self.data_points):

            if (
                date_time > self.data_points[-1][0]
                or date_time < self.data_points[0][0]
            ):

                start_time = self.data_points[-1][0]
                end_time = self.data_points[0][0]
                start_value = self.data_points[-1][1]
                end_value = self.data_points[0][1]

                if self.time_basis == "day":
                    end_of_basis = 60 * 60 * 24

                else:
                    raise NotImplementedError(
                        'Time basis "{}" is not implemented.'.format(self.time_basis)
                    )

                time_delta = end_of_basis - start_time + end_time
                value_delta = end_value - start_value

                if date_time <= end_time:
                    return end_value - (value_delta / time_delta) * (
                        end_time - date_time
                    )
                else:
                    return (value_delta / time_delta) * (
                        date_time - start_time
                    ) + start_value

            elif date_time <= data_point[0]:

                start_time = self.data_points[i - 1][0]
                end_time = data_point[0]
                start_value = self.data_points[i - 1][1]
                end_value = data_point[1]

                value_delta = end_value - start_value
                time_delta = end_time - start_time

                return (value_delta / time_delta) * (
                    date_time - start_time
                ) + start_value

    def plot(self) -> None:

        import matplotlib.pyplot as plt

        if self.time_basis == "day":
            time_range = range(0, 60 * 60 * 24, 60)

        else:
            raise NotImplementedError(
                'Time basis "{}" is not implemented.'.format(self.time_basis)
            )

        value_range = []
        for time_int in time_range:
            value_range.append(self.get_value(time_int))

        plt.plot(time_range, value_range)

        time_points = [p[0] for p in self.data_points]
        value_points = [p[1] for p in self.data_points]

        plt.scatter(time_points, value_points)

        plt.xlabel("time")
        plt.ylabel("value")

        plt.title("Stacked Linear Model")

        plt.show()


if __name__ == "__main__":

    model = StackedLinearModel("day")
    model.add_point(arrow.get("07:00", "HH:mm"), 0)
    model.add_point(arrow.get("10:00", "HH:mm"), 0.9)
    model.add_point(arrow.get("17:00", "HH:mm"), 0.9)
    model.add_point(arrow.get("22:00", "HH:mm"), 0)

    model.plot()
