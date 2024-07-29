import smtplib
import time
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
recipient = os.getenv("RECIPIENT")


def with_in_range():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    iss_latitude = float(response.json()['iss_position']['latitude'])
    iss_longitude = float(response.json()['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url, params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and with_in_range():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=recipient,
                                msg="Subject: ISS Location \n\n The ISS os over head, try and look for it")
