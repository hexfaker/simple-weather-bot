import dotenv
from pydantic import BaseSettings, Field


class Config(BaseSettings):
    mapquest_key: str = Field(env="MAPQUEST_KEY",)

    openweathermap_key: str = Field(env="OPENWEATHERMAP_KEY")

    telegram_token: str = Field(env="TELEGRAM_TOKEN")

    @staticmethod
    def load() -> "Config":
        dotenv.load_dotenv("default.env")
        return Config()
