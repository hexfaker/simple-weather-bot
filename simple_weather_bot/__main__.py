# type: ignore[attr-defined]

import typer

from simple_weather_bot.bot import run_bot

from .api import GeoWeatherAPI
from .config import Config
from .formatter import format_weather

app = typer.Typer(
    name="simple-weather-bot",
    help="Simple bot telling weather and recommending clothes",
    add_completion=False,
)


@app.command()
def serve_bot():
    """Запускает бота для telegram"""

    run_bot(Config.load())


@app.command()
def show(address: str):
    """Звпрашивает погоду по адресу и выводит ответ"""

    config = Config.load()
    api = GeoWeatherAPI(config.mapquest_key, config.openweathermap_key)

    print(format_weather(api.get_today_weather_for_address(address)))


def main():
    app()


if __name__ == "__main__":
    main()
