# simple-weather-bot

<div align="center">


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/hexfaker/simple-weather-bot/blob/master/.pre-commit-config.yaml)
[![License](https://img.shields.io/github/license/hexfaker/simple-weather-bot)](https://github.com/hexfaker/simple-weather-bot/blob/master/LICENSE)

</div>


# Для школы CTO

### Задача и уровень сложности
Умный сервис погоды, сложность со звездочкой

### Технологии 
python 3.8, docker и docker-compose, telegram

### Интерфейс
Консоль и телеграм-бот, принимающий адрес и возвращающий текст с описанием погоды.

### Формат ответа
Текстовый шаблон. Данные о погоде подставляются из [Open Weather Map](https://openweathermap.org/).
Рекомендации одежды составляются по списку критериев, заданных в коде.
Адрес преобразуется в координаты при помощи сервиса [Map Quest](https://developer.mapquest.com/)

```
Погода на сегодня: <краткое описание>


🌡 Температура:

    Утро: <X>°C (<X>°C по ощущениям)
    День: <X>°C (<X>°C по ощущениям)
    Вечер: <X>°C (<X>°C по ощущениям)

💧 Влажность: <X>%

🌬 Скорость ветра: <X> м/с

👚 Следует надеть: <список рекомендуемой одежды>
```

### Демо (видео)
[Видео](http://www.youtube.com/watch?v=al2XYCOsLio)

Попробовать бота самим можно в [telegram](https://t.me/hexweather_bot).

### Описание работы
1. Пользователь отправляет адрес через интерфейс мессенджера
2. Сервер получив этот адрес, преобразует его в координаты при помощи отправки запроса в
сервис  [Map Quest](https://developer.mapquest.com/).
3. Полученные координаты сервер отправляет в сервис [Open Weather Map](https://openweathermap.org/),
и получает в ответ прогноз погоды на неделю в этой координате.
4. Из прогноза выбирается день, в котором та же дата, что и в том месте, где эта координата находится с, учетом часовых поясов. 
Часовой пояс так же приходят в ответе от Open Weather Map.
5. После этого по этому прогнозу формируется текстовый ответ путем подстановки в шаблон.
    * В частности информация о прогнозе прогоняется через список критериев, 
        которые формируют список рекомендуемой одежды.
6. После этого текстовый ответ отправляется обратно пользователю.

# Как запустить?
1. Получить ключи от [Map Quest](https://developer.mapquest.com), [Open Weather Map](https://openweathermap.org/), telegram.
2. В корне проекта скопировать файл `default.example.env` в `default.env`, в последний поместить полученные ключи в соответствующие строки.
3. Установить docker и docker-compose
4. Выполнить команду `docker-compose up -d`.
 
## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
