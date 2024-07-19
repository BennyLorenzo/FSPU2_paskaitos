# mūsų sukurtas modulis (failas/funkcijų biblioteka) su aritmetinėm funkcijom

def sumuok(sk1: int | float, sk2: int | float) -> int | float:
    res = sk1 + sk2 # skaičiuojam naudodami tarpinį kintamąjį res
    return res

def atimk(sk1: int | float, sk2: int | float) -> int | float:
    res = sk1 - sk2 # skaičiuojam naudodami tarpinį kintamąjį res
    return res

def daugink(sk1: int | float, sk2: int | float) -> int | float:
    res = sk1 * sk2 # skaičiuojam naudodami tarpinį kintamąjį res
    return res

def dalink(sk1: int | float, sk2: int | float) -> int | float:
    res = sk1 / sk2 # skaičiuojam naudodami tarpinį kintamąjį res
    return res

if __name__ == '__main__':
    print(sumuok(5, 5))
    print(atimk(5, 5))
    print(daugink(5, 5))
    print(dalink(5, 5))
