#!/usr/bin/python
import RPi.GPIO as gpio 
from time import sleep 
from random import uniform

gpio.setwarnings(False) 
gpio.setmode(gpio.BCM) 

color2gpio = {"red" : 5, "green" : 6, "blue" : 13}

for value in color2gpio.values():
    gpio.setup(value, gpio.OUT, initial=gpio.LOW)

while True: 
    for i in color2gpio.values():
        gpio.output(i, gpio.HIGH) 
        rounded = round(uniform(0.1, 0.6),1)
        print "Run:", rounded
        sleep(rounded) 
        gpio.output(i, gpio.LOW) 
        rounded = round(uniform(0.1, 4.8),1)
        print "Sleep:", rounded  
        sleep(rounded) 
