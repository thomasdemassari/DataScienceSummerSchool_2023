import math

n = 20    # False
n = 405  # False
n = 70   # False
n = 100  # True
n = 460  # True
n = 225  # True
n = 182  # False
n = 253  # False
n = 275  # False
n = 205  # False
n = 350  # True
n = 925  # False
n = 815  # True
n = 92   # True

c = math.ceil(n/30)
c = c + (c == 3) + (c == 7) + (c == 11)
(math.ceil(c) % 4 == 0) or (math.ceil(c) % 8 == 0) or (math.ceil(c) % 12 == 0) 

#Soluzione breve
#Devo assumere che il valore estremo non è compreso
print(n % 120 > 90)
