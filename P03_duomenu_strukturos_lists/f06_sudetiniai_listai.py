darbuotojai = [
    ['Valdas', 'Programuotojas', 2000],
    ['Adomas', 'Direktorius', 3000],
    ['Aldona', 'Vadybininkas', 1800],
    ['Jogaila', 'Programuotojas', 2500],
]

print(darbuotojai[0])
print(darbuotojai[0][1].upper())

for darbuotojas in darbuotojai:
    print(darbuotojas[0], darbuotojas[2])

atlyginimai = []
for vardas, pareigos, atlyginimas in darbuotojai:
    atlyginimai.append(atlyginimas)
print(sum(atlyginimai))

suma = 0
for darbuotojas in darbuotojai:
    suma += darbuotojas[2]
print(suma)

pareigybes = []
for vardas, pareigos, atlyginimas in darbuotojai:
    pareigybes.append(pareigos)
print(f'Programuotojai: {pareigybes.count("Programuotojas")}')

# suskaičiuoti atlyginimų sumą ir programuotojų skaičių su vienu ciklu
pareigybes = []
atlyginimai = []
for vardas, pareigos, atlyginimas in darbuotojai:
    pareigybes.append(pareigos)
    atlyginimai.append(atlyginimas)
print(f'Atlyginimų suma: {sum(atlyginimai)}, programuotojų skaičius: {pareigybes.count("Programuotojas")}')