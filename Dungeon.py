cerco,caverna='il tesoro', ['un masso','una trappola','delle spade','il tesoro','una ragnatela','un boleto delle tombe']

cerco,caverna = 'il talismano del potere', ['una trappola','un boleto delle tombe','una ragnatela']
# cerco, caverna = 'la corona di rubini', []                         # funziona anche in questi casi particolari?
# cerco, caverna = 'la corona di rubini', ['la corona di rubini']    #
# cerco, caverna = 'la corona di rubini', ['il martello di granito'] #

# scrivi qui

i = 0
j = 0 
x = -1

if cerco in caverna:
    while caverna[i] != cerco:
        print("Vedo", caverna[i])
        i = i + 1
    print("Che fortuna! Ho trovato il tesoro")

    indietro = caverna[:i]
    indietro.reverse()

    for z in range(len(indietro)):
        print("Vedo", indietro[z])
    print("Eco")

else:
    while j < len(caverna):
        print("Vedo", caverna[j])
        j = j + 1
    print("Putroppo", cerco, "non c'è")
    print("Torno indietro!")
    while abs(x+1) < len(caverna):
        print("Vedo", caverna[x])
        x = x - 1
