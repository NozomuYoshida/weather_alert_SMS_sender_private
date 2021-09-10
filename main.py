# This program needs api key of OpenWeather: https://openweathermap.org/
# To run, replace API_KEY to your own api key (registration needed)
# Other APIs to explore: https://apilist.fun/

import os
import requests
from twilio.rest import Client
# Uncomment below if you use python anywhere
# from twilio.http.http_client import TwilioHttpClient

URL = 'https://api.openweathermap.org/data/2.5/onecall'

# Morioka
MY_LATITUDE = 39.697922
MY_LONGITUDE = 141.155991
# Tsukuba
TSUKUBA_LATITUDE = 36.177780
TSUKUBA_LONGITUDE = 140.093735
# BANGKOK
BANGKOK_LATITUDE = 13.756331
BANGKOK_LONGITUDE = 100.501762

# Environment variable
API_KEY = os.environ.get('OWM_API_KEY')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

API_KEY_NAME = 'python'

ACCOUNT_SID = 'ACd3fd405688dcd594ee8f73ca840931ff'
PHONE_NUMBER = '+19165896015'
MY_PHONE_NUMBER = '+819058456340'

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)


def send_sms(from_phone_number, to_phone_number):
    # Switch the statement below if you use python anywhere
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella🌂",
        from_=from_phone_number,
        to=to_phone_number
    )
    print(message.status)



parameters = {
    # 'lat': MY_LATITUDE,
    # 'lon': MY_LONGITUDE,
    'lat': TSUKUBA_LATITUDE,
    'lon': TSUKUBA_LONGITUDE,
    # 'lat': BANGKOK_LATITUDE,
    # 'lon': BANGKOK_LONGITUDE,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()

weather_data_hourly_list = weather_data['hourly']
weather_id_next_12hours_list = []
for weather_data_hourly in weather_data_hourly_list[0:12]:
    # print(weather_data_hourly)
    weather_id_hourly = weather_data_hourly['weather'][0]['id']
    weather_id_next_12hours_list.append(weather_id_hourly)
print(weather_id_next_12hours_list)

for weather_id in weather_id_next_12hours_list:
    if weather_id < 700:
        # Uncomment below if you use python anywhere
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        print('Bring an Umbrella')
        send_sms(PHONE_NUMBER, MY_PHONE_NUMBER)
        break

