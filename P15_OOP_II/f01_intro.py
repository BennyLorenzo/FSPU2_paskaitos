"""Objektinį programavimą patogu naudoti programose, kurios atvaizduoja
realaus pasaulio objektus, turinčius savybes, bei galimus veiksmus.
Įsivaizduokim žaidimą, kuriame veikėjai yra gyvūnai, pabandykime
aprašyti jų klases.
P.S. Pabaigę pirmąjį variantą, pamatėme, kad turime 3 kart pakartotas
tas pačias kodo eilutes. Šią problemą spręsime sekančiame faile.
"""


class Kate:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

    def miaukseti(self):
        print(f"{self.vardas} sako miau miau")

    def __str__(self):
        return f"{self.vardas} {self.spalva}"


class Shuo:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

    def loti(self):
        print(f"{self.vardas} sako au au")

    def __str__(self):
        return f"{self.vardas} {self.spalva}"


class Papuga:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva


kate1_o = Kate("Rainė", "raina")
kate1_o.begti()
kate1_o.miaukseti()
print(kate1_o)

kate2_o = Kate("Alisa", "balta")
kate2_o.begti()
kate2_o.miaukseti()
print(kate2_o)

shuo1_o = Shuo("Reksas", "margas")
shuo1_o.begti()
shuo1_o.loti()
print(shuo1_o)
