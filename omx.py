from omxplayer import OMXPlayer
from time import sleep

state1 = 0
state2 = 0
file_path_or_url = '/home/pi/Downloads/test.mp4'

#state 1
#welcome home 
#-------------------------------------------
#p-Play
#-------------------------------------------

print "Welcome to OMXPlayer na ja"
print "Press p and enter to start"

while(state1 == 0):
	input1 = raw_input("where is p : ")
	if(input1 == 'p'):
		state1 = 1
		print "Let start."
	else:
		print "Please try again."

#state 2
#Play video and control video
#p-Play,Pause
#q-Quit

player = OMXPlayer(file_path_or_url)

while(state2==0):
	input2 = raw_input("Play|Pause|Quit : ")
	if(input2=='p'):
		player.play_pause()
	elif(input2=='q'):
		state2 = 1
		player.quit()


print "see you again"
