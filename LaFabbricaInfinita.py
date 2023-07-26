import math

m = 10

x,y = 2.5 * m, 0.5 * m       # True
#x,y = 2.5 * m, 1.5 * m      # False
#x,y = 0.5 * m, 0.5 * m      # False
#x,y = 5.5 * m, 0.5 * m      # True
#x,y = 5.5 * m, 2.5 * m      # True
#x,y =  7.0 * m, 4.5 * m     # False
#x,y = 5.5 * m, 2.5 * m      # True
#x,y = 299.5 * m, 200.5 * m  # True
#x,y = 300.5 * m, 200.5 * m  # False

(math.ceil(x/m) % 3 == 0) and (int(y/m) % 2 == 0)
