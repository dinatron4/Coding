import requests
from datetime import datetime
import time

MY_LAT = 47.4979
MY_LONG = 19.0402
FORMAT = 0

def is_iss_overhead():
    #Getting the request for ISS position
    response_ISS = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_ISS.raise_for_status()
    data_ISS = response_ISS.json()

    lat_ISS = float(data_ISS["iss_position"]["latitude"])
    lng_ISS = float(data_ISS["iss_position"]["longitude"])
    print(lat_ISS, lng_ISS)
    if MY_LAT - 5 <= lat_ISS <= MY_LAT + 5 and MY_LONG - 5 <= lng_ISS <= MY_LONG + 5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": FORMAT,
    }

    #Getting the request for sunrise and sunset time
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #Current time
    time_now = datetime.now()

    print(f"Sunrise at {sunrise}")
    print(f"Sunset at {sunset}")
    print(f"Current time {time_now.hour}")
    
    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Look up!!!")