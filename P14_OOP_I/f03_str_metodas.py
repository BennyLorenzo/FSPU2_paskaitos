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

    # nurodoma ką print funkcija turi atspausdinti, kai spausdiname patį objektą
    def __str__(self):
        return f"{self.kaina} EUR, {self.pastatymo_metai} metai."

namas_obj = Namas(100_100, 2001)
# print(namas_obj.pastatymo_metai)

namas2_obj = Namas(999_000, 2020)
# print(namas2_obj.pastatymo_metai)

# print(namas_obj)
# print(namas2_obj)