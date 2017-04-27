from time import sleep
import MFRC522

class Rfid(object):
	"""docstring for Rfid"""
	# dict_rfid = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0} ---> rfid_show 
	# disaster : 1 fire 2 earthquake 3 storm 4 tsunami
	# place : 5 city 6 forest 7 shore 8 dessert

	def __init__(self):	
		self.uid_for_set_card = [0,0,0,0]
		self.uid1 = [0,0,0,0]
		self.uid2 = [0,0,0,0]
		self.disaster = {'fire':0,'earth':0,'storm':0,'tsunami':0}
		self.place = {'city':0,'forest':0,'shore':0,'desert':0}
		self.txt = ''
		self.disaster_default = 'fire'
		self.place_default = 'city'
		self.tkey1 = None
		self.tkey2 = None



	def set_card(self):

                state_set_card = 0

		temp = self.disaster.keys() + self.place.keys()

		for i in range(len(temp)):
                        print 'input '+temp[i]+ ' card'
                        while state_set_card == 0:
                                MIFAREReader1 = MFRC522.MFRC522(dev='/dev/spidev0.0')
                                (status1,TagType1) = MIFAREReader1.MFRC522_Request(MIFAREReader1.PICC_REQIDL)
                                (status1,self.uid_for_set_card) = MIFAREReader1.MFRC522_Anticoll()
                                if status1 == MIFAREReader1.MI_OK:
                                        print "Card1 read UID: "+str(self.uid_for_set_card[0])+","+str(self.uid_for_set_card[1])+","+str(self.uid_for_set_card[2])+","+str(self.uid_for_set_card[3])
                                        keyboard = str(self.uid_for_set_card[0]) + str(self.uid_for_set_card[1]) + str(self.uid_for_set_card[2]) + str(self.uid_for_set_card[3])
                                        state_set_card = 1
                                del MIFAREReader1
			
			self.txt = self.txt + keyboard
			self.txt = self.txt + '/'
			print 'wait a second , please move your card out!'
			sleep(1)
			state_set_card = 0
		self.write_file()
	
	def write_file(self):
		file = open('rfid.txt','wb')
		file.write(self.txt)
		file.close()

	def disaster_place(self):
		file = open('rfid.txt','r')
		tsum = ''
		tstr = ''
		for i in self.disaster.keys():
			while tstr != '/':
				tstr = file.read(1)
				tsum = tsum + tstr
			tsum = tsum.replace('/','') 
			self.disaster[i] = tsum
			tsum = '' # clear str
			tstr = ''
		tsum = ''
		for i in self.place.keys():
			while tstr != '/':
				tstr = file.read(1)
				tsum = tsum + tstr
			tsum = tsum.replace('/','')
			self.place[i] = tsum				
			tsum = '' # clear str
			tstr = ''
		tsum = ''
		tstr = ''
		file.close()
		self.disaster = dict((v,k) for k,v in self.disaster.iteritems())
		self.place = dict((v,k) for k,v in self.place.iteritems())

	def interface_rfid(self):

                MIFAREReader1 = MFRC522.MFRC522(dev='/dev/spidev0.0')

                (status1,TagType1) = MIFAREReader1.MFRC522_Request(MIFAREReader1.PICC_REQIDL)

                (status1,self.uid1) = MIFAREReader1.MFRC522_Anticoll()

                if status1 == MIFAREReader1.MI_OK:

                        #print "Card1 read UID: "+str(self.uid1[0])+","+str(self.uid1[1])+","+str(self.uid1[2])+","+str(self.uid1[3])
                        self.tkey1 = str(self.uid1[0]) + str(self.uid1[1]) + str(self.uid1[2]) + str(self.uid1[3])
                else :
                        self.tkey1 = None
                        
                del MIFAREReader1
                    
                MIFAREReader2 = MFRC522.MFRC522(dev='/dev/spidev1.2')

                (status2,TagType2) = MIFAREReader2.MFRC522_Request(MIFAREReader2.PICC_REQIDL)
                
                (status2,self.uid2) = MIFAREReader2.MFRC522_Anticoll()

                if status2 == MIFAREReader2.MI_OK:
                        #print "Card2 read UID: "+str(self.uid2[0])+","+str(self.uid2[1])+","+str(self.uid2[2])+","+str(self.uid2[3])
                        self.tkey2 = str(self.uid2[0]) + str(self.uid2[1]) + str(self.uid2[2]) + str(self.uid2[3])

                else :
                        self.tkey2 = None

                del MIFAREReader2

                if self.tkey1 not in self.disaster.keys(): 
			self.tkey1 = None
		if self.tkey2 not in self.place.keys():
			self.tkey2 = None
				
                if self.tkey1 is None and self.tkey2 is not None:
                        self.disaster_default = None
                        self.place_default = self.place[self.tkey2]
                elif self.tkey2 is None and self.tkey1 is not None:
                        self.disaster_default = self.disaster[self.tkey1]
                        self.place_default = None
                elif self.tkey2 is None and self.tkey1 is None:
                        self.disaster_default = None
                        self.place_default = None
                elif self.tkey1 is not None or self.tkey2 is not None:
                        self.disaster_default = self.disaster[self.tkey1]
                        self.place_default = self.place[self.tkey2]
                        
                print str(self.disaster_default) + '||' + str(self.place_default)
		

		if self.disaster_default is None and self.place_default is None:
			return 0
		elif self.disaster_default is 'fire' and self.place_default is None:
			return 1
		elif self.disaster_default is 'tsunami' and self.place_default is None:
			return 2
		elif self.disaster_default is 'storm' and self.place_default is None:
			return 3
		elif self.disaster_default is 'earth' and self.place_default is None:
			return 4
		elif self.disaster_default is None and self.place_default is 'city':
			return 5
		elif self.disaster_default is None and self.place_default is 'shore':
			return 6
		elif self.disaster_default is None and self.place_default is 'forest':
			return 7
		elif self.disaster_default is None and self.place_default is 'desert':
			return 8
		elif self.disaster_default is 'fire' and self.place_default is 'city':
			return 9
		elif self.disaster_default is 'fire' and self.place_default is 'shore':
			return 10
		elif self.disaster_default is 'fire' and self.place_default is 'forest':
			return 11
		elif self.disaster_default is 'fire' and self.place_default is 'desert':
			return 12
		elif self.disaster_default is 'tsunami' and self.place_default is 'city':
			return 13
		elif self.disaster_default is 'tsunami' and self.place_default is 'shore':
			return 14
		elif self.disaster_default is 'tsunami' and self.place_default is 'forest':
			return 15
		elif self.disaster_default is 'tsunami' and self.place_default is 'desert':
			return 16
		elif self.disaster_default is 'storm' and self.place_default is 'city':
			return 17
		elif self.disaster_default is 'storm' and self.place_default is 'shore':
			return 18
		elif self.disaster_default is 'storm' and self.place_default is 'forest':
			return 19
		elif self.disaster_default is 'storm' and self.place_default is 'desert':
			return 20
		elif self.disaster_default is 'earth' and self.place_default is 'city':
			return 21
		elif self.disaster_default is 'earth' and self.place_default is 'shore':
			return 22
		elif self.disaster_default is 'earth' and self.place_default is 'forest':
			return 23
		elif self.disaster_default is 'earth' and self.place_default is 'desert':
			return 24
	
	def check_video(self,result):
		if result == 11: # fire forest
                        return 3
                elif result == 13: # tsunami city
                        return 6 
                elif result == 17: # storm city
                        return 1
                elif result == 18: # storm coast
                        return 7
                elif result == 19: # storm forest
                        return 5
                elif result == 20: # storm desert
                        return 4
                elif result == 21: # eq city
                        return 2
                elif result == 22: # eq shore
                        return 6
                else:
                        return 0
		 
'''
a = Rfid()
a.disaster_place()
while True:
        b = a.interface_rfid()
        print b
'''
