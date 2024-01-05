from django.shortcuts import render
from django.shortcuts import render
from django. views. decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse 
import telebot
from .main import bot
import logging
from .models import WeatherMessage

def main1(request):
    return HttpResponse('Bot ishladi')


@csrf_exempt
def index(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("Telegram Bot")
    if request.method == 'POST':
        update = telebot.types.Update.de_json(
            request.body.decode("utf-8"))
        try:
           bot.process_new_updates([update])
        except Exception as e:
           logging.error(e)
        return HttpResponse(status=200)

def save_weather_message(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        recipient_email = request.POST.get('recipient_email', '')

        weather_message = WeatherMessage(content=content, recipient_email=recipient_email)
        weather_message.save()

        return HttpResponse("Ma'lumot saqlandi!")
    else:
        return HttpResponse("Noto'g'ri so'rov turi")
