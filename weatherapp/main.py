import telebot
import requests
import os
from telebot.types import Message
import weatherapp
import django
from .models import WeatherMessage
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()

BOT_TOKEN = '6981534767:AAFlwBKGSoCPkSgbs61LOXV2SPDhLd8Zqy0'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum botimizga xush kelibsiz ! ")

@bot.message_handler(commands=['weather'])
def weather(message):
    city = message.text[9:]
    data = get_full_data(city)
    holatuz = {'Clear':"Musaffo osmon", "Sunny": "Quyoshli osmon", "Clouds":"Bulutli"}
    holat = data.get("weather")[0].get("main", "xatolik")
    a = None
    try:
        a = holatuz[holat]
    except:
        a = "Bilmayman hozir havo holati qanaqa ekanligini"
    location = data.get("sys",{}).get('country')
    temp = round(data.get("main", {}).get('temp', 0) - 273.15)
    bot.send_message(message.chat.id, f"hozirda {city}da havo harorati +{temp} C bo'lishi kutulmoqda va {city} joylashgan davlat {location}, shuningdek {city} shahri osmoni hozirda {a}. (Ps. Clouds - Bulutli, Clear - Musaffo, Rain - Yomg'irli degan ma'noda) !..")
@bot.message_handler(commands=['posts'])
def get_posts(message):
    weather_messages = WeatherMessage.objects.all()
    for message in weather_messages:
        print(f"Sent at {message.sent_time} to {message.recipient_email}: {message.content}")




def get_full_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?appid=9d797cbb0255e00be40ea9eccfc36d8b&q={}'.format(city)
    response = requests.get(url)
    return response.json()




