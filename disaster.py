from time import sleep,time
from omxplayer import OMXPlayer
from rfid import Rfid
from button_and_4d import ButtonAnd4D
import pygame

Debug = False
pygame.mixer.init()
pygame.mixer.music.load('/home/pi/Wrong-buzzer.mp3') 
video_playing = False
time_start=0
pos = 0
t_pos = pos
list_pos = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250] # change dai na
    
rfid_read = Rfid()
rfid_read.disaster_place()
player = OMXPlayer('/home/pi/video/real/clect.mp4',['-o','local','--no-osd'])

sleep(1)
try:
        while True:
                effect=ButtonAnd4D()
                while video_playing == False:
                        pos = rfid_read.interface_rfid()
                        if(t_pos != pos):
                                player.set_position(list_pos[pos]-8)
                                t_pos = pos
                                time_start=time()
                        if(player.position()>list_pos[pos]-1):
                                player.set_position(list_pos[pos]-8)
                        if effect.get_button() == 1:
                                time_start=time()
                                if list_pos[pos] <= 90: 
                                        pygame.mixer.music. play()
                                else:
                                        if Debug is True:
                                                print 'finally :' + str(pos)
                                        clip = rfid_read.check_video(pos)
                                        video_playing = True
                                        player.load('/home/pi/video/real/'+str(clip)+'.mp4')
                        elif time()-time_start >= 900 or time_start == 0:
                                player.load('/home/pi/intro.mp4')
                                clip = 'intro'
                                video_playing = True
                sleep(2)

                # show video disaster
                while player.position() < player.duration()-0.5 and clip!=0:
                        effect.play_4d(clip,player.position())
                        if clip == 'intro':
                                pos = rfid_read.interface_rfid() 
                        if effect.get_button() == 1 or t_pos != pos:
                                break
                time_start=time()
                if clip==0:
                        sleep(4)
                effect.clean()
                player.quit()
                del player
                video_playing = False
                player = OMXPlayer('/home/pi/video/real/clect.mp4',['-o','local','--no-osd'])
                sleep(2)
                pos = 0
                t_pos = -1
                
except KeyboardInterrupt:
        player.quit()
        effect.clean()

'''
rfid_result = 1 # function return from rfid
disaster_video = '/home/pi/video/'+rfid_result+'.mp4'
s
player.load(disaster_video)

# repeat to state 1 again when video have ended
'''
