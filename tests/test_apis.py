import pytest

from simple_weather_bot.api import Coords, GeocodingAPI, WeatherAPI


@pytest.fixture()
def geo_api(config) -> GeocodingAPI:
    return GeocodingAPI(config.mapquest_key)


@pytest.fixture()
def weather_api(config):
    return WeatherAPI(config.openweathermap_key)


@pytest.fixture()
def moscow_coords(geo_api) -> Coords:
    return geo_api.get_coordinates("Россия, Москва, Ленинские горы дом 1")


def test_geocoding_moscow(moscow_coords):
    assert moscow_coords is not None


def test_weather_moscow(moscow_coords, weather_api):
    assert weather_api.get_weather_today(moscow_coords) is not None
