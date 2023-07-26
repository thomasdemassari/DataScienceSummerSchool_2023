#faccendiere1, faccendiere2 = 'Sonny', 'Lenny'
#registro = ['mortimer','rupert', 'rupert','mortimer','sonny e lenny', 'mortimer', 'rupert',  'lenny e sonny', 'mortimer', 'mortimer e rupert', 'rupert e mortimer']

faccendiere1, faccendiere2 = 'Joey', 'Vincent'
registro = ['rupert','rupert', 'mortimer e rupert','mortimer', 'mortimer', 'vincent e joey', 'rupert','mortimer', 'joey e vincent','mortimer', 'mortimer e rupert', 'rupert e mortimer']


dip1 = faccendiere1 + " e " + faccendiere2
a = dip1.lower()
dip2 = faccendiere2 + " e " + faccendiere1
b = dip2.lower()

registro.remove(a)
registro.remove(b)
print(registro)
