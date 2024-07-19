from django.urls import path
from . import views

urlpatterns = [

    path('request_to_api/', views.request_to_api),
    path('get_coordinates/', views.get_coordinates),
]