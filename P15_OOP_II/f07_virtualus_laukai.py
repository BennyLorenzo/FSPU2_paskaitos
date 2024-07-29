class Darbuotojas:

    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None

    # dekoratorius
    @property # geteris
    def atlyginimas(self):
        if self.__atlyginimas:
            return self.__atlyginimas
        else:
            return "Atlyginimas dar nepaskirtas."

    @atlyginimas.setter # setteris
    def atlyginimas(self, suma):
        if suma >= 0:
            self.__atlyginimas = suma
            print(f"Naujas atlyginimas {self.__atlyginimas}.")
        else:
            print("Atlyginimas turi būti teigiamas skaičius.")

    #
    # def set_atlyginimas(self, atlyginimas):
    #     if atlyginimas >= 0:
    #         self.__atlyginimas = atlyginimas
    #     else:
    #         print("Atlyginimas turi būti teigiamas skaičius.")

darb1 = Darbuotojas("Adomas","Adomaitis","derintojas")
print(darb1.vardas,darb1.pavarde,darb1.pareigos)
print(darb1.atlyginimas)
darb1.atlyginimas = 1000 # perimta priskyrimo operacija, taip pat printina įvykdžius
print(darb1.atlyginimas)


# darb1.set_atlyginimas(-700)
# darb1.set_atlyginimas(1500)
# darb1.get_atlyginimas()