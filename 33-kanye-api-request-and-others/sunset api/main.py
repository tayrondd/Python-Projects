import requests
from datetime import datetime

# https://sunrise-sunset.org/api
# nj location
parameters = {
    "lat": 40.673778,
    "ing": -74.168057,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # check if api return any error except 200
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":"))
sunset = int(data["results"]["sunset"].split("T")[1].split(":"))


time_now = datetime.now()
print(time_now.hour)