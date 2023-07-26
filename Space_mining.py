import math

d = 30

x,y = 0, 0      # 3
x,y = 2, 2      # 3
x,y = -2, -2    # 3
x,y = 7, 0      # 2
x,y = -7, 0     # 2
x,y = 0, 8      # 2 
x,y = -12, 0    # 2
x,y = 2, 13     # 2 
x,y = 13, 13    # 1
x,y = 14, -12   # 1
x,y = -11, -13  # 1
x,y = -10, 11   # 1

(((x < -d/6) or (x > d/6)) or ((x > -d/6) and (x < d/6))) + (((y < d/6) and (y > -d/6)) or (x > -d/6 and x < d/6)) + (((y < d/6) and (y > -d/6)) and ((x > -d/6) and (x < d/6)))
