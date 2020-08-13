import datetime as dt
from datetime import datetime
from typing import List, Tuple

import httpx
import pytz
from pydantic import BaseModel, Extra


class Coords(BaseModel):
    lat: float
    lng: float


class Temp(BaseModel):
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float


class FeelsLike(BaseModel):
    day: float
    night: float
    eve: float
    morn: float


class WeatherDesc(BaseModel):
    class Config:
        extra = Extra.ignore

    main: str
    description: str


class Weather(BaseModel):
    class Config:
        extra = Extra.ignore

    temp: Temp
    feels_like: FeelsLike
    humidity: int
    wind_speed: float

    weather: List[WeatherDesc]


def get_today_at_timezone(tzname: str) -> Tuple[dt.date, dt.timezone]:
    tz = pytz.timezone(tzname)
    now = datetime.now(tz)
    return now.date(), tz


class GeocodingAPI:
    def __init__(self, key: str):
        self.key = key

    def get_coordinates(self, address: str):
        resp = httpx.get(
            "http://www.mapquestapi.com/geocoding/v1/address",
            params={"key": self.key, "location": address},
        ).json()

        if len(resp["results"]) > 0:
            locations = resp["results"][0]["locations"][0]
            return Coords(**locations["latLng"])

        return None


class WeatherAPI:
    def __init__(self, key: str):
        self.key = key

    def get_weather_today(self, coords: Coords):
        resp = httpx.get(
            "https://api.openweathermap.org/data/2.5/onecall",
            params={
                "lat": coords.lat,
                "lon": coords.lng,
                "part": "daily",
                "appid": self.key,
                "units": "metric",
                "lang": "ru",
            },
        ).json()

        today, tz = get_today_at_timezone(resp["timezone"])

        weather_by_day = {
            datetime.utcfromtimestamp(float(day["dt"]))
            .astimezone(tz)
            .date(): day
            for day in resp["daily"]
        }

        res = weather_by_day[today]

        return Weather.parse_obj(res)


class GeoWeatherAPI:
    def __init__(self, mapquest_key: str, openweathermap_key: str):
        self.geo = GeocodingAPI(mapquest_key)
        self.weather = WeatherAPI(openweathermap_key)

    def get_today_weather_for_address(self, address: str) -> Weather:
        return self.weather.get_weather_today(self.geo.get_coordinates(address))
