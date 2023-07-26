# piano_utente = 3; piano_ascensore = 7    # 7,6,5,4,3,DING!
# piano_utente = 5; piano_ascensore = 0   # 0,1,2,3,4,5,DING!
# piano_utente = 3; piano_ascensore = 3   # DING!
# piano_utente = 4; piano_ascensore = 6   # 6,5,4,DING!
# piano_utente = 6; piano_ascensore = 4   # 4,5,6,DING!

def DieciPiani(piano_utente, piano_ascensore):
    piani = range(10)
    i = 0

    if (piano_ascensore > piano_utente):
        for piano in range(piano_ascensore-piano_utente+1):
            piano = piano_ascensore - piani[i]
            i = i + 1
            print(piano)
    else:
        if (piano_ascensore < piano_utente):
            for piano in range(piano_utente-piano_ascensore+1):
                piano = piano_ascensore + piani[i]
                i = i + 1
                print(piano)
    print("DING")

DieciPiani(56, 58)
