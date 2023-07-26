import math

r = 5.0

x,y = 0,0    #  0.0
x,y = 0,3    #  3.0
x,y = -4,0   #  4.0
x,y = 3,-3   #  4.242640687119285
x,y = 3,4    #  5.0
#x,y = 4,-3   #  5.0
#x,y = -4,3   #  5.0
#x,y = 6,0    #  4.0
#x,y = 0,7    #  3.0
#x,y = 0,-8   #  2.0
#x,y = 10,0   #  0.0
#x,y = -6,7   #  0.7804555427071129
x,y = -7,9   #  0.0  

distanza = math.sqrt((x**2)+(y**2))


print(abs((distanza - (distanza > r) * (r*2)) * (distanza < r*2))) #fatto da me con abs per tutta l'operazione
print(abs(distanza - (distanza > r) * (r*2)) * (distanza < r*2)) #fatto da Leonardo con abs solo per i primi tre termini, (distanza < r*2) escluso da abs
