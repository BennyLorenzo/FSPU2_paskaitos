# 4
class Irasas:

    def __init__(self, menesis, pavadinimas, suma):
        self.menesis = menesis
        self.pavadinimas = pavadinimas
        self.suma = suma

    def __repr__(self):
        return (f"Mėnesis: {self.menesis}, pavadinimas: {self.pavadinimas}, suma: {self.suma}")


class PajamuIrasas(Irasas):
    pass


class IslaiduIrasas(Irasas):
    pass


class Biudzetas:

    def __init__(self, *args):
        self.irasai = [*args]

    def gauti_balansa(self):
        pajamos = []
        islaidos = []
        for elem in self.irasai:
            if type(elem) == PajamuIrasas:
                pajamos.append(elem.suma)
            elif type(elem) == IslaiduIrasas:
                islaidos.append(elem.suma)
            else:
                print("Įrašas neaptiktas.")
        print(f"Visos pajamos: {sum(pajamos)}\n"
              f"Visos išlaidos: {sum(islaidos)}\n"
              f"Balansas: {sum(pajamos) - sum(islaidos)}"
              )

    def parodyti_ataskaita(self):
        print("Visų įrašų ataskaita: ")
        for irasas in self.irasai:
            if type(irasas) == PajamuIrasas:
                print("Pajamų įrašas - ", irasas)
            elif type(irasas) == IslaiduIrasas:
                print("Išlaidų įrašas - ", irasas)
            else:
                print("Įrašas neaptiktas.")


biudzetas = Biudzetas()
while True:
    print("Pasirinkite funkciją:\n"
          "1 - įrašyti pajamas\n"
          "2 - įrašyti išlaidas\n"
          "3 - peržiūrėti balansą\n"
          "4 - peržiūrėti ataskaitą\n"
          "q - išeiti\n")
    pasirinkimas = input("Įveskite pasirinkimą: ")
    if pasirinkimas == "1":
        pajamu_ivestis = input("Įveskite mėnesį, pavadinimą ir sumą, atskirtus kableliais: ")
        pajamu_eilute = pajamu_ivestis.split(',')
        pajamos = PajamuIrasas(pajamu_eilute[0], pajamu_eilute[1], float(pajamu_eilute[2]))
        biudzetas.irasai.append(pajamos)
    elif pasirinkimas == "2":
        islaidu_ivestis = input("Įveskite mėnesį, pavadinimą ir sumą, atskirtus kableliais: ")
        islaidu_eilute = islaidu_ivestis.split(',')
        islaidos = IslaiduIrasas(islaidu_eilute[0], islaidu_eilute[1], float(islaidu_eilute[2]))
        biudzetas.irasai.append(islaidos)
    elif pasirinkimas == "3":
        biudzetas.gauti_balansa()
    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()
    elif pasirinkimas == "q":
        print("Programa baigė darbą.")
        break
    else:
        print("Tokio pasirinkimo nėra!")