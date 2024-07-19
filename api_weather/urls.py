from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request_to_api/', views.request_to_api, name='request_to_api'),
    path('get_coordinates/', views.get_coordinates, name='get_coordinates'),
]