import requests

name = 'Австралия'
response = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru')
a = response.json()
print(a)
print(a['weather'][0]['description'])  # описание
print(a['main']['temp']) # температура
print(a['main']['feels_like']) # ощущается как
print(a['wind']['speed']) # ощущается как

