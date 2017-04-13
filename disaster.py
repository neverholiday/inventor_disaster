from omxplayer import OMXPlayer

# this script artn't tested yet, wait for real video complete
# Ya pung run na heyyyyyyyyyyyyyyyyyyyyy

# state 1 play video from rfid card
# contol seeker na ja 
# 16 positions 
# every position has 30 second
# repeat 1:0-30 2:31-60 3:60-90 4:90-120 5:120-150 6:150-180
# repeat 7:180-210 8:210-240 9:240-270 10:270-300 11:300-330 12:330-360

state1 = 0
state2 = 0
pos = 0
t_pos = pos
list_pos = [30,60,90,120,150,180,210,240,270,300,330,360] # change dai na
player = OMXPlayer('/home/pi/video/rfid_video.mp4') 

while(state1 == 0):
	pos = raw_input('input : ') # this line will be replaced by rfid  
	pos = int(pos)
	if(t_pos != pos):
		player.set_position(list_pos[pos]-10)
		t_pos = pos
	if(pos == 12): # press button to play end state
		state1 = 1
	if(player.position()>list_pos[pos]):
		player.set_position(list_pos[pos]-20)
	
# state 2 when player press the button disaster is coming. 
# 12 disastors are real , 4 are fake and they didn't show anything

rfid_result = 1 # function return from rfid
disaster_video = '/home/pi/video/'+rfid_result+'.mp4'

player.load(disaster_video)

# repeat to state 1 again when video have ended
