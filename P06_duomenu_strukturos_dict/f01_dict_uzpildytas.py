
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

print(type(person_info))
print(person_info)
print(person_info['name'])
print(person_info['languages'])
print(person_info['languages'][2])
print(person_info['occupation']['workplace'])