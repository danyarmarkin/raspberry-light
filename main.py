import requests
import json
import time
from math import *
try:
    import RPi.GPIO as gpio
except:
    pass

lamps = [2, 3, 4, 17, 27, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8]

value = 0
calibrate = 0
lampsOff = 0

gpio.setmode(gpio.BCM)
for i in lamps:
    print(i)
    gpio.setup(i, gpio.OUT)
    gpio.output(i, gpio.LOW)
    time.sleep(0.1)
time.sleep(1)

# switch off lamps
def lamp(v, c, off):
    global lamps
    d = v - c
    if d < 0:
        d += 360
    l = floor(d / (360 / len(lamps)))
    if l >= len(lamps):
        l = len(lamps) - 1
    for i in lamps:
        gpio.output(i, gpio.HIGH)
    print(l)
    ind = 0
    if off % 2 == 0:
        ind = 1
    for i in range(int(l - floor(off / 2 - ind)), int(l + floor(off / 2)) + 1, 1):
        j = i
        if j < 0:
            j += len(lamps)
        if j >= len(lamps):
            j -= len(lamps)
        gpio.output(lamps[j], gpio.LOW)


session = requests.Session()

while True:
    # get response from firebase of compass data
    r = session.get('https://camera-scan-e5684-default-rtdb.europe-west1.firebasedatabase.app/compassData.json?print=pretty')
    responce = json.loads(r.text)
    try:
        print(responce["value"])
        value = int(responce["value"])
        calibrate = int(responce["calibration"])
        lampsOff = int(responce["lampsOff"])
        lamp(value, calibrate, lampsOff)
    except:
        print("error")