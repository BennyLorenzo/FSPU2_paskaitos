listas = ['sausis','vasaris','kovas','balandis','gegužė','birželis']

for elem in listas[::-1]:
    print(elem)

print("---------")
for elem in listas[3:0:-1]:
    print(elem)

print("---------")
for elem in sorted(listas):
    print(elem)

sudetinis = [('sausis', 31), ('vasaris', 28), ('kovas', 31)]

for menesis, diena in sudetinis:
    print(menesis, diena)

zodynas = {
    'sausis': 31,
    'vasaris': 28,
    'kovas': 31,
}

for menesis, diena in zodynas.items():
    print(menesis, diena)
