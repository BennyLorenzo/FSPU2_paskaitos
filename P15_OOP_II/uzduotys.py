# 1
class Automobilis():

    def __init__(self, gamintojas, modelis):
        self.gamintojas = gamintojas
        self.modelis = modelis
        self.kuro_kiekis = 0
        self.uzvestas = False

    def __str__(self):
        return f"{self.gamintojas} {self.modelis}"

    def vaziuoti(self):
        if self.kuro_kiekis > 0 and self.uzvestas:
            print(f"{self} važiuoja.")
        elif self.kuro_kiekis <= 0 and not self.uzvestas:
            print(f"{self} reikia kuro ir užvedimo.")
        elif self.kuro_kiekis <= 0:
            print(f"{self} reikia kuro.")
        elif not self.uzvestas:
            print(f"{self} reikia užvesti.")
        else:
            print(f"{self} kažkas negerai.")

    def pildyti_degalus(self, kiekis):
        if self.kuro_kiekis + kiekis >= 100:
            self.kuro_kiekis = 100
            print(f"{self} papildyta degalais pilnai {self.kuro_kiekis}%.")
        else:
            self.kuro_kiekis += kiekis
            print(f"{self} papildyta degalais {kiekis}%.")

    def uzvesti(self):
        if self.kuro_kiekis > 0:
            self.uzvestas = True
            print(f"{self} užvesta.")
        else:
            print(f"{self} neturi kuro!")

    def uzgesinti(self):
        self.uzvestas = False
        print(f"{self} užgesinta.")

class Elektromobilis(Automobilis):

    def pildyti_degalus(self, kiekis):
        if self.kuro_kiekis + kiekis >= 100:
            self.kuro_kiekis = 100
            print(f"{self} pakrauta pilnai {self.kuro_kiekis}%.")
        else:
            self.kuro_kiekis += kiekis
            print(f"{self} pakrauta {kiekis}%.")

auto1 = Automobilis("Audi", "A3")
auto2 = Elektromobilis("BMW","i7")

auto1.uzvesti()
auto2.uzvesti()

auto1.vaziuoti()
auto2.vaziuoti()

auto1.pildyti_degalus(20)
auto2.pildyti_degalus(20)

auto1.vaziuoti()
auto2.vaziuoti()

auto1.uzvesti()
auto2.uzvesti()

auto1.vaziuoti()
auto2.vaziuoti()

auto1.uzgesinti()
auto2.uzgesinti()

auto1.pildyti_degalus(19)
auto2.pildyti_degalus(19)