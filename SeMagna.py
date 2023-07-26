panini, burgers = 3, 5   # Servito bla bla... alla fine stampa 'Avanzano 2 burger.'
# panini, burgers = 9,3   # Servito bla bla... alla fine stampa 'Avanzano 6 panini.'
panini, burgers = 4,4   # Servito bla bla... alla fine stampa 'credenza vuota!'

hambuger = 0

if(panini < 1) and (burgers < 1):
    raise Exception("Non hai burgers e non hai neanche abbastanza panini")
else:
    if(panini < 1):
        raise Exception("Non hai abbastanza panini")
    else:
        if(burgers < 1):
            raise Exception("Non hai abbastanza burgers")
        else:
            while (panini > 0 and burgers > 0):
                if (panini > 0) and (burgers > 0):
                    hambuger = hambuger + 1 
                    panini = panini - 1
                    burgers = burgers - 1
                    print("Servito un hambuger:", panini, "panini rimanenti,", burgers, "burger rimanenti")
               
print("Avanzano", panini, "panini e", burgers, "burger. Sono stati prodotti", hambuger, "hamburger")

if (panini + burgers == 0):
    print("Hai la credenza vuota")
