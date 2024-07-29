
# _ - laukas arba metodas yra apsaugotas, galima naudoti tik tame pačiame faile
# __ - laukas arba metodas yra privatus, pakeitimai vaikiniame elemente negalimi

paprastas_skaicius = 1

def daugink(sk1, sk2): # apsaugota funkcija (klasėje - metodas)
    return sk1 * sk2

_skaicius = 10 # apsaugotas kintamasis (klasėje - laukas)

def _sudek(sk1, sk2): # apsaugota funkcija (klasėje - metodas)
    return sk1 + sk2

__privatus_skaicius = 100 # privatus kintamasis

def __atimk(sk1, sk2): # privati funkcija
    return sk1 - sk2

class Darbuotojas:

    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self._atlyginimas = None

    def get_atlyginimas(self):
        if self._atlyginimas:
            print(self._atlyginimas)
        else:
            print("Atlyginimas dar nepaskirtas.")

    def set_atlyginimas(self, atlyginimas):
        if atlyginimas >= 0:
            self._atlyginimas = atlyginimas
        else:
            print("Atlyginimas turi būti teigiamas skaičius.")

darb1 = Darbuotojas("Adomas","Adomaitis","derintojas")
print(darb1._atlyginimas)
darb1.get_atlyginimas()
darb1._atlyginimas = 1000
darb1.get_atlyginimas()
darb1.set_atlyginimas(2500)
darb1.get_atlyginimas()

class Vadovas(Darbuotojas):

    def prideti_dividendus(self, suma):
        if self._atlyginimas:
            self._atlyginimas += suma

vad1 = Vadovas("Bosas","Bosaitis","bosas")
vad1.set_atlyginimas(1500)
print(vad1._atlyginimas)
vad1.prideti_dividendus(1500)
print(vad1._atlyginimas)