invitati_miei =   ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA", "VittorioG", ]
invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG", "RobertoU", "EmmaK"]

miei = set(invitati_miei)
gianni = set(invitati_gianni)
giulia = set(invitati_giulia)
tutti = miei | gianni | giulia
inter = (miei & gianni) | (gianni & giulia) | (miei & giulia)

print("Invitati miei:", len(miei))
print("Invitati gianni:", len(gianni))
print("Invitati giulia:", len(giulia))
print("Invitati totali:", len(tutti))
print("Nomi amici:", tutti)
print("Amici almeno due volte:", len(inter))
print("Nome amici almeno due volte:", inter)
