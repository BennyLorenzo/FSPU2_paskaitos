# listų metodų užduotys,
# naudoti listų metodus, indeksavimą
# padaryti pakeitimus originaliam liste
# ir atprintinti komentare nurodytą rezultatą

# 1 užduotis
months = ['sausis', 'gegužė', 'vasaris', 'vasaris', 'balandis', 'kovas']
# rezultatas ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė]
months.remove('gegužė')
months.remove('vasaris')
months[2] = 'kovas'
months[3] = 'balandis'
months.append("gegužė")
print(f'1 užduotis: {months}')

# 2 užduotis
months = ['gegužė', 'sausis', 'sausis', 'balandis', 'kovas']
# rezultatas ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė]
months.remove('gegužė')
months.remove('sausis')
months.insert(1, 'vasaris')
months[2] = 'kovas'
months[3] = 'balandis'
months.append("gegužė")
print(f'2 užduotis: {months}')

# sekančiuose žingsniuose pradėsim nuo vieno pradinio listo ir jis
# turės būti eigoje keičiamas taip kaip nurodyta komentaruose, bei
# po įvykdyto pakeitimo išspausdinamas

# duotas pradinis listas
months = ["sausis", "kovas", "sausis", "balandis", "Vilnius", "birželis", "sausis"]

# 3 užduotis
# ["sausis", "kovas", "sausis", "balandis", "birželis", "sausis"]
months.remove('Vilnius')
print(f'3 užduotis: {months}')

# 4 užduotis
# ["sausis", "kovas", "balandis", "birželis", "sausis"]
del months[2]
print(f'4 užduotis: {months}')

# 5 užduotis
# ["sausis", "vasaris", "kovas", "balandis", "birželis", "sausis"]
months.insert(1, 'vasaris')
print(f'5 užduotis: {months}')

# 6 užduotis
# ["sausis", "vasaris", "kovas", "balandis", "birželis", "liepa"]
months[-1] = 'liepa'
print(f'6 užduotis: {months}')

# 7 užduotis
# ["sausis", "vasaris", "kovas", "balandis", "birželis", "liepa", "rugpjūtis"]
months.append('rugpjūtis')
print(f'7 užduotis: {months}')

# 8 užduotis
# ["sausis", "vasaris", "kovas", "balandis", "birželis", "liepa", "rugpjūtis", "rugsėjis", "spalis", "lapkritis", "gruodis"]
months += ["rugsėjis", "spalis", "lapkritis", "gruodis"]
print(f'8 užduotis: {months}')

# 9 užduotis
# NEDARANT PAKEITIMŲ originaliam LISTE ATPRINTINTI lyginius mėnesius
# hint - sudarom naują listą iš keletos slice
# ["vasaris", "balandis", "birželis", "rugpjūtis", "spalis", "gruodis"]
all_months = months
all_months.insert(4, "gegužė")
print(f'9 užduotis: {all_months[1::2]}')

# 10 užduotis
# atprintinti listo ilgį
print(f'10 užduotis: listo ilgis - {len(months)}')

# Visose užduotyse kuriose nėra duoti konkretūs sąrašai(list), juos sukuriame patys,
# naudodami mažiausiai 4 elementus. Programų darbo rezultatus printinam.

# 11. Parašykite programą, kuri susumuoja visus sąrašo sudaryto iš int ir float elementus.
skaiciai = [1, 100, 4.8, 7]
print(f'11 užduotis: skaičių suma = {sum(skaiciai)}')

print("-------------------")
# 12. Parašykite programą, kuri padaugina visus sąrašo sudaryto iš int ir float elementus
# iš vartotojo įvesto skaičiaus ir atspausdina rezultatus po vieną naujoje eilutėje.
skaiciai = [1, 100, 4.8, 7]
print(f'12 užduotis:')
daugiklis = int(input("Įveskite daugiklį: "))
for skaicius in skaiciai:
    print(round(skaicius * daugiklis, 2))

print("-------------------")
# 13. Parašykite programą, kuri iš sąrašo sudaryto iš int ir float elementų
# gauna didžiausią vertę ir ją atspasdina.
skaiciai = [1, 100, 4.8, 7]
print(f'13 užduotis: didžiausias skaičius = {max(skaiciai)}')

print("-------------------")
# 14. Parašykite programą, kuri sujungia visas sąrašo(sudaryto iš str elementų)
# eilutes į vieną eilutę ir ją atspausdina.
list = ["vienas", "du", "trys"]
print(f'14 užduotis: {" ".join(list)}')

print("-------------------")
# 15. Patys sukurkite du sąrašus ir juos sujunkite į vieną.
list1 = [1, 2, 3]
list2 = ['vienas', 'du', 'trys']
merged_list = list1 + list2
print(f'15 užduotis: {merged_list}')

print("-------------------")
# 16. Parašykite python programą, kuri paprašytų vartotojo įvesti 3 sveikuosius skaičius
# ir rastų didžiausią įvestą reikšmę.
print(f'16 užduotis:')
user_input = input("Įveskite tris sveikuosius skaičius, atskirtus per tarpą: ")
input_numbers = user_input.split(" ")
i = 0
for number in input_numbers:
    input_numbers[i] = int(number)
    i += 1
print(f'Didžiausias įvestas skaičius: {max(input_numbers)}')

# 17.
# panaudoti listą months ir sukurti naują listą spring,
# su pavasario mėnesiais iš didžiosios raidės
# ['Kovas', 'Balandis', 'Gegužė']

months = ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']
spring = months[2:5]
i = 0
for month in spring:
    spring[i] = month.capitalize()
    i += 1
print(f'17 užduotis: {spring}')


# 18.
# 18a. Naudojam sąrašą darbuotojai. Parašom programą, kuri iš jo sudaro
# naują sąrašą darbuotojai2, kuriame pareigybės įrašytos didžiosiomis raidėmis.
# 18b. Tas pats kodas kaip 10a, tik papildomai - atlyginimai visiems pakelti 10%.

darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]
i = 0
darbuotojai2 = []

print(f'18a užduotis: ')
for vardas, pareigybes, atlyginimas in darbuotojai:
    darbuotojai2.append([vardas, pareigybes.capitalize(), atlyginimas])
    print(darbuotojai2[i])
    i += 1

i = 0
print(f'18b užduotis: ')
for vardas, pareigybes, atlyginimas in darbuotojai2:
    darbuotojai2[i][2] = round(atlyginimas * 1.1)
    print(darbuotojai2[i])
    i += 1
