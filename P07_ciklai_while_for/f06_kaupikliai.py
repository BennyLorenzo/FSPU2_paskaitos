stringas_duomenys = "Šiame stringe yra balsių aeouioiuioiuyoo"
stringas_kaupiklis = ""
tikrinimas = "aeiouy"

for simbolis in stringas_duomenys:
    if simbolis in tikrinimas:
        stringas_kaupiklis += simbolis
print(stringas_kaupiklis)
print(len(stringas_kaupiklis))

listas_duomenys = list(range(12))
print(listas_duomenys)
nelyginiai_kaupiklis =[]

for elem in listas_duomenys:
    if elem % 2 != 0:
        print(elem)
        nelyginiai_kaupiklis.append(elem)

print(nelyginiai_kaupiklis)

listas = [34, 18, 70, 2, 8, 30, 19, 5, 22, 25]
# listas = [-5, -3, -100]

maxas = listas[0]
for elem in listas:
    if elem > maxas:
        maxas = elem
print(maxas)

# patikrinti ar nors vienas elementas dalinasi iš 5
flag5 = False
flag3 = False

for elem in listas:
    if elem % 5 == 0:
        flag5 = True
    if elem % 3 == 0:
        flag3 = True
    if flag5 and flag3:
        print(elem)
        break

if flag5 and flag3:
    print("Bent vienas elementas dalinasi iš 5 ir bent vienas iš 3.")