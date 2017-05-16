import RPi.GPIO as GPIO
Debug = False
class ButtonAnd4D(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37,GPIO.IN)
        self.relay_use=True
        for i in [7,11,15,16]: # 7:light front 16:light back 15:pump 11:hot wind
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,1)
    
    def hot_wind(self,video,position):
        time_start = {'2':[3],'3':[5],'4':[5],'intro':[1,10]}
        time_duration = {'2':[7],'3':[16],'4':[7],'intro':[5,4]}
        if str(video) in time_start.keys() and str(video) in time_duration.keys():
            time_start = time_start[str(video)]
            time_duration = time_duration[str(video)]
            for index in range(len(time_start)):
                if  position >= time_start[index] and position <= time_start[index]+time_duration[index]:
                    if self.relay_use:
                        GPIO.output(11,0)
                    return True
                else:
                    if self.relay_use:
                        GPIO.output(11,1)
        return False

    def water(self,video,position):
        time_start = {'1':[21],'5':[1,15],'6':[6,10,13,24,26],'7':[1,6,11],'8':[3,8,17],'9':[1,10,19,25],'10':[6,10,13,24,26],'intro':[1]}
        time_duration = {'1':[3],'5':[0.5,7],'6':[1,1,6,1,1],'7':[0.5,0.5,2],'8':[0.5,4,2],'9':[1,1,1,3],'10':[1,1,6,1,1],'intro':[2]}
        if str(video) in time_start.keys() and str(video) in time_duration.keys():
            time_start = time_start[str(video)]
            time_duration = time_duration[str(video)]
            for index in range(len(time_start)):
                if  position >= time_start[index] and position <= time_start[index]+time_duration[index]:
                    if self.relay_use:
                        GPIO.output(15,0)
                    return True
                else:
                    if self.relay_use:
                        GPIO.output(15,1)
        return False

    def light_front(self,video,position):
        time_start = {'1':[13,22],'5':[14],'intro':[1]}
        time_duration = {'1':[3,2],'5':[3],'intro':[10]}
        if str(video) in time_start.keys() and str(video) in time_duration.keys():
            time_start = time_start[str(video)]
            time_duration = time_duration[str(video)]
            for index in range(len(time_start)):
                if  position >= time_start[index] and position <= time_start[index]+time_duration[index]:
                    if self.relay_use:
                        GPIO.output(7,0)
                    return True
                else:
                    if self.relay_use:
                        GPIO.output(7,1)
        return False

    def light_back(self,video,position):
        time_start = {'1':[13,21,22],'2':[19],'4':[3,10],'5':[1,9,14],'6':[18],'7':[6],'8':[1],'9':[1,6,18],'10':[18],'intro':[1]}
        time_duration = {'1':[3,3,2],'2':[2],'4':[2,3],'5':[3,7,3],'6':[12],'7':[6],'8':[18],'9':[3,4,10],'10':[12],'intro':[10]}
        if str(video) in time_start.keys() and str(video) in time_duration.keys():
            time_start = time_start[str(video)]
            time_duration = time_duration[str(video)]
            for index in range(len(time_start)):
                if  position >= time_start[index] and position <= time_start[index]+time_duration[index]:
                    if self.relay_use:
                        GPIO.output(16,0)
                    #print str(position) + ' : ' + str(time_start[index]) + ' : on'
                    return True

                else:
                    if self.relay_use:
                        GPIO.output(16,1)
                    #print str(position) + ' : ' + str(time_start[index]) + ' : off'
        return False

    def play_4d(self,video,position):
        temp='none'
        if self.hot_wind(video,position):
            temp='hot wind '
        if self.water(video,position):
            if temp == 'none':
                temp='water '
            else:
                temp+=': water '
        if self.light_front(video,position):
            if temp == 'none':
                temp='light front '
            else:
                temp+=': light front '
        if self.light_back(video,position):
            if temp == 'none':
                temp='light back'
            else:
                temp+=': light back'
        if Debug is True:
            print temp
    
    def get_button(self):
        return GPIO.input(37)

    def clean(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        for i in [7,11,15,16]: # 7:light front 16:light back 15:pump 11:hot wind
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,1)
        
