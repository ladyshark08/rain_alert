import requests
import smtplib
import os

my_email = "testludemy@gmail.com"
password = ""

api_key = os.environ.get("API_KEY")

parameters = {
    "lat": 49.248810,
    "lon": -122.980507,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)

result = response.json()['list']


def will_it_rain():
    for data in result:
        for info in data['weather']:
            p = (info['id'])
            if p < 700:
                return "it's going to rain today.Bring an umbrella and a raincoat"
    return "Not raining today"


with smtplib.SMTP("smtp.gmail.com", port=587) as new_connect:
    new_connect.starttls()
    message = f'Subject: Rain Forecast\n\nHey Buddy,\n\n{will_it_rain()}'
    new_connect.login(user=my_email, password=password)
    new_connect.sendmail(from_addr=my_email, to_addrs="ladyshark08@proton.me",
                         msg=message)
