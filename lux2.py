#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import sys, os
import time
from time import sleep   
import pickle
import RPi.GPIO as GPIO 

     

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(2)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
while True:
        list = [0];
        for a in range(1, 11):                              
            # print RCtime(17)     # Read RC timing using pin #17
            w = float(RCtime(17)) 
            x = 1/w
            y = (x * 100000)
            lux = round(y, 1)
            print "lux ", lux 
            time.sleep(1)
            list.append ( lux );
        print "max is ", max(list)
        mlux = max(list)
        pickle.dump(mlux, open( "lux.p", "wb" ))
