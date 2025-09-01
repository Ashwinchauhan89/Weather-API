from django.shortcuts import render
import requests
import datetime

def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Ujjain'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=02558e7431818066156e0be688575dde'
    PARAMS = {'units': 'metric'}

    try:
        response = requests.get(url, params=PARAMS)
        data = response.json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        date = datetime.date.today()

        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'date': date,
            'city': city,
        }

    except (KeyError, IndexError, requests.exceptions.RequestException):
        context = {
            'error': 'Could not retrieve weather data. Please check the city name or try again later.',
            'city': city
        }

    return render(request, 'index.html', context)
