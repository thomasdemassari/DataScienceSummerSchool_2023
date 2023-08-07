circuito = [('condensatore', 8), ('resistenza',4), ('led',5), ('diodo',1), ('trasduttore',2),
            ('transistor',12) , ('sensore',3),('solenoide',10)]

lista_nuova = [circuito[i][0] for i in range(len(circuito)) if circuito[i][1] >= 4]
print(lista_nuova)
