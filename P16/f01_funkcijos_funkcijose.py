

sk = 100 # duomenys

def sudek (sk1, sk2): # funkcijos
    return sk1 + sk2

def atimk (sk1, sk2):
    return sk1 - sk2

print(sk)

# funkcijų kodas taip pat gali būti kaip duomenys, type - function

print(sudek)

# funkcija kaip argumentas kitai funkcijai

def daryk_aritmetini_veiksma(sk1, sk2, funkcija):
    res = funkcija(sk1, sk2)
    return res

print(daryk_aritmetini_veiksma(400, 200, sudek))
print(daryk_aritmetini_veiksma(400, 200, atimk))
print(daryk_aritmetini_veiksma(400, 200, print))

# funkcija gali grąžinti kitą funkciją

def grazink_funkcija_keliancia_laipsniu(laipsnis):
    def pakelk(skaicius):
        return skaicius ** laipsnis
    return pakelk

# def kelk_kvadratu

kelk_kvadratu = grazink_funkcija_keliancia_laipsniu(2)
print(kelk_kvadratu(9))

kelk_kubu = grazink_funkcija_keliancia_laipsniu(3)
print(kelk_kubu(2))
