#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, time, datetime
import sys
import urllib            # URL functions
import urllib2           # URL functions
import inspect
from time import sleep
# now pickle
import pickle
# now paho
import paho.mqtt.publish as publish
#

pres = pickle.load( open( "pres.p", "rb" ))
print "mressure = ", pres
#
# insert data into MQTT Broker 192.168.123.91
#    
# Now we going to try Mqtt
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
#
time.sleep (1)
#
publish.single("ajhome/press", payload=pres, qos=1, retain=True, hostname="192.168.123.91", port=1883, client_id="", keepalive=60, will=None, auth = {'username':"inexeng", 'password':"booboo34"}, tls=None)
#
print "sent ", pres

