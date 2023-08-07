import csv

costo_unitario = 100  # euro

def terme(nome_file):
    with open(nome_file, encoding = "utf-8", newline = "") as file:
        lettore = csv.reader(file, delimiter = ",")
        diz = dict()
        next(lettore) #Faccio next per ignorare la prima riga
        # contatore = 0 
        for riga in lettore:
            tmp = (riga.count('1'))*costo_unitario
            diz[riga[0]] = tmp 

            #modo artigianale per togliere riga 0
            # if contatore == 0:
            #     del diz[riga[0]]
            # contatore += 1
    return diz

res1 = terme('/Users/thomasdemassari/Cache/formats/centro-benessere1.csv')
print(res1)
assert res1 == { 'Marco':    400,
                 'Andrea':   300,
                 'Sara':     600,
                 'Rosa':     200,
                 'Cristina': 300,
                 'Roberto':  100}

res2 = terme('/Users/thomasdemassari/Cache/formats/centro-benessere2.csv')
print(res2)
assert res2 == { 'Giulio': 300,
                 'Sabina': 100 }

