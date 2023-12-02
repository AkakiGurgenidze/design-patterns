import os

import pytest

from weather.weather_api import APIWeatherStatistics


@pytest.mark.vcr
def test_api_average() -> None:
    stats = APIWeatherStatistics(os.environ["API_KEY"])

    assert stats.get_interval(0) == 401
