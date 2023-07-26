monte = [90,40,50,20,60, 7, 3, 4, 9, 8]   # [20, 40, 50, 60, 90, 9, 8, 7, 4, 3]
monte = [5,0,3,4,3,8]                    # [0, 3, 5, 8, 4, 3]
monte = []                               # []
monte = [7,3]                            # [7,3]

import copy
copia = copy.deepcopy(monte)
lun = len(copia)
n = int(len(monte)/2)
copia_pt1 = copia[:n]
copia_pt1.sort()
copia_pt2 = copia[n:]
copia_pt2.sort()
copia_pt2.reverse()

monte.extend(copia_pt1)
monte.extend(copia_pt2)

i = 0
for i in range(lun):
    occorrenza = copia[i]
    index = monte.index(occorrenza)
    monte.pop(index)
    i = i + 1

print(monte)
