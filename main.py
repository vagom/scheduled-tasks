ILimport os
import requests
from twilio.rest import Client

# # ******************** My e-mail credentials *********************
# my_email = os.environ.get("MY_EMAIL")
# my_password = os.environ.get("MY_EMAIL_PASSWORD")
# # ****************************************************************

# ******************** Phone credentials *********************
my_mobile = os.environ.get("MY_MOBILE")

# ****************************************************************

# ******************** Piracicaba lat, lon ***********************
MY_LAT = -22.725165
MY_LON = -47.6493269
# ****************************************************************

# ******************** OpenWeather parameters ********************
owm_api_key = os.environ.get("OWM_API_KEY")
owm_endpoint = os.environ.get("OWM_ENDPOINT")
# ****************************************************************

# ******************** Twilio parameters *************************
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
msg_serv_sid = os.environ.get("TWILIO_MSG_SID")
twilio_phone = os.environ.get("TWILIO_PHONE")
# ****************************************************************

owm_params = {
    "lat" : MY_LAT,
    "lon" : MY_LON,
    "cnt" : 4,
    "APPID" : owm_api_key
}

response = requests.get(url=owm_endpoint, params=owm_params)
response.raise_for_status()
weather_data = response.json()
response_code = weather_data["cod"]

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code <= 700:
        will_rain = True

if will_rain:
    print(will_rain)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=msg_serv_sid,
        body='Better bring an Umbrella! ☔',
        from_=twilio_phone,
        to=my_mobile
    )

