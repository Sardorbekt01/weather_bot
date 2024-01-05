from django.urls import path
from .views import *

urlpatterns = [
    path('',main1,name='main'),
    path('save-weather-message/', save_weather_message, name='save_weather_message')
]