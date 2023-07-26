import random
import string

# FUNZIONE GIA' COMPLETA, NON TOCCARE !
def raggi_cosmici(flusso_dati):
    for x in range(random.randint(1,min(3,len(flusso_dati)))):
        i = random.randint(0,len(flusso_dati)-1)
        #print('i',i)
        lista = list(flusso_dati[i])
        for c in range(random.randint(1,3)):
            #print('lista',lista)
            lista[random.randint(0,len(lista)-1)] = random.choice('0123456789$/()')
            #print('flusso_dati[i]=',flusso_dati[i])
            #print('modifico',flusso_dati[i])
            flusso_dati[i] = ''.join(lista)

# IMPORTANTE: dopo un primo round di testing, SCOMMENTA queste istruzioni random.seed
#             per cambiare gli errori casuali introdotti  e verificare
#             che il tuo programma gestisca anche quelle
# NOTA: Il numero del parametro non influisce sul numero o tipo di errori,
# determina solo  quale sequenza di errori viene generata.
# Se non imposti il seed otterrai errori completamente casuali diversi
# ad ogni esecuzione del programma!

random.seed(7)
#random.seed(6)   # scommenta
#random.seed(9)   # scommenta


calendario = [
    '07/11/2020',
    '30/04/2020',
    '02/10/2022',
    '08/11/2023',
    '25/01/2021',
    '29/05/2023',
]

raggi_cosmici(calendario)  # modifica calendario con errori casuali !

print(calendario, "\n")

for i in range(len(calendario)):
    try:
        data = calendario[i].split("/")
        data = [int(data[0]), int(data[1]), int(data[2])]
        if (data[2] <= 2020 and data[2] >= 2023):
            raise Exception(data[2], "non è un anno valido!")
        else:
            if (data[0] > 31):
                raise Exception(data[0],"non è un giorno valido")
            else:
                if (data[1] > 12):
                    raise Exception(data[1], "non è un mese valido")
                else:
                    date = calendario[i]
                    tpl = (date[0],date[1],data[2])
                    print("Riconosciuto!", tpl)
    except ValueError:
        print("La data non è scritta correttamente")
    except Exception as errore:
        print(repr(errore))
