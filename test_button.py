import RPi.GPIO as G

G.setmode(G.BOARD)

# 7light 16light 11fan hot 15pump
a = [7,11,16,15]

for i in a:
	G.setup(i,G.OUT)
        G.output(i,1)

G.setup(37,G.IN)

b = [11]

while True:

        if G.input(37) == 1:
                for i in b:	
                        
                        G.output(i,0)	
        else:
                for i in b:
                        G.output(i,1)

