
# žodynai 99% suderinami su JSON formatu (JS objektais)
person_info = {
    'name': 'Albert',
    'surname': 'Einstein',
    'languages': ['German', 'Latin', 'Italian', 'English'],
    'occupation': {
        'role':'professor',
        'workplace':'University of Berlin'
    }
}

'''
print(type(person_info))
print(person_info)
print(person_info['name'])
print(person_info['languages'])
print(person_info['languages'][2])
print(person_info['occupation']['workplace'])
'''
for element in person_info:
    print(element)

print(type(person_info.items()))
print(person_info.keys())
print(person_info.values())
'''
for key, val in person_info.items():
        print(key, val, sep=": ")
'''

if 'Albert' in person_info.values():
    print('Albert yra tarp žodyno reikšmių.')