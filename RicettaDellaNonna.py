#          0        1    2           3               4        5         6        7       8         9           10    11
ricetta = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
#ricetta = "cappone , pepe,\noliva\n,\n\tpepe, acciuga "   #  1 oliva 2 pepe 0 cappero

ricetta = ricetta.split(",")
i = 0
j = 0
ricettaOK = list()

print(ricetta)

for i in range(11):
    ingrediente = ricetta[i].strip()
    ricettaOK.append(ingrediente)
    i = i +1

tobuy = ["cappero", "pepe", "oliva"]
oliva, capperi, pepe = 0, 0, 0

j = 0
z = 0

capperi = ricettaOK.count(tobuy[0])
pepe = ricettaOK.count(tobuy[1])
oliva = ricettaOK.count(tobuy[2])  

print("Servono:")
print(oliva, "olive")
print(pepe, "pepe")
print(capperi, "capperi")
