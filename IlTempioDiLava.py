d = 80

x,y = 0, 0     # False
x,y = 20, 20  # False
x,y = 60, 10  # True
x,y = 10, 60  # True
x,y = 20, 70  # False
x,y = 70, 20  # False
x,y = 70, 70  # False
x,y = 0,60    # True
x,y = 60,0    # True

print(((x > d/2) and (y < -x + d)) or ((x < d/2) and (y <= -x + d) and (y > d/2)))

print((y < -x + d) and not ((x < d/2) and (y < d/2)))
