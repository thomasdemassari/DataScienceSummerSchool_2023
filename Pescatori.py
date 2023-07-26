ristorante, pesci = "Il Galeone", "carpe"            # True
ristorante, pesci = "Il Galeone", "aringhe"         # False
ristorante, pesci = "Al Molo",    "trote"           # True
ristorante, pesci = "Al Molo",    "orate"           # False
ristorante, pesci = "La Cambusa", "merluzzi"        # False
ristorante, pesci = "Da Zio beppe", "aringhe"       #Errore (ma dovrebe dare false)
ristorante, pesci = "Da Zio beppe", "tostapane"       #Errore (ma dovrebbe dare false)


registro = {
    "L'Ancora"  : ['aringhe', 'carpe'],
    "Il Galeone": ['merluzzi', 'carpe', 'trote'],
    "Al Molo"   : ['trote'],
    "La Cambusa": ['aringhe', 'carpe'],
}

(ristorante in registro) and (pesci in registro[ristorante]) #cosi se il ristorante non esiste darà false invece che errore
