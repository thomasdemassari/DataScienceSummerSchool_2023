import math

studenti = ['M_Alessandro', 'F_Alessia', 'F_Alice', 'M_Andrea', 'F_Anna', 'F_Arianna', 'F_Aurora',
            'F_Beatrice', 'F_Bianca', 'F_Camilla', 'F_Chiara', 'M_Federico', 'M_Francesco', 'M_Gabriele',
            'F_Gaia', 'F_Ginevra', 'F_Giorgia', 'F_Giulia', 'M_Giuseppe', 'F_Greta', 'M_Leonardo', 'M_Lorenzo',
            'F_Ludovica', 'M_Matteo', 'M_Mattia', 'M_Merlino','F_Nicole', 'M_Nicolo', 'F_Noemi', 'M_Riccardo',
            'F_Sara', 'F_Sofia', 'M_Tommaso', 'F_Vittoria']

#studenti = ['M_Alessandro', 'F_Alessia', 'F_Alice', 'M_Andrea', 'F_Anna', 'F_Arianna', 'F_Aurora',
            #'F_Beatrice', 'F_Bianca', 'F_Camilla', 'F_Chiara', 'M_Federico', 'M_Francesco', 'M_Gabriele',
            #'F_Gaia', 'F_Ginevra', 'F_Giorgia']

#Per maschi: stanze da 3
#Per femmine: stanze da 3
#Persone assegnate in base a ordine alfabetico

persone_stanzaM = 3
persone_stanzaF = 3

#Divido i maschi dalle femmine
maschi = list()
maschi_ = list()
femmine = list()
femmine_ = list()
#Uso metodo startswith. Se inzia con M, metto in maschi, altrimenti in femmine. Cico per tutta la lista studenti
i = 0
for i in range(len(studenti)):
    if studenti[i].startswith("M"):
        studente_maschio = studenti[i] 
        maschi_.append(studente_maschio) #aggiungo alla lista con M_
        studente_maschio = studente_maschio.replace("M_","") #tolgo il sesso
        maschi.append(studente_maschio) #aggiungo ala lista senza M_
    else:
        studente_femmina = studenti[i]
        femmine_.append(studente_femmina) #aggiungo alla lista con F_
        studente_femmina = studente_femmina.replace("F_","") #tolgo il sesso
        femmine.append(studente_femmina) #aggiungo alla lista senza F_
    i = i + 1

#Ordine alfabetico
maschi.sort()
femmine.sort()

#Controllo dei risultati del ciclo for e stampa dei risultati
if ((("F_" or "M_") in maschi) or (("F_" or "M_")  in femmine) or len(studenti) != (len(maschi) + len(femmine)) or ("M_" in femmine_) or ("F_" in maschi_)):
    print("Attenzione! La suddivisione maschi-femmine non è avvenuta correttamente")
else:
    print("La suddivisione maschi-femmine è avvenuta correttamente\n")
    print("1.a)\t maschi con _ =", maschi_, "\n\t femmine con _ =", femmine_, "\n")
    print("1.b)\t maschi =", maschi, "\n\t femmine =", femmine, "\n")

#Calcolo del numero delle stanze
if len(maschi) % persone_stanzaM == 0: 
    nstanza_m = len(maschi) // persone_stanzaM
else:
    nstanza_m = (len(maschi) // persone_stanzaM) + 1
    if math.isclose(len(maschi) % persone_stanzaM, 1/persone_stanzaM): #questo if mi serve per avere sempre la stessa lunghezza delle camere. Se c'è una camera da 1 metti due spazi, se la camera è da 2 metti uno spazio
        maschi.append("")
        maschi.append("")
    else:
        maschi.append("")

if len(femmine) % persone_stanzaF == 0:
    nstanza_f = len(femmine) // persone_stanzaF
else:
    nstanza_f = (len(femmine) // persone_stanzaF) + 1
    if math.isclose(len(femmine) % 3, 1/persone_stanzaF): 
        femmine.append("")
        femmine.append("")
    else:
        femmine.append("")


#Scrivo da chi sono composte le stanze 
#Salvo per sicurezza la lista di studenti divisi per sesso
maschi_backup = maschi[:]
femmine_backup = femmine[:]

i_stanza_m = 1 #numero della stanza analizzata
for i in range(nstanza_m):
    instanza_maschi = maschi[0] + " " + maschi[1] + " " + maschi[2] #chi c'è in stanza
    print("Stanza maschi", i_stanza_m , ":", instanza_maschi) 
    i_stanza_m = i_stanza_m + 1 
    maschi = maschi[3:] #tolgo i primi tre ragazzi che ho già messo nella stanza
print("\n")
i_stanza_f = 1
for j in range(nstanza_f):
    instanza_femmine = femmine[0] + " " + femmine[1] + " " + femmine[2]
    print("Stanza femmine", i_stanza_f , ":", instanza_femmine)
    i_stanza_f = i_stanza_f + 1
    femmine = femmine[3:]
