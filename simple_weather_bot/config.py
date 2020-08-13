from pydantic import BaseSettings, Field


class Config(BaseSettings):
    mapquest_key: str = Field(env="MAPQUEST_KEY",)

    openweathermap_key: str = Field(env="OPENWEATHERMAP_KEY")
