import os
import uuid

from pathlib import Path

import requests
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from geopy.geocoders import Nominatim

from api_weather.models import SearchHistory

#записываем куки
def index(request):
    user_id = request.COOKIES.get('user_id')

    if not user_id:
        user_id = str(uuid.uuid4())
        response = render(request, 'index.html', {})
        response.set_cookie('user_id', user_id)
        return response

    recent_searches = SearchHistory.objects.filter(user_id=user_id)[:5]
    context = {
        'recent_searches': recent_searches
    }

    return render(request, 'index.html', context=context)


def request_to_api(request):
    # Получаем параметры запроса
    city = request.GET.get('city')

    # Проверить пустой ли он
    if not city:
        return JsonResponse(
            {"error": "Необходимо ввести название города"}, status=400)

    latitude, longitude = get_coordinates(city)

    if latitude is None or longitude is None:
        return JsonResponse(
            {"error": "Введите корректное название города"}, status=404)

    # Получить куки и историю поиска
    user_id = request.COOKIES.get('user_id')
    res = SearchHistory.objects.filter(user_id=user_id, city=city)

    if not res:
        SearchHistory.objects.create(user_id=user_id, city=city, count_city=1)
    else:
        res.update(count_city=F('count_city') + 1)

    api_path = "https://api.open-meteo.com/v1/forecast"
    data = "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": data
    }

    response = requests.get(api_path, params=params)

    if response.status_code != 200:
        return JsonResponse(
            {"error": "Ошибка при получении данных о погоде"}, status=500)

    result = response.json().get("current")
    print(result)

    status_weather = result["weather_code"]

    return JsonResponse({
        "weather_response": result,
        "real_status": status_weather
    })


def get_coordinates(city):
    geolocator = Nominatim(user_agent="api_weather")
    location = geolocator.geocode(city)
    if location:
        print(location.latitude, location.longitude)# оставили для проверки координат :)
        return location.latitude, location.longitude
    return None, None
