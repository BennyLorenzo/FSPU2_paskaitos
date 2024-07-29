# privatūs atributai nepasiekiami vaikų

class Darbuotojas:

    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None

    def get_atlyginimas(self):
        if self.__atlyginimas:
            print(f"Naujas atlyginimas yra {self.__atlyginimas}.")
        else:
            print("Atlyginimas dar nepaskirtas.")

    def set_atlyginimas(self, atlyginimas):
        if atlyginimas >= 0:
            self.__atlyginimas = atlyginimas
        else:
            print("Atlyginimas turi būti teigiamas skaičius.")

darb1 = Darbuotojas("Adomas","Adomaitis","derintojas")
# print(darb1.__atlyginimas) # privatus atributas nepasiekiamas, crash
darb1.get_atlyginimas()

darb1.set_atlyginimas(-700)
darb1.set_atlyginimas(1500)
darb1.get_atlyginimas()

class Vadovas(Darbuotojas):

    # def prideti_dividendus(self, suma):
    #     if self.__atlyginimas: # crashina, privatus tėvinės klasės atributas
    #         self.__atlyginimas += suma
    pass

vad1 = Vadovas("Bosas","Bosaitis","bosas")
vad1.set_atlyginimas(2500)
vad1.get_atlyginimas()
# print(vad1.__atlyginimas)
# vad1.prideti_dividendus(1500)