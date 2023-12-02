from dataclasses import dataclass
import httpx


@dataclass
class APIWeatherStatistics:
    api_key: str

    def get_interval(self, days: int) -> list:
        response = httpx.get(
            "https://api.openweathermap.org/data/2.5/forecast/daily",
            params={
                "lat": "41.6938",
                "lon": "44.6833",
                "cnt": days,
                "appid": self.api_key,
            },
        )

        return response.json()["cod"]
