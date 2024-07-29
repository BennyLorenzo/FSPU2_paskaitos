"""Programa dažnai turi sukurti ir naudoti ne vieną, o keletą
tos pačios klasės objektų. Pažiūrėsime kokius turim variantus"""
from f03_str_metodas import Namas  # importuojam klasės Namas aprašą iš f03_str_metodas failo

# sukuriam keletą kintamųjų
namas1_obj = Namas(10_000, 1986)
namas2_obj = Namas(20_000, 2000)
namas3_obj = Namas(30_000, 1983)
namas4_obj = Namas(40_000, 1980)

# patalpinam objektus į talpyklą - listą
objektu_listas = [namas4_obj, namas3_obj, namas2_obj, namas1_obj]

# dirbam su grupe objektų iškarto, o ne su kiekvienu kintamuoju individualiai

# perrenkam visus objektus ir atspausdinam jų duomenis naudodami __str__ funkcionalumą
# negalim skaičiuoti, printinamas str'as iš __str__ metodo
for namas_obj in objektu_listas:
    print(namas_obj)

# perrenkam visus objektus ir atspausdinam jų duomenis, naudodami kreipimąsi į laukus
# paskaičiuosime namų kainas su PVM
for namas_obj in objektu_listas:
    print(namas_obj.pastatymo_metai, ",kaina su PVM", namas_obj.kaina * 1.21)

# aukščiau parašytas kodas, turi trūkumą, kad riboja objektų
# kiekį iki 4 vienetų, pažiūrėkime, kaip mes galime sukaupti
# liste nuo 0 iki begalybės objektų. tam reikia kartojimo
# sakinio while ir vartotojo įvesties.

# vartotojo įvestis, galim sukaupti kiek tik reikia objektų
kaupiklis = []
while True:
    ivestis = input("Įveskite metus, arba q - pabaigti įvestį")
    if ivestis == "q":
        break
    metai = int(ivestis)
    kaina = float(input("Įveskite kainą"))

    naujas_namo_obj = Namas(kaina, metai)
    kaupiklis.append(naujas_namo_obj)

    for namo_obj in kaupiklis:
        print(namo_obj)