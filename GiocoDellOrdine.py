giocatore1 = ["h", "b", "f", "a", "x"]
giocatore2 = ["e", "c", "g", "d", "z"]

import copy
ggiocatore1 = giocatore1[:]
ggiocatore2 = giocatore2[:]


i = 0
for i in range(5):
    giocatore1[i] = giocatore1[i] + "_1"
    giocatore2[i] = giocatore2[i] + "_2"

giocata = list(giocatore1 + giocatore2)
giocata.sort()
giocata.reverse()
print("L'ordine delle giocate è:", giocata)

j = 0
punti1 = list()
punti2 = list()

for j in range(len(ggiocatore1)):
    punto1 = ord(ggiocatore1[j])
    punto2 = ord(ggiocatore2[j])
    punti1.append(punto1)
    punti2.append(punto2)
    j = j+1

if sum(punti1) == sum(punti2):
    print("I giocatori hanno pareggiato")
else:
    if sum(punti1) > sum(punti2):
        print("Ha vinto il giocatore 1")
    else: 
        print("Ha vinto il giocatore 2")
