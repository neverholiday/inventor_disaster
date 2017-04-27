from omxplayer import OMXPlayer
from rfid import Rfid
#import RPi.GPIO as GPIO
from button_and_4d import ButtonAnd4D
import time

video_playing = False
pos = 0
t_pos = pos
list_pos = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250] # change dai na

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(37,GPIO.IN)

                
rfid_read = Rfid()
rfid_read.disaster_place()
player = OMXPlayer('/home/pi/video/real/clect.mp4',['-o','local','--no-osd'])
#player = OMXPlayer('/home/pi/video/real/clect.mp4')
time.sleep(1)
try:
        while True:
                effect=ButtonAnd4D()
                #print effect.get_button()
                while video_playing == False:
                        #pos = raw_input('input di : ') # this line will be replaced by rfid  
                        pos = rfid_read.interface_rfid()
                        #print pos

                        if(t_pos != pos):
                                player.set_position(list_pos[pos]-8)
                                t_pos = pos
                        if(player.position()>list_pos[pos]-1):
                                player.set_position(list_pos[pos]-8)
                        if effect.get_button() == 1:
                                if list_pos[pos] <= 90: 
                                        print 'insert card'
                                else:
                                        print 'finally :' + str(pos)
                                        clip = rfid_read.check_video(pos)
                                        if clip != 0:
                                                video_playing = True
                                                player.load('/home/pi/video/real/'+str(clip)+'.mp4')
                time.sleep(2)

                
                while player.position() < player.duration()-0.5:
                #while player.is_playing():
                        #effect.play_4d(1,player.position())
                        if effect.get_button() == 1:
                                break
                player.quit()
                del player
                video_playing = False
                player = OMXPlayer('/home/pi/video/real/clect.mp4',['-o','local','--no-osd'])
                #player.load('/home/pi/video/real/clect.mp4')
                time.sleep(2)
                pos = 0
                t_pos = -1
                
except KeyboardInterrupt:
        player.quit()
        effect.clean()
# state 2 when player press the button disaster is coming. 
# 12 disastors are real , 4 are fake and they didn't show anything
'''
rfid_result = 1 # function return from rfid
disaster_video = '/home/pi/video/'+rfid_result+'.mp4'

player.load(disaster_video)

# repeat to state 1 again when video have ended
'''
