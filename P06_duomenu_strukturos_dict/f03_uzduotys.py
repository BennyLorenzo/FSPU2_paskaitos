# skirtuko funkcija
counter = 1
def skirtukas(count):
    print("-----------")
    print(f'{count} užduotis')
    print("-----------")
'''
# 1 užduotis
skirtukas(counter)
counter += 1
automobile = {
    'make': 'Lotus',
    'model': 'Exige',
    'country': 'United Kingdom',
    'drive': '2-wheel',
    'engine': 'V6',
    'power': '430 bhp',
    'year': '2010',
    'exterior': {
        'color':'blue',
        'finish':'gloss'
    },
    'interior': {
        'color': 'black',
        'material': 'leather',
        'stitching': 'red'
    },
    'additional': ['heated rear window','rear parking sensors','hard top storage bag']
}
print(automobile['make'])
print(automobile['exterior']['finish'])
print(automobile['interior']['material'])
print(automobile['additional'])

# 2 užduotis
skirtukas(counter)
counter += 1
darbuotojas = ['Jogaila', 'programuotojas', 1999, 2500]
darbuotojai = {}
darbuotojai.update({
    'vardas':darbuotojas[0],
    'pareigos':darbuotojas[1],
    'darbo_pradzios_metai': darbuotojas[2],
    'atlyginimas': darbuotojas[3]
})
print(darbuotojai)
darbuotojai['vardas'] = 'Jonas'
print(darbuotojai)
darbuotojai['stazas'] = 2024 - darbuotojai['darbo_pradzios_metai']
print(darbuotojai)
del darbuotojai['darbo_pradzios_metai']
print(darbuotojai)

# 3 užduotis
skirtukas(counter)
counter += 1
user_input = input("Įveskite savo vardą, pavardę ir amžių, atskirtus tarpais: ")
user_data = user_input.split(" ")
user_dict = {}
user_dict.update({
    'vardas':user_data[0],
    'pavarde':user_data[1],
    'amzius':user_data[2]
})
for key, value in user_dict.items():
    print(key, value, sep=": ")

# 4 užduotis
skirtukas(counter)
counter += 1
business = {
    'industry': 'logistics',
    'size': ['small', 'medium', 'large'],
    'valuation': 1200000,
    'for_sale': False,
    'owner':('Mantas','Linas'),
    'GRB coefficient': 1.24
}
for key, value in business.items():
    print(key, value, sep=": ")

# 5 užduotis
skirtukas(counter)
counter += 1
miestai1 = ["Vilnius", "Kaunas", "Klaipėda"] # didžiausi miestai
miestai2 = ["Šiauliai", "Panevėžys", "Alytus"] # mažesni miestai
miestai3 = ["Prienai", "Kretinga"] # miesteliai
miestai = {
    "didelis miestas": ["Vilnius", "Kaunas", "Klaipėda"],
    "mazas miestas": ["Šiauliai", "Panevėžys", "Alytus"],
    "miestelis": ["Prienai", "Kretinga"]
}
user_input = input("Įveskite norimą miestą: ")
for key, value in miestai.items():
    if user_input in value:
        print(f'{user_input} yra {key}.')
    else:
        print('Miesto dydis nežinomas.')
'''
# 6 užduotis
skirtukas(counter)
counter += 1
grades_sum = 0
salinami_studentai = []
studentai = {
    "Tomas": [4, 8, 6, 7, 2],
    "Lina": [6, 1, 5, 8, 5],
    "Viktoras": [8, 8, 7, 9, 10],
    "Rasa": [6, 8, 6, 8, 7],
    "Benas": [2, 1, 3, 6, 10],
    "Sandra": [6, 7, 9, 3, 4]
}
for key, value in studentai.items():
    grades_sum += (sum(value) / len(value))
    print(key,value, sep=" pažymiai: ")
    if ((sum(value)/len(value)) < 5):
        salinami_studentai.append(key)
    for grade in value:
        if grade < 5:
            salinami_studentai.append(key)
print(f'Studentų pažymių vidurkis: {round(grades_sum / len(studentai),1)}')
for studentas in salinami_studentai:
    del studentai[studentas]
print(f'Šalinami studentai: {salinami_studentai}')
print(f'Likę studentai: {studentai}')