#Modifica il programma di prima in Python  per riportare lo stato delle varie azioni compiute. Elenchiamo qui i possibili casi e i risultati attesi:

fatto_colazione, lavato_denti = False,False

if fatto_colazione and lavato_denti:
    print("Ho fatto colazione \nho lavato i denti \nfatto tutto! \nposso uscire di casa!")
else:
    if (fatto_colazione == False) and (lavato_denti == True):
        print("Non ho fatto colazione, ma ho lavato i denti \nNON posso uscire di casa")
    else:
        if (fatto_colazione == True) and (lavato_denti == False):
            print("Ho fatto colazione, ma non ho lavato i denti \bNON posso uscire di casa")
        else:
            if (fatto_colazione == False) and (lavato_denti == False):
                print("Non ho fatto colazione e non ho lavato i denti \nNON posso uscire di casa")
            else:
                print("Condizione non gestita")

#Prova a fare un programma in Python che ti dice se puoi uscire di casa solo se hai fatto colazione (per cui devi avere almeno un tipo di latte) e lavato i denti
ho_latte_intero = False
ho_latte_scremato = False
lavato_denti = False
fatto_colazione = (ho_latte_intero) or (ho_latte_scremato)

if (fatto_colazione == True) and (lavato_denti == True):
        print("Hai fatto colazione e hai lavato i denti. \nPuoi uscire di casa")
else:
    if (fatto_colazione == True) and (lavato_denti == False):
        print("Hai fatto colazione, ma non ti sei lavato i denti. \nNon puoi uscire di casa")
    else:
        if (lavato_denti == True) and (fatto_colazione == False):
            print("Non hai fatto colazione perchè non hai il latte, ma hai lavato i denti. \nNon puoi uscire di casa")
        else:
             print("Non hai fatto colazione perchè non hai il latte e non ti sei neanche lavato i denti. \nLavati i denti e vai a comprare il latte")
