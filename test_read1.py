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
MIFAREReader1 = MFRC522.MFRC522()


# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status1,TagType1) = MIFAREReader1.MFRC522_Request(MIFAREReader1.PICC_REQIDL)


    
    # Get the UID of the card
    (status1,uid1) = MIFAREReader1.MFRC522_Anticoll()

    # If we have the UID, continue
    if status1 == MIFAREReader1.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid1[0])+","+str(uid1[1])+","+str(uid1[2])+","+str(uid1[3])

