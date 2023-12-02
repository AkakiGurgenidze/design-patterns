from weather.weather import FakeWeatherStatistics, Weather


def test_average_weekly() -> None:
    statistics = FakeWeatherStatistics([18, 18, 18, 18, 18, 18, 18])

    average = Weather(statistics).get_average(days=7)

    assert average == 18


def test_average_by_days() -> None:
    statistics = FakeWeatherStatistics([19, 19, 19, 20, 20, 20])

    average = Weather(statistics).get_average(days=3)

    assert average == 19
