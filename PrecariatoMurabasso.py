lavori = [
    ["Straordinari in fonderia", 175.13, "non pagato"],
    ["Part time gelateria",      450, "non pagato"],
    ["Rendita investimenti",     500, "pagato"],
    ["Pettinatura pitoni",       1000, "pagato"],
    ["Installazione artistica",  600, "non pagato"],
    ["Noleggio scarpe eleganti", 100, "non pagato"]
]

pagato = "pagato"
non_pagato = "non pagato"

lavori_pagati = list()
cifre_pagate = list()
lavori_nonpagati = list()
cifre_nonpagate = list()

for i in range(len(lavori)):
    if lavori[i][2] == pagato:
        lavori_pagati.append(lavori[i][0])
        cifre_pagate.append(float(lavori[i][1]))
    else:
        lavori_nonpagati.append(lavori[i][0])
        cifre_nonpagate.append(lavori[i][1])


cassa = sum(cifre_pagate)
crediti = sum(cifre_nonpagate)
print("Totale ricevuto:", cassa, "\nTotale da ricevere:", crediti)

massimo = max(cifre_pagate)
indice = cifre_pagate.index(massimo)
print("Il lavoro più pagato finora è:", lavori_pagati[indice])
