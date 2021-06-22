import requests
from datetime import datetime

api_key = '758093beb3bd2776951491e29bcab162'
city = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#variables to store and display data
temperature=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
humidity=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#print the data
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
print ("-------------------------------------------------------------")

print("Current weather description : ",weather_desc)
print("Currrent temp : {:.2f} deg C".format(temperature))
print("Current humidity : ",humidity,'%')
print("Current wind speed : ",wind_speed,'kmph')

#saving in txt file
with open('weather_data.txt', 'a') as f:
    f.write("-------------------------------------------------------------"+"\n")
    f.write("Weather Stats for - {}  || {}".format(city.upper(), date_time+"\n"))
    f.write("-------------------------------------------------------------"+"\n")

    f.write("Current weather description : "+str(weather_desc)+"\n")
    f.write("Currrent temp : {:.2f} deg C".format(temperature)+"\n")
    f.write("Current humidity : "+str(humidity)+'%'+"\n")
    f.write("Current wind speed : "+str(wind_speed)+'kmph'+"\n")
    f.close()
