# Harjoitus, jossa tehdään luokkia ja olioita

# MODULIEN JA KIRJASTOJEN LATAUKSET

# LUOKKIEN MÄÄRITTELY, muista iso etukirjain, rivit 7 ovat parametreja, luokan nimen jälkeen kaksoispiste, init-funktio=(olion)muodostusfunktio

# Määritellään Henkilö-luokka (yliluokka superclass / parent class), joka määrittelee yleiset ominaisuudet

class Henkilo:
    def __init__(self, etunimi, sukunimi, osasto):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.osasto = osasto

# Tehdään lista työhuoneista
tyohuoneet = ['A228']

# Opiskelija-luokka (aliluokka subclass / child class), perii Henkilö-luokan ominaisuudet
class Opiskelija(Henkilo):
    def __init__(self, etunimi, sukunimi, osasto, opiskelijanumero):
        super().__init__(etunimi, sukunimi, osasto)
        self.opiskelijanumero = opiskelijanumero
class Opettaja(Henkilo):
    def __init__(self, etunimi, sukunimi, osasto, tyohuone):
        super().__init__(etunimi, sukunimi, osasto)
        # tai self.xyz = tyohuone
        self.tyohuone = tyohuone

# Opettaja-luokka, perii Henkilo-luokan, ominaisuutena työhuone, esim. A228

# VARSINAINEN OHJELMA

# Luodaan opiskelija-olio ja opettaja-olio

opiskelija1 = Opiskelija('Jakke', 'Jäynä', 'ICT', 123456)
opettaja1 = Opettaja('Olli', 'Opettaja', 'Tieto- ja viestintätekniikka', 'A228')

# Testataan oliota
print('Opiskelija', opiskelija1.etunimi, opiskelija1.sukunimi, 'opiskelee', opiskelija1.osasto,'-osastolla, opiskelijanumero', opiskelija1.opiskelijanumero)
print(opettaja1.etunimi, opettaja1.sukunimi, 'työskentelee huoneessa',opettaja1.tyohuone)

# Oma versio käyttäen listaa hyödyksi
# print('Opettaja', opettaja1.etunimi, opettaja1.sukunimi, 'opettaa', opettaja1.osasto,'-osastolla työhuoneessa',tyohuoneet[0])