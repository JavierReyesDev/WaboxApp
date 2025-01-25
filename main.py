import requests
from random import randint

RECIPIENT = "" # Add your phone number here (e.g., +1234567890 including country code)
API_KEY = "" # Add your API key here (Get it from https://www.waboxapp.com)
url = "https://www.waboxapp.com/api/send/chat"

def get_unique_id():
    num = "{:20d}".format(randint(0,9999999999999999999))
    return f"uid{num}"

unique_id = get_unique_id()
message = "Reminder of the day..." # Add your message here
params = {
    "token":API_KEY,
    "uid":RECIPIENT,
    "to":RECIPIENT,
    "custom_uid":unique_id,
    "text":message
}

try:
    response = requests.post(url=url, json=params)
    response.raise_for_status()
    print("Whatsapp message sent")
except requests.exceptions.RequestException as e:
    print(f"Error sending the message: {response.status_code}, Response: {response.text}")
