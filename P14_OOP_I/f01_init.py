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

namas_obj = Namas(100_100, 2001)
print(namas_obj)
print(namas_obj.kaina)
print(namas_obj.pastatymo_metai)
print("Namo amžius metais:",namas_obj.grazink_amziu())

#
# namas_obj2 = Namas(999_000, 2020)
# print(namas_obj2)
# print(namas_obj2.kaina)
# print(namas_obj2.pastatymo_metai)