#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader2 = MFRC522.MFRC522(dev='/dev/spidev1.2')

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status2,TagType2) = MIFAREReader2.MFRC522_Request(MIFAREReader2.PICC_REQIDL)
    # If a card is found

    
    # Get the UID of the card
    (status2,uid2) = MIFAREReader2.MFRC522_Anticoll()

    # If we have the UID, continue
    if status2 == MIFAREReader2.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid2[0])+","+str(uid2[1])+","+str(uid2[2])+","+str(uid2[3])
    
        # This is the default key for authentication
