#!usr/bin/python3

DEBUG = False

import sys
import Adafruit_DHT
import requests
import sqlite3
import time

data_pin = 17

ts = time.time()
room = requests.get("http://nogordio.com/hum.txt").text
forecast = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Seixal,PT&APPID=0e3c908e4eb2f5ae39116b7f67c31130")
forecast_data = forecast.json()
ext_temp = forecast_data['list'][0]['main']['temp'] 
ext_hum = forecast_data['list'][0]['main']['humidity']
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,data_pin)

if DEBUG == True:
    print(room)
    print(ts)
    print(ext_temp)
    print(ext_hum)
    print(temperature)
    print(humidity)
else:
    conn = sqlite3.connect('hum.db')
    # Do this instead
    t = (ts, room, ext_temp, ext_hum, temperature, humidity)
    conn.execute('INSERT INTO data (ts, room, ext_temp, ext_hum, int_temp, int_hum) VALUES (?,?,?,?,?,?)', t)
    conn.commit()
    conn.close()
sys.exit()
