import json
import requests

api_key = '6515bb3582e8427298c0c38d2ada0508' # u can use my own api-key
defolt_url = "https://api.openweathermap.org/data/2.5/weather?"
city = str(input("Enter ur full city name: "))
url = defolt_url + "q=" + city + "&units=metric" + "&appid=" + api_key
response = requests.get(url)


if response.status_code == 200:
   data = response.json()   
   main = data['main']
   temperature = main['temp']  
   humidity = main['humidity']  
   pressure = main['pressure']  
   report = data['weather']
   print(f"{city:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else: 
   print("Error in the HTTP request")