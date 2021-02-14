import requests
import os
from twilio.rest import Client

account_sid = "removed"
auth_token = "removed"
api_key = os.environ.get("OWM_API_KEY")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "appid": api_key,
    "lat": 50.8284,
    "lon": -0.1395,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, parameters)
response.raise_for_status()
data = response.json()
hourly_12_hours = data["hourly"][0:12]
will_rain = False

hourly_ids = [i["weather"][0]["id"] for i in hourly_12_hours]

for i in hourly_ids:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+removed',
        to='+removed'
    )
    print(message.status)