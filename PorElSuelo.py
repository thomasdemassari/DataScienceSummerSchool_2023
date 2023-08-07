frase = ['Por', 'el', 'suelo', 'camina', 'mi', 'pueblo']

frase = ['Esperando', 'la', 'ultima', 'ola']
# produce:  [(0, 1, 2, 3, 4, 5, 6, 7, 8), (0, 1), (0, 1, 2, 3, 4, 5), (0, 1, 2)]

lista_nuova = list()
[lista_nuova.append(tuple(range(1, (len(frase[i]) + 1)))) for i in range(len(frase))]
print(lista_nuova)
