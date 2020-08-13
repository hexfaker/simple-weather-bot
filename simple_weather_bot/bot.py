from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher,
    Filters,
    MessageHandler,
    Updater,
)

from .api import GeoWeatherAPI
from .config import Config
from .formatter import format_weather

MESSAGE_HELP = (
    "Привет!\n"
    "Пришли мне адрес и я отвечу погодой по этому адресу на сегодня, а так же подскажу как "
    "одеться по погоде!"
)


def buid_handlers(api: GeoWeatherAPI, dispather: Dispatcher):
    def start(update: Update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text(MESSAGE_HELP)

    def help_command(update: Update, context: CallbackContext):
        """Send a message when the command /help is issued."""
        update.message.reply_text(MESSAGE_HELP)

    def weather(update: Update, context: CallbackContext):
        """Reply with weather"""
        weather = api.get_today_weather_for_address(update.message.text)
        reply = format_weather(weather)
        update.message.reply_markdown(reply)

    dispather.add_handler(CommandHandler("start", start))
    dispather.add_handler(CommandHandler("help", help_command))
    dispather.add_handler(
        MessageHandler(Filters.text & ~Filters.command, weather)
    )


def run_bot(config: Config):
    updater = Updater(config.telegram_token, use_context=True)
    api = GeoWeatherAPI(config.mapquest_key, config.openweathermap_key)
    buid_handlers(api, updater.dispatcher)

    updater.start_polling()

    updater.idle()
