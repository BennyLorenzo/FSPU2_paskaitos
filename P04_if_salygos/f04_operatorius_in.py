spring = ['kovas', 'balandis', 'gegužė']

month1 = 'sausis'
month3 = 'kovas'

print(month1 in spring)
print(month3 in spring)

print(month3, 'yra pavasario mėnesis') if month3 in spring else print(month3, 'nėra pavasario mėnesis')