import requests

from datetime import datetime as dt

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # print(response.status_code)
#
#
# data = response.json()
# # print(data)
#
# longitude = data["iss_position"]["longitude"]
# # print(longitude)
#
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
# print(iss_position)


MY_LAT = 20.593683

MY_LNG = 78.962883

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)

sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)

time_now = dt.now()
hour = time_now.hour
print(hour)






