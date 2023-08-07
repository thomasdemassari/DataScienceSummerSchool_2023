stringa = "Hattori Hanzō è un famoso ninja giapponese del periodo Sengoku"
#stringa = "Ebbe un ruolo chiave nell'unificazione del Giappone."

#Lo faccio normalmente
nuova_lista = list()
nuova_parola = str()
for i in range(len(stringa)):
    if stringa[i] != " ":
        nuova_parola = nuova_parola + stringa[i]
    else:
        nuova_lista.append(nuova_parola)
        nuova_parola = str()
print(nuova_lista)

#Lo faccio con list comprehension
nuova_lista = list()
nuova_parola = str()
nuova_parola = [nuova_parola + stringa[i] for i in range(len(stringa)) if stringa[i] != " "]
print(nuova_parola)
print(nuova_lista)
