carrello = []
pozzo = ['███','▓▓▓','▒▒▒', '░░░']  # <-- cima del pozzo

pozzo = ['┼┼','┤├','┐┌', '╗╔', '║║']  #  ['║', '║', '╗', '╔', '┐', '┌', '┤', '├', '┼', '┼']

i = 0
lun = len(pozzo)
while i < (lun):
    blocco = pozzo[-1]
    pezzettino = list(blocco)
    carrello = carrello + pezzettino
    print("Il pozzo è:", pozzo)
    print("Trivello lo strato", blocco, "e lo divido nei blocchi", pezzettino, "\n")

    pozzo.remove(blocco)
    i = i + 1

print("Il pozzo finale é:", pozzo)
print("Il carrello finale è:", carrello)
