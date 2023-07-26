matrimoni = ["Amilcare-Maria Eusonia", "Oronzo Pio-Genoveffa", "Venceslao-Elvira"]
#matrimoni = ["Liutprando-Brunilde", "Clodoveo-Elvira Pancrazia Ludmilla", "Gian Evaristo-Ubalda"]

sposi1 = matrimoni[0].split("-")
sposi2 = matrimoni[1].split("-")
sposi3 = matrimoni[2].split("-")

diz = { 
    sposi1[0] : sposi1[1],
    sposi2[0] : sposi2[1],
    sposi3[0] : sposi3[1]
}

print(diz)
