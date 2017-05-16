#!/bin/sh
#launcher.sh

sleep 20
cd /
cd /home/pi/inventor
sudo killall omxplayer.bin
sudo killall python
sleep 10
python disaster.py

