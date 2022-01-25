# Globaali näkyvyys näkyy kaikkialla

etunimi = "Erkki"
sukunimi = 'Esimerkki'

# Muuttuja funktion tai metodin sisällä
def kerro_nimi():
    etunimi = 'Eveliina'  #älä käytä samaa muuttujaa kun on jo globaalina käytössä
    print('Etunimi on', etunimi, 'ja sukunimi on', sukunimi)
    # def tervehdi():
    #     print('Terve', etunimi, sukunimi)
    # tervehdi()
kerro_nimi()
print('Etunimi on', etunimi, 'ja sukunimi on', sukunimi)

# print('Etunimi on', etunimi, 'ja sukunimi on', sukunimi)