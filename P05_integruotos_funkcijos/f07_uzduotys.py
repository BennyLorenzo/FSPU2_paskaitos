# skirtuko funkcija
counter = 1
def skirtukas(count):
    print("-----------")
    print(f'{count} užduotis')
    print("-----------")

# 1 UŽDUOTIS
skirtukas(counter)
counter += 1
listas = ['sausis', 'vasaris', 'LT', 'UK', 'LTU']
for item in listas:
    print(item, end=" ") if len(item) < 4 else None
print("")
# atprintinti iš listo tik sąntrumpų stringus
# santrumpą randame naudodami funkciją len

# 2. UŽDUOTIS
# Sukurti Python listą su visų savo žinomų duomenų tipų elementais.
# Išspausdinkite visų tipų pavadinimus(str, int ir pan), naudodami sukurtą listą.
skirtukas(counter)
counter += 1
type_list = ["string", 10, 10.5, True, ["list"]]
for item in type_list:
    print(type(item), end=" ")
print("")

# 3. UŽDUOTIS
# Atspausdinkite visus elementus(jų reikšmes) iš 2-oje užduotyje sukurto listo, taip pat ir jų tipus,
# atskirdami "|" simboliu.
skirtukas(counter)
counter += 1
for item in type_list:
    print(item, type(item), end="|")
print("")

# 4. UŽDUOTIS
# Parašykit programą, kuri paklausia vartotojo koks jo vardas, kiek jam metų ir tiek kartų kiek jam metų
# atspausdina pasveikinimą su gimtadieniu, pasveikinimo eilutėje panaudodama įvestą vardą.
# Kartojimui naudojam for, range
skirtukas(counter)
counter += 1
user_input = input("Įveskite savo vardą ir metų skaičių, atskirtus tarpu: ")
user_data = [user_input.split(" ")]
for vardas, metai in user_data:
    for i in range(int(metai)):
        print(f'Su gimtadieniu, {vardas}!')


# 5. UŽDUOTIS Sukurkite list su float tipo duomenimis, turinčius 3 skaitmenis po kablelio.
# panaudodami pirmojo listo duomenis, sukurkite kitą list su visomis reikšmėmis, suapvalintomis iki
# 2 skaičių po kablelionnaudodami round. Atspausdinkit abu listus.
skirtukas(counter)
counter += 1
float_list = [214.547, 1357.789, 14777.658]
rounded_list = []
for item in float_list:
    rounded_list.append(round(item, 2))
print(float_list)
print(rounded_list)

# 6. UŽDUOTIS Sukurkite list su darbuotojų vardais ir juos surūšiuokite A-Z tvarka, po to Z-A,
# rezultatus atspausdinkite.
skirtukas(counter)
counter += 1
employee_list = ["Tadas", "Aidas", "Rasa", "Monika", "Tomas", "Greta", "Beatričė"]
employee_list.sort()
print(employee_list)
employee_list.reverse()
print(employee_list)

# 7. UŽDUOTIS Parašykite programą, kuri leistų vartotojui įrašyti bet kokį skaičių ir jį
# suapvalinti iki tam tikro skaičiaus ženklų po kablelio(vartotojas įveda iki kiek ženklų
# po kablelio jis nori suapvalinti).
skirtukas(counter)
counter += 1
user_input = input("Įveskite bet kokį skaičių ir iki kiek ženklų po kablelio norite skaičių suapvalinti, atskirta tarpu: ")
user_data = [user_input.split(" ")]
for skaicius, apvalinimas in user_data:
    print(f'Suapvalintas skaičius: {round(float(skaicius), int(apvalinimas))}')

# BONUS
# užduotys, nebūtinai
# iš
# šios
# paskaitos
# # 8. UŽDUOTIS Suskaičiuoti kiek kiekvieno duomenų tipo elementų
# # turim liste ir atprintinti rezultatus, pvz "str - 3" "int - 2" ir t.t.:
# listas = ['A', 'B', 'C', 1, 2, 0.5, 0.7777, True, (1, 2), (10, 20), [4, 5]]
skirtukas(counter)
counter += 1
listas = ['A', 'B', 'C', 1, 2, 0.5, 0.7777, True, (1, 2), (10, 20), [4, 5]]
types = [
["str", 0],
["int", 0],
["float", 0],
["list", 0],
["tuple", 0],
["bool", 0],
["other", 0]
]
for item in listas:
    if type(item) is str:
        types[0][1] += 1
    elif type(item) is int:
        types[1][1] += 1
    elif type(item) is float:
        types[2][1] += 1
    elif type(item) is list:
        types[3][1] += 1
    elif type(item) is tuple:
        types[4][1] += 1
    elif type(item) is bool:
        types[5][1] += 1
    else:
        types[6][1] += 1
for type, num in types:
    print(f'{type} - {num}', end=" ")
print("")

# 9. UŽDUOTIS
# Panaudoti paskaitose naudotą listą darbuotojai, susumuoti TIK programuotojų atlyginimus.
skirtukas(counter)
counter += 1
darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]
salaries = []
for vardas, pareigos, atlyginimas in darbuotojai:
    salaries.append(atlyginimas)
print(f'Visų darbuotojų atlyginimų suma: {sum(salaries)}')

# 10. UŽDUOTIS
# Išsiaiškinti pvz per wiki puslapį kaip yra nustatoma ar metai yra keliamieji ar ne. Parašyti
# palyginimą naudojant loginius operatorius, kuris nustato ar metai yra keliamieji.
# Vienas iš testų turėtų būti su 2100 metais kurie yra nekeliamieji.
skirtukas(counter)
counter += 1
input_year = int(input("Įveskite norimus metus: "))
keliamieji = False
if (input_year % 4 == 0):
    if (input_year % 100 == 0):
        if (input_year % 400 == 0):
            keliamieji = True
        else:
            keliamieji = False
    else:
        keliamieji = True
else:
    keliamieji = True
if keliamieji:
    print(f'{input_year} yra keliamieji metai.')
else:
    print(f'{input_year} nėra keliamieji metai.')