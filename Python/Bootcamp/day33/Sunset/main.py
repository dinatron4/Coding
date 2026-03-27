import requests
from datetime import datetime

MY_LAT = 47.4979
MY_LONG = 19.0402
FORMAT = 0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": FORMAT,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# sunrise = sunrise.replace("T", " ").rstrip("0+:")
# sunset = sunset.replace("T", " ").rstrip("0+:")

time_now = datetime.now()

print(f"Sunrise at {sunrise}")
print(f"Sunset at {sunset}")
print(f"Current time {time_now.hour}")