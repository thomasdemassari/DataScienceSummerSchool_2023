# scrivi la funzione
def nobulli(bullo : str):
    str_tmp = str()
    for i in range(len(bullo)):
        if (bullo[i] == "w") or (bullo[i] == "a") or (bullo[i] == "k") or (bullo[i] == " "):
            str_tmp = str_tmp + bullo[i]
    ris = str_tmp
    return(ris)

def nobulli2(bullo : str, mantieni : list):
    str_tmp2 = str()
    for z in range(len(bullo)):
        for j in range(len(mantieni)):
            if (bullo[z] == mantieni[j]):
                str_tmp2 = str_tmp2 + bullo[z]
    ris2 = str_tmp2
    return(ris2)


# NON TOCCARE, queste linee devono funzionare
bullo1 = "waekai waekai waekai waekai"
bullo2 = "bwaka rwaka swaka twaka zwaka mmmwatka"
bullo3 = "eweaekea zwxarkma qwoagkpa"

lettere = ["w","a","k", " "]

res1 = nobulli(bullo1)   # Deve RITORNARE il verso pulito "waka waka waka waka"
res1_2 = nobulli2 (bullo1, lettere)
print(res1)
print(res1_2, "\n")
res2 = nobulli(bullo2)   # Deve RITORNARE il verso pulito "waka waka waka waka waka waka"
res2_2 = nobulli2 (bullo2, lettere)
print(res2)
print(res2_2, "\n")
res3 = nobulli(bullo3)   # Deve RITORNARE il verso pulito "waka waka waka"
res3_2 = nobulli2 (bullo3, lettere)
print(res3)
print(res3_2)
