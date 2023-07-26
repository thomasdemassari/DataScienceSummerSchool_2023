testo = "CiAo QuEsTo E' uN TeStO sToRto"   # cIaO qUeStO e' Un tEsTo StOrTO
testo = "gInGillo"                        # GiNgILLO
tradotto = ''

lettere = list(testo)

i = 0
for i in range(len(lettere)):
    if lettere[i].islower():
        lettera = lettere[i].upper()
    else:
        lettera = lettere[i].lower()
    tradotto = tradotto + lettera
    i = i +1

print(tradotto)
