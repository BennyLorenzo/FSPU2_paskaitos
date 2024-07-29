
# dekoratoriai - funkcijos, keičiančios (papildančios) kitų funkcijų darbą

def sudek (sk1, sk2):
    return sk1 + sk2

def atimk (sk1, sk2):
    return sk1 - sk2

def numesk_skaiciu_po_kablelio(sk):
    return int(sk)

print(sudek(1,2))
print(atimk(8,2))

# dekoratorius papildys šių funkcijų darbą, suformuodamas kitą grąžinamą rezultatą (lyginis, nelyginis)

def lyginis_nelyginis(funkcija):
    def wrapper(sk1, sk2):
        res = funkcija(sk1, sk2)
        return res
    return wrapper

# patikriname ar funkcija sudek() pereina per funkciją lyginis_nelyginis()

sudek_nauja = lyginis_nelyginis(sudek)
print(sudek_nauja(1,2))

# pridedam funkcionalumą į dekoratorių

def lyginis_nelyginis(funkcija):
    def wrapper(sk1, sk2):
        res = funkcija(sk1, sk2)
        if res % 2 == 0:
            res = f"Rezultatas {res} yra lyginis."
        else:
            res = f"Rezultatas {res} yra nelyginis."
        return res
    return wrapper

sudek_nauja = lyginis_nelyginis(sudek)
print(sudek_nauja(1,2))

atimk_nauja = lyginis_nelyginis(atimk)
print(atimk_nauja(5,3))

# numesk_skaiciu_po_kablelio = lyginis_nelyginis(numesk_skaiciu_po_kablelio())
# print(numesk_skaiciu_po_kablelio(10.55)) crashins, trūksta argumentų

# tobuliname funkciją

def lyginis_nelyginis(funkcija):
    def wrapper(*args, **kwargs):
        res = funkcija(*args, **kwargs)
        if res % 2 == 0:
            res = f"Rezultatas {res} yra lyginis."
        else:
            res = f"Rezultatas {res} yra nelyginis."
        return res
    return wrapper

@lyginis_nelyginis
def sudek (sk1, sk2):
    return sk1 + sk2

@lyginis_nelyginis
def atimk (sk1, sk2):
    return sk1 - sk2

@lyginis_nelyginis
def numesk_skaiciu_po_kablelio(sk):
    return int(sk)

@lyginis_nelyginis
def dalink(sk1, sk2, sveikas_sk = False):
    res = sk1/sk2
    if sveikas_sk:
        return int(res)
    return res

@lyginis_nelyginis
def duok_penkis():
    return 5

print(sudek(1,2))
print(atimk(5,1))
print(numesk_skaiciu_po_kablelio(10.99))
print(dalink(10,5))
print(dalink(10,3,sveikas_sk=True))
print(duok_penkis())