from pathlib import Path

import dotenv
import pytest

from simple_weather_bot.config import Config


@pytest.fixture
def config():
    path = Path("default.env")
    assert path.exists()
    dotenv.load_dotenv(path)
    return Config()
