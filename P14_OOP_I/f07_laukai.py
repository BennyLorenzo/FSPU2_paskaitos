

class Namas:
    valiutos_kodas = 'EUR' # klasės laukas

    def __init__(self, kaina, pastatymo_metai):
        self.kaina = kaina
        self.pastatymo_metai = pastatymo_metai

    def __str__(self):
        return f"{self.pastatymo_metai}, {self.kaina} {self.valiutos_kodas}"

namas1_obj = Namas(100_000, 2001)
namas2_obj = Namas(999_000, 2020)

print(namas1_obj)
print(namas2_obj)

Namas.valiutos_kodas = '€'

print(namas1_obj)
print(namas2_obj)

# negalima keisti klasės lauko vienam objektui
namas1_obj.valiutos_kodas = "USD"
print(namas1_obj)
print(namas2_obj)

Namas.valiutos_kodas = "AUD"
print(namas1_obj) # išlieka objekto valiutos kodas
print(namas2_obj)