import unittest
from unittest.mock import patch
from api_weather.views import get_coordinates


class TestGetCoordinates(unittest.TestCase):

    @patch('api_weather.views.Nominatim')
    def test_get_coordinates_success(self, mock_geolocator):
        # Настройка имитации
        mock_location = mock_geolocator.return_value.geocode.return_value
        mock_location.latitude = 55.1
        mock_location.longitude = 53.0

        # Вызов функции
        latitude, longitude = get_coordinates("Оренбург")

        # Проверка результатов
        self.assertEqual(latitude, 55.1)
        self.assertEqual(longitude, 53.0)

    @patch('api_weather.views.Nominatim')
    def test_get_coordinates_failure(self, mock_geolocator):
        # Настройка имитации для случая, когда город не найден
        mock_geolocator.return_value.geocode.return_value = None

        # Вызов функции
        latitude, longitude = get_coordinates("НеизвестныйГород")

        # Проверка результатов
        self.assertIsNone(latitude)
        self.assertIsNone(longitude)


if __name__ == '__main__':
    unittest.main()
