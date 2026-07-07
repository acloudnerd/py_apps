import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
response.raise_for_status()

data = response.json()

# print(data["iss_position"]["latitude"])

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

the_current_position = (latitude, longitude)

print(the_current_position)
