from datetime import datetime
# klasės aprašymo sintaksė

class Namas:

    # __init__ - objekto kūrimo metu, pateikiami duomenys (inicijuojamas objekto kūrimas, aprašome priimamąjį)
    def __init__(self, kaina, pastatymo_metai):
        self.kaina = kaina # atributas - savybės, laukai
        self.pastatymo_metai = pastatymo_metai

    def grazink_amziu(self): # atributas - funkcija, metodas
        skirtumas = datetime.today() - datetime(self.pastatymo_metai, 1, 1)
        amzius = round(skirtumas.days / 365, 1)
        return amzius

    # OOP principais duomenys pasiekiami tik per metodus
    def gauk_kaina(self):
        return self.kaina

    def kainos_nustatymas(self, nauja_kaina):
        if nauja_kaina <= 0:
            print("Kaina negali būti mažesnė arba lygi 0.")
        else:
            self.kaina = nauja_kaina

    def nuolaida(self, nuolaidos_proc):
        self.kaina = self.kaina - self.kaina * nuolaidos_proc / 100

    # nurodoma ką print funkcija turi atspausdinti, kai spausdiname patį objektą
    def __str__(self):
        return f"{self.kaina} EUR, {self.pastatymo_metai} metai."

namas_obj = Namas(100_100, 2001)
namas2_obj = Namas(999_000, 2020)

print(namas_obj)
print(namas2_obj)

# tiesioginis kreipinys ir duomenų keitimas (galimas Python, kitur ne)
namas_obj.pastatymo_metai = 1930
print(namas_obj)

namas2_obj.pastatymo_metai = 1920
print(namas2_obj)

namas2_obj.pastatymo_metai += 100
print(namas2_obj)

# laikomasi OOP principų, pasiekiam ir keičiam duomenis naudojant metodus
kaina = namas_obj.gauk_kaina()
print(kaina)

namas2_obj.kainos_nustatymas(500000)
print(namas2_obj.gauk_kaina())

namas2_obj.nuolaida(50)
print(namas2_obj.gauk_kaina())
