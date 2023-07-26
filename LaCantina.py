parola = "cantina"  #  ['c','a','n','t','i','n','a','n','i','t','n','a','c']
#parola = "vino"    #  ['v', 'i', 'n', 'o', 'n', 'i', 'v']
#parola = "ok"      #  ['o', 'k', 'o']

l1 = list(parola)
l2 = l1[:]
l1.reverse()

print(l2 + l1[1:])

#l1 = [parola, parola.reverse()]
