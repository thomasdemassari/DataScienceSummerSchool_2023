#parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']  # {'d': 8, 'o': 7, 'n': 3, 'l': 7}
parole = ['d','ii','nnn','dd','ooo','n']                        # {'d': 3, 'i': 2, 'n': 4, 'o': 3}

parole = "".join(parole)
lettere = set(parole)
lettere = list(lettere)
lettere.sort()
freq = dict()

for i in range(len(lettere)):
    rep = parole.count(lettere[i])
    freq[lettere[i]] = rep
    i = i+1
    
print(freq)
