
import requests
import time
import random  
THINGSPEAK_API_KEY = ''
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

def send_data_to_thingspeak(temperature, humidity):
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': temperature,
        'field2': humidity
    }
    response = requests.get(THINGSPEAK_URL, params=payload)
    if response.status_code == 200:
        print(f"Data sent successfully: Temp={temperature}, Humidity={humidity}")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")

while True:
    temp = round(random.uniform(25, 35), 2)
    hum = round(random.uniform(50, 70), 2)
    send_data_to_thingspeak(temp, hum)
    time.sleep(5)  
