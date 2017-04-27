import RPi.GPIO as GPIO

class ButtonAnd4D(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37,GPIO.IN)
        self.relay_use=True
        for i in [7,11,15,16]: # 7:light front 16:light back 15:pump 11:hot wind
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,1)
    
    def hot_wind(self,video,position):
        time_start = {'1':[2,]}
        time_duration = {'1':[12]}
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
        time_start = {'1':[1,5,8]}
        time_duration = {'1':[2,1,2]}
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
        time_start = {'1':[3,8]}
        time_duration = {'1':[3,2]}
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
        time_start = {'1':[1]}
        time_duration = {'1':[5]}
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
        if self.hot_wind(1,position):
            temp='hot wind '
        if self.water(1,position):
            if temp == 'none':
                temp='water '
            else:
                temp+=': water '
        if self.light_front(1,position):
            if temp == 'none':
                temp='light front '
            else:
                temp+=': light front '
        if self.light_back(1,position):
            if temp == 'none':
                temp='light back'
            else:
                temp+=': light back'
        print temp
    
    def get_button(self):
        return GPIO.input(37)

    def clean(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        for i in [7,11,15,16]: # 7:light front 16:light back 15:pump 11:hot wind
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,1)
        
