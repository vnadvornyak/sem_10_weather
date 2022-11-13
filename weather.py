import requests

def weather(name: str):
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru')
    a = response.json()
    description = a['weather'][0]['description']  # описание
    temp = a['main']['temp']  # температура
    feel = a['main']['feels_like']  # ощущается как
    wind = a['wind']['speed']  # ветер
    return f'В этой стране сейчас {description}.\nСредняя температура {temp}. Ощущается как {feel}.\nСкорость ветра {wind} м/с.'
