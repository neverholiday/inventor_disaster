#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
from time import sleep

continue_reading = True


uid1 = [0,0,0,0]
uid2 = [0,0,0,0]

# Create an object of the class MFRC522

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."
io = '0'
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
try:
    while True:


        #if io == '0':
            #io = raw_input('Enter reader card : ')
        
        #elif io == '1':
        MIFAREReader1 = MFRC522.MFRC522(dev='/dev/spidev0.0')

        (status1,TagType1) = MIFAREReader1.MFRC522_Request(MIFAREReader1.PICC_REQIDL)

        (status1,uid1) = MIFAREReader1.MFRC522_Anticoll()

        if status1 == MIFAREReader1.MI_OK:

            print "Card1 read UID: "+str(uid1[0])+","+str(uid1[1])+","+str(uid1[2])+","+str(uid1[3])
            #print "Card2 read UID: "+str(uid2[0])+","+str(uid2[1])+","+str(uid2[2])+","+str(uid2[3])

                #io = '0'

        del MIFAREReader1

        #elif io == '2':
        sleep(2)
            
        MIFAREReader2 = MFRC522.MFRC522(dev='/dev/spidev1.2')

        (status2,TagType2) = MIFAREReader2.MFRC522_Request(MIFAREReader2.PICC_REQIDL)
            
        
        # Get the UID of the card
        
        (status2,uid2) = MIFAREReader2.MFRC522_Anticoll()

        if status2 == MIFAREReader2.MI_OK:


            #print "Card1 read UID: "+str(uid1[0])+","+str(uid1[1])+","+str(uid1[2])+","+str(uid1[3])
            print "Card2 read UID: "+str(uid2[0])+","+str(uid2[1])+","+str(uid2[2])+","+str(uid2[3])

               # io = '0'
        del MIFAREReader2

except KeyboardInterrupt:

    print "Ctrl+C captured, ending read."
    GPIO.cleanup()
            
        # This is the default key for authentication
