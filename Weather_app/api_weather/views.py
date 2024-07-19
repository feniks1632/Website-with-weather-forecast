from django.shortcuts import render
from pathlib import Path
import os
from django.db.models import F
from geopy.geocoders import Nominatim
import requests
from django.http import JsonResponse
from .models import SearchHistory



#достаем кооридинаты города
def get_coordinates():
    geolocator = Nominatim(user_agent="api_weather")
    adress = "Оренбург"
    location = geolocator.geocode(adress)
    if location:
        return location.latitude, location.longitude
    return None


def request_to_api(request):
    # словарь переводчик
    translation_dict = {
        "time": "время",
        "interval": "интервал",
        "temperature_2m": "температура",
        "relative_humidity_2m": "влажность",
        "apparent_temperature": "ощущаемая температура",
        "weather_code": "код погоды",
        "wind_speed_10m": "скорость ветра",
        "wind_direction_10m": "направление ветра",
    }
    # словарь с кодами погоды
    weather_code_dict = {
        0: "Чистое небо",
        1: "Преимущественно ясно, переменная облачность и пасмурно",
        2: "Преимущественно ясно, переменная облачность и пасмурно",
        3: "Преимущественно ясно, переменная облачность и пасмурно",
        45: "Туман и отложение инея",
        48: "Туман и отложение инея",
        51: "Морось: легкая",
        53: "Морось: умеренная",
        55: "Морось: интенсивная",
        56: "Моросящий дождь: легкая интенсивность",
        57: "Моросящий дождь: плотная интенсивность",
        61: "Дождь: небольшой",
        63: "Дождь: умеренной интенсивности",
        65: "Дождь: сильной интенсивности",
        66: "Ледяной дождь: небольшой",
        67: "Ледяной дождь: сильной интенсивности",
        71: "Снегопад: слабой интенсивности",
        73: "Снегопад: умеренной интенсивности",
        75: "Снегопад: сильной интенсивности",
        77: "Снежные зерна",
        80: "Ливни: слабые",
        81: "Ливни: умеренные",
        82: "Ливни: сильные",
        85: "Небольшой снегопад",
        86: "Сильный снегопад",
        95: "Гроза: Слабая или умеренная",
        96: "Гроза с небольшим градом",
        99: "Гроза с сильным градом",
    }
    # получаем параметры запроса
    res = SearchHistory.objects.all()
    print(res)
    # Сохранение истории поиска
    if  res.user_id:
        SearchHistory.objects.create(user_id=user_id, city=city, count_city=1)
    if res.user_id and res.city:
        SearchHistory.objects.update(count_city=F('count_city')+1)

    # заполняем словарь с параметрами запроса, координатами и URL и получаем ответ от сервера
    latitude, longitude = get_coordinates()
    api_path = "https://api.open-meteo.com/v1/forecast?"
    data = "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": data
    }
    response = requests.get(api_path, params=params)
    result = response.json()["current"]

    # выыод текущего статуса погоды
    status_weather = result["weather_code"]
    real_status_weather = weather_code_dict[status_weather]

    # перевод ключей в русский язык
    translated_response = {translation_dict.get(
        key, key): value for key, value in result.items()}
    
    return translated_response, real_status_weather
