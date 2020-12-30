#!/usr/bin/python
import RPi.GPIO as gpio 
from time import sleep 
from random import uniform

gpio.setwarnings(False) 
gpio.setmode(gpio.BCM) 

class Led:
    def __init__(self, colour, pin):
        self.colour = colour
        self.pin = pin

    def setup(self, pin):
        gpio.setup(pin, gpio.OUT, initial=gpio.LOW)

color2gpio = []
color2gpio.append(Led("red", 5))
color2gpio.append(Led("green", 6))
color2gpio.append(Led("blue", 13))

for led in color2gpio:
    print("Colour : {}, Gpio : {}".format(led.colour, led.pin))
    Led.setup(led, led.pin)

while True: 
    for i in color2gpio:
        gpio.output(i.pin, gpio.HIGH) 
        rounded = round(uniform(0.1, 0.6),1)
        print("Run:", rounded)
        sleep(rounded) 
        gpio.output(i.pin, gpio.LOW) 
        rounded = round(uniform(0.1, 4.8),1)
        print("Sleep:", rounded)
        sleep(rounded) 
