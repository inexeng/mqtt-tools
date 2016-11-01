#!/bin/sh
# My ThinkSpeak

# Force install
#VERSION=`python -c "import webiopi; print(webiopi.VERSION)"`
#if [ "$VERSION" != "0.5.3" ]; then
#	echo "Update required..."
#	chmod 777 setup.sh
#	sudo ./setup.sh
#

# Start AJ Temps service
# look in  m2m.eclipse.org
# paho/ajtest/tempin   and   paho/ajtest/tempout
cd projects
sudo python /home/pi/projects/pub_temps.py

