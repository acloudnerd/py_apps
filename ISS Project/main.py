import requests
from datetime import datetime
MY_LATITUTE = -26.099456787109375
MY_LONGITUDE = 28.053760528564453

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code)
# response.raise_for_status()

# data = response.json()

# # print(data["iss_position"]["latitude"])

# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# the_current_position = (latitude, longitude)

# print(the_current_position)

parameters = {
    "lat": MY_LATITUTE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)
response.raise_for_status()
data = response.json()
sunset = data["results"]["sunset"]
sunrise = data["results"]["sunrise"]

print(type(sunrise), sunset)

# print(datetime.now())

