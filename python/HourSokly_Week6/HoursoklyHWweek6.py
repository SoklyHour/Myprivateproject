import requests
api_key = 'd1bb067f227391f80404e48c793bbf0d'
user_input = input("Enter your search location: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("city not found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temparature= ( temp - 32 ) * 5/9
    print(f"The weather in {user_input} is {weather} with the temperature of {temparature}c")

