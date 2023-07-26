db = {}

nomi =     ['hacKnights','Cult  of  Cobra','unsafe\nKreW']
dossier =  ['hack.odt','cobra.odt','unsafe.docx']

# Ricerca 'tale e quale':
ricerca = 'hacKnights'         # hack.odt
# ricerca = 'Cult  of  Cobra'   # cobra.odt
# ricerca = 'unsafe\nKreW'      # unsafe.docx

# Ricerca su variazioni della normalizzazione:
# ricerca = 'hacknights'      # hack.odt
# ricerca = 'HACKNIGHTS'      # hack.odt
# ricerca = 'Hacknights'      # hack.odt
# ricerca = 'cult of cobra'   # cobra.odt
# ricerca = 'CULT OF COBRA'   # cobra.odt
# ricerca = 'Cult of cobra'   # cobra.odt
# ricerca = 'unsafe krew'     # unsafe.docx
# ricerca = 'Unsafe krew'     # unsafe.docx
# ricerca = 'UNSAFE KREW'     # unsafe.docx


i = 0
for i in range(len(nomi)):
    nomi_v0 = nomi[i].replace("  ", " ")
    nomi_v0 = nomi_v0.replace("\n", " ")
    nomi_v1 = nomi_v0.lower()
    nomi_v2 = nomi_v0.upper()
    nomi_v3 = nomi_v1.capitalize()
    
    db[nomi[i]] = dossier[i]
    db[nomi_v0] = dossier[i]
    db[nomi_v1] = dossier[i]
    db[nomi_v2] = dossier[i]
    db[nomi_v3] = dossier[i]

    i = i + 1

print(db)
print(db[ricerca])
