#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, time, datetime
import sys
import urllib            # URL functions
import urllib2           # URL functions
import inspect
# now paho
import paho.mqtt.publish as publish



# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before. 
tfile = open("/sys/bus/w1/devices/28-000007d47604/w1_slave") 
# Read inside temp of the text in the file. 
text = tfile.read() 
tfile.close() 
secondline = text.split("\n")[1] 
temperaturedata = secondline.split(" ")[9] 
temperature = float(temperaturedata[2:]) 
ti = temperature / 1000 
tii = ("{0:.1f}".format(round(ti,1)))
print "in", tii
tiii = float(tii)
tig = tiii - 2
time.sleep (2)


# insert data into MQTT Broker 192.168.123.91
##    

# Now we going to try Mqtt
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
#
publish.single("ajhome/tempshed", payload=tig, qos=1, retain=True, hostname="192.168.123.91", port=1883, client_id="", keepalive=60, will=None, auth = {'username':"inexeng", 'password':"booboo34"}, tls=None)
#
time.sleep (1)
#
#
print "sent ", tig
#
sys.exit()
