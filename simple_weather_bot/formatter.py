from .api import Weather


def need_umbrella(weather: Weather):
    if any(["дождь" in w.description for w in weather.weather]):
        return ["возьмите зонт 🌂"]
    return []


def top(weather: Weather):
    t = weather.feels_like.day

    if 30 <= t < 35:
        return ["майку"]
    if 20 <= t < 30:
        return ["футболку или рубашку с коротким рукавом"]
    if 15 <= t < 20:
        return ["толстовку или свишот"]
    if 5 <= t < 15:
        return ["легкую куртку или ветровку"]
    if -5 <= t < 5:
        return ["пальто или утепленную куртку"]
    if -15 <= t < -5:
        return ["пуховик или шубу"]
    if t < -15:
        return ["пуховик или шубу со свитером"]
    if t >= 35:
        return ["да можно и голым в такую жару, никто не осудит"]


def bottom(weather):
    t = weather.feels_like.day

    if t > 20:
        return ["шорты"]
    if 5 < t <= 20:
        return ["любые штаны"]
    if -10 < t <= 5:
        return ["штаны", "термобелье"]
    if t < -10:
        return ["теплые ватные штаны"]


def make_clothes_list(weather: Weather):
    res = []
    for c in [top, bottom, need_umbrella]:
        res += c(weather)

    return ", ".join(res)


def format_weather(weather: Weather):
    return (
        f"Погода на сегодня: *{weather.weather[0].description}*\n\n\n"
        f"🌡 Температура:\n\n"
        f"    Утро: {weather.temp.morn:.0f}°C ({weather.feels_like.morn:.0f}°C по ощущениям)\n"
        f"    День: {weather.temp.day:.0f}°C ({weather.feels_like.day:.0f}°C по ощущениям)\n"
        f"    Вечер: {weather.temp.eve:.0f}°C ({weather.feels_like.eve:.0f}°C по ощущениям)\n\n"
        f"💧 Влажность: {weather.humidity}%\n\n"
        f"🌬 Скорость ветра: {weather.wind_speed} м/с\n\n"
        f"👚 Следует надеть: {make_clothes_list(weather)}"
    )
