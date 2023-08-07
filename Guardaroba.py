indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
capi = [9,5,7,3]

#Metodo 1, non va bene
lista1 = [str("ci sono " + str(capi[i]) + " " + str(indumenti [i])) for i in range(len(indumenti))]
print(lista)

#Metodo 2, non va bene
indice = indumenti.index(indumenti[-1])
i = 0
lista_while = list()
while i <= indice:
    lista_while.append(str("ci sono " + str(capi[i]) + " " + str(indumenti [i])))
    i = i + 1
print(lista_while)
