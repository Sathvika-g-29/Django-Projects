import requests
from django.conf import settings
from django.shortcuts import render


def home(request):
    weather_data={}
    error=""
    if request.method== "POST":
        city=request.POST.get('city')
        api_key=getattr(settings, "OPENWEATHER_API_KEY", "")
        if not api_key:
            error="Weather API key is not configured."
            return render(request,"home.html",{"weather":weather_data,"error":error})
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response=requests.get(url)
        data=response.json()
        if data["cod"]==200:
            weather_data={
                "city":city,
                "temperature":data["main"]["temp"],
                "humidity":data["main"]["humidity"],
                "wind":data["wind"]["speed"],
                "description":data["weather"][0]["description"]
            }
        else:
            error="City not found.Please eneter a valid city name."
    return render(request,"home.html",{"weather":weather_data,"error":error})
