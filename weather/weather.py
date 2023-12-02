from dataclasses import dataclass
from typing import Protocol


class WeatherStatistics(Protocol):
    def get_interval(self, days: int) -> list:
        pass


@dataclass
class FakeWeatherStatistics:
    stats: list

    def get_interval(self, days: int) -> list:
        return self.stats[:days]


@dataclass
class Weather:
    stats: WeatherStatistics

    def get_average(self, days: int) -> int:
        return sum(self.stats.get_interval(days)) // days
