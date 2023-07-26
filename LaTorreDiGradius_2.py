import math

n,m = 160,170   # True
n,m = 135, 140 # False
n,m = 160,190  # False
n,m = 70,170   # False
n,m = 350,260  # False
n,m = 350,340  # True
n,m = 350,340  # True
n,m = 430,530  # False
n,m = 520,510  # True
n,m = 730,740  # False


#((n % 90) > 60) and ((m % 90) > 60)
#Così non so se sono enbrambe sullo stesso spicchio
#Il modulo 4 deriva dal fatto che gli spicchi gialli sono 4
((n % 90) > 60) and ((m % 90) > 60) and ((n // 90) % 4 == (m // 90) % 4)
