import pickle

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
auto2 = Elektromobilis("BMW", "i7")

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


# 2
class CoffeeShop:

    def __init__(self, name, meniu):
        self.name = name
        self.meniu = meniu
        self.orders = []

    def add_order(self, item):
        if item in self.meniu.keys():
            self.orders.append(item)
        else:
            print("Šiuo metu šios prekės nėra!")

    def fulfill_order(self):
        if len(self.orders) > 0:
            del self.orders[0]
        else:
            print("Visi užsakymai įvykdyti!")

    def list_orders(self):
        return self.orders

    def due_amount(self):
        sum = 0
        for item in self.orders:
            for key, value in self.meniu.items():
                if item == key:
                    sum += value['price']
        print(sum)

    def cheapest_item(self):
        prices = []
        for key, value in self.meniu.items():
            prices.append(value['price'])
        return min(prices)

    def drinks_only(self):
        drinks = []
        for key, value in self.meniu.items():
            if value['type'] == 'drink':
                drinks.append(key)
        return drinks

    def food_only(self):
        food = []
        for key, value in self.meniu.items():
            if value['type'] == 'food':
                food.append(key)
        return food


cafe1 = CoffeeShop("La Chikita", {
    'cola':
        {
            'type': 'drink',
            'price': 2.2},
    'fanta':
        {
            'type': 'drink',
            'price': 2},
    'burger':
        {
            'type': 'food',
            'price': 4.5},
    'pizza':
        {
            'type': 'food',
            'price': 12}
})

cafe1.add_order('cola')
cafe1.add_order('burger')
cafe1.add_order('burger')
# cafe1.fulfill_order()
# print(cafe1.orders)
print(cafe1.list_orders())

print(cafe1.cheapest_item())
cafe1.due_amount()
print(cafe1.drinks_only())
print(cafe1.food_only())


# 3
class ElectronicDevice:

    def __init__(self, brand, price, warranty_period):
        self.brand = brand
        self.__price = price  # EUR
        self.__warranty_period = warranty_period  # months

    @property  # geteris
    def price(self):
        return self.__price

    def get_details(self):
        print(f"Device details: {self.brand}, {self.__price} EUR, garantija: {self.__warranty_period} mėn.")

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
        return self.__price


class Laptop(ElectronicDevice):

    def __init__(self, brand, price, warranty_period, ram, storage):
        super().__init__(brand, price, warranty_period)
        self.ram = ram  # GB
        self.storage = storage  # GB


class Smartphone(ElectronicDevice):

    def __init__(self, brand, price, warranty_period, screen_size, battery_capacity):
        super().__init__(brand, price, warranty_period)
        self.screen_size = screen_size  # cm
        self.battery_capacity = battery_capacity  # hours


class Television(ElectronicDevice):

    def __init__(self, brand, price, warranty_period, mountable, resolution):
        super().__init__(brand, price, warranty_period)
        self.mountable = mountable  # bool
        self.resolution = resolution  # 1080p


class Discount():

    def apply_discount(self, obj, procent):
        if 0 < procent <= 100:
            res = obj.price - obj.price * procent / 100
            print(f"Pritaikyta {procent}% nuolaida. Nauja kaina: {res} EUR")
            return res
        else:
            print("Nuolaidos pritaikyti nepavyko.")


laptop1 = Laptop("Asus", 1400, 12, 8, 500)
laptop2 = Laptop("Apple", 2500, 24, 12, 1000)
smartphone1 = Smartphone("Samsung", 1200, 6, 120, 6)
smartphone2 = Smartphone("Xiaomi", 800, 0, 100, 4)
tv1 = Television("Phillips", 4000, 36, False, 2160)
tv2 = Television("Šilelis", 250, 12, True, 760)

laptop1.get_details()
laptop2.get_details()
smartphone1.get_details()
smartphone2.get_details()
tv1.get_details()
tv2.get_details()

# smartphone1.__price = 10000 # protected attribute, does not work
# smartphone1._warranty_period = 36 # protected attribute, does not work

discount = Discount().apply_discount(tv1, 60)


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


try:
    with open('irasai.pickle', mode='rb') as failas:
        print("Failas įkeltas!")
        irasai = pickle.load(failas)
        biudzetas = irasai
except:
    print("Failas nerastas!")
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
        with open('irasai.pickle', mode='wb') as failas:
            pickle.dump(biudzetas, failas)
        print("Programa baigė darbą.")
        break
    else:
        print("Tokio pasirinkimo nėra!")