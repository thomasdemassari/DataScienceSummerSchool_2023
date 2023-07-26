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
