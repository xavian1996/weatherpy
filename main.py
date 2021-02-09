import requests
from prettytable import PrettyTable

city = input('Enter City => ')#City name here
api = "b70fa075d4b9d69d8fc57f4b199d9f68"#api of https://openweathermap.org get urs from the website
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}")#request a response

#if the response equal 200 = OK thats mean everything is okey

weather = response.json()["weather"]#get weather info
temp = response.json()["main"]#get temperature info
wind = response.json()["wind"]#get wind info
clouds = response.json()["clouds"]#get clouds info
coord = response.json()["coord"]#get coordinates


weather_cloud = weather[0]["description"]

temp_feels = temp["temp"]
temp_feels_like = temp["feels_like"]
temp_feels_min = temp["temp_min"]
temp_feels_max = temp["temp_max"]

wind_speed = wind["speed"]

clouds_deg = clouds["all"]

coordination_lon = coord["lon"]
coordination_lat= coord["lat"]
#write everything into a table
table = PrettyTable()

table.field_names = ["City",
                     "weather Description",
                     "Temperature",
                     "Feels Like",
                     "Temperature Min",
                     "Temperature Max",
                     "Win Speed",
                     "Cloud",
                     "Coordinates Long",
                     "Coordinates Lat"]
table.add_row([city.capitalize(),
               weather_cloud,
               temp_feels,
               temp_feels_like,
               temp_feels_min,
               temp_feels_max,
               wind_speed,
               clouds_deg,
               coordination_lon,
               fescoordination_lat])

print(table)