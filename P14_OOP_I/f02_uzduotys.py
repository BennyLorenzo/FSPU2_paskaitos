# 1
class Knyga:

    def __init__(self, pavadinimas, autorius, puslapiu_skaicius, perskaityti_puslapiai):
        self.pavadinimas = pavadinimas # atributas - savybės, laukai
        self.autorius = autorius
        self.puslapiu_skaicius = puslapiu_skaicius
        self.perskaityti_puslapiai = perskaityti_puslapiai

    def paskaiciuok_kiek_liko_puslapiu(self): # atributas - funkcija, metodas
        return self.puslapiu_skaicius - self.perskaityti_puslapiai

    def __str__(self):
        return f"{self.pavadinimas}, {self.autorius}, perskaityta {self.perskaityti_puslapiai} iš {self.puslapiu_skaicius} puslapių."

if __name__ == '__main__':
    knyga1 = Knyga("Laikinai jūsų","Antanas Šileika", 304, 200)
    knyga2 = Knyga("Broliai Karamazovai I tomas","Fiodoras Dostojevskis", 552, 357)

    print(knyga1)
    print(knyga2)

    print("Liko perskaityti",knyga1.paskaiciuok_kiek_liko_puslapiu(),"puslapių.")
    print("Liko perskaityti",knyga2.paskaiciuok_kiek_liko_puslapiu(),"puslapių.")

# 2
class Calculator:

    def __init__(self, skaicius1, skaicius2):
        self.skaicius1 = skaicius1
        self.skaicius2 = skaicius2

    def sudetis(self):
        return self.skaicius1 + self.skaicius2

    def atimtis(self):
        return self.skaicius1 - self.skaicius2

    def daugyba(self):
        return self.skaicius1 * self.skaicius2

    def dalyba(self):
        return self.skaicius1 / self.skaicius2

if __name__ == '__main__':
    calc1 = Calculator(20,45)
    calc2 = Calculator(445.4,228.74)
    print(calc1.sudetis())
    print(calc2.atimtis())
    print(calc2.daugyba())
    print(calc1.dalyba())

# 3
class Employee:

    def __init__(self, name, last_name, position, company):
        self.name = name
        self.last_name = last_name
        self.full_name = f"{name} {last_name}"
        self.email = f"{str.lower(name)}.{str.lower(last_name)}@{str.lower(company)}.com"
        self.full_info = f"{self.full_name}, {position} of {company}, email: {self.email}"

    def __str__(self):
        return self.full_info


emp = Employee("John", "Doe", "manager", "APPLE")
if __name__ == '__main__':
    print(emp)

# 4
class Country:

    def __init__(self, name, population, area_km2):
        self.name = name
        self.area_km2 = area_km2
        self.population = population

    def is_big(self):
        if self.population > 20000000 and self.area_km2 > 3000000:
            return True
        else:
            return False

    def compare_pd(self, other_country):
        if self.population/self.area_km2 > other_country.population/other_country.area_km2:
            print(f"{self.name} has a larger population density than {other_country.name}.")
        else:
            print(f"{self.name} has a smaller population density than {other_country.name}.")

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
if __name__ == '__main__':
    print(australia.is_big())
    print(andorra.is_big())
    andorra.compare_pd(australia)