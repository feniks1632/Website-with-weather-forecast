# Прогноз погоды
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Geopy](https://img.shields.io/badge/-Geopy-464646?style=flat-square&logo=Geopy)](https://geopy.readthedocs.io/en/stable/index.html)
[![Open_Meteo](https://img.shields.io/badge/-Open_meteo-464646?style=flat-square&logo=Open_meteo)](https://open-meteo.com/)
## Описание
Сайт для получения прогноза погоды по введенному названию города. Пользователи могут вводить название города, и приложение отображает текущие данные о погоде, включая температуру, влажность, скорость и направление ветра.

### Функциональность

- Получение текущих данных о погоде по введенному названию города.
- Отображение истории недавних запросов.
- Обработка ошибок для некорректных вводов и проблем с API.

#### Технологии

- Django: веб-фреймворк для разработки серверной части.
- Geopy: библиотека для геокодирования (получения координат по названию города).
- Open Meteo API: API для получения данных о погоде.
- HTML/CSS/JavaScript: для фронтенд-разработки.

### Установка

## 1. Клонируйте репозиторий:

```bash
   git clone <название репозитория>
   cd <ваш_репозиторий>
```

## 2. Создайте и активируйте виртуальное окружение:
```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Window
```

## 3. Установите зависимости проекта
```bash
   pip install -r requirements.txt
```

## 4. Выполните миграции базы данных
```bash
   python manage.py makemigrations
   python manage.py migrate
```

## 5. Запустите сервер разработки
```bash
   python manage.py runserver
```

## 6. Откройте браузер и перейдите по адресу: http://127.0.0.1:8000

### Использование
# 1. Введите название города в текстовое поле.
# 2. Нажмите кнопку "Получить погоду".
# 3. Просмотрите текущие данные о погоде для введенного города.
# 4. Просмотрите историю недавних запросов.

## Тестирование
Для запуска тестов используйте следующую команду:
```bash
   python manage.py test
```

#### Автор проекта

Никита Бражников - (https://github.com/feniks1632)
