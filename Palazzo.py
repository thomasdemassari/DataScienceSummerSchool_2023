parola = 'palazzo'
#parola = "ciao come stai?"

lettere = list(parola)

i = 0
for i in range(len(lettere)):
    print(i, lettere[i].lower(), lettere[i].upper())
    i = i + 1
