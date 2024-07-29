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
