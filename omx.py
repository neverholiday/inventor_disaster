from omxplayer import OMXPlayer
from time import sleep

state1 = 0
state2 = 0
file1 = '/home/pi/video/1.mp4'
file2 = '/home/pi/video/3.mp4'

#state 1
#welcome home 
#-------------------------------------------
#p-Play
#-------------------------------------------

print "Welcome to OMXPlayer na ja"
print "Press p1 or p2 then enter to start"

while(state1 == 0):
	input1 = raw_input("where is p : ")
	if(input1 == 'p1' or input1 == 'p2'):
		state1 = 1
		print "Let start."
	else:
		print "Please try again."

#state 2
#Play video and control video
#p-Play,Pause
#q-Quit
if(input1 == 'p1'):
	player = OMXPlayer(file1)
	sw = '1'
elif(input1 == 'p2'):
	player = OMXPlayer(file2)
	sw = '2'

while(state2==0):
	input2 = raw_input("Play|Pause|Quit|Switch video : ")
	if(input2=='play'):
		player.play()
	elif(input2=='pause'):
		player.pause()
	elif(input2=='q'):
		state2 = 1
		player.quit()
		print "see you again"
	elif(input2 == 'c'):
		now_p = sw
		sw = raw_input("1 or 2 : ")
		if(now_p == sw):
			print 'Now '+now_p+'.mp4 is playing'
			continue
		elif(sw == '1'):
			player.load(file1)
		elif(sw == '2'):
			player.load(file2)

	elif(input2 == 'x'):
		print "Can play ?"
		print player.can_play()
		print "Can pause ?"
		print player.can_pause()
