duomenu_listas = [1, 10, 2, 20, 3, 30, 4, 40]

res = [elem for elem in duomenu_listas if elem < 10]
print(res)

res = [elem for elem in duomenu_listas if elem % 2 != 0]
print(res)

res = sum([elem for elem in duomenu_listas if elem < 10])
print(res)

res = sum([elem**2 for elem in duomenu_listas if elem % 2 == 0])
print(res)

res = [elem for elem in duomenu_listas[:3] if elem < 10]
print(res)

res = [elem ** 2 for elem in duomenu_listas][:5]
print(res)

raides = ['A', 'B', 'C']
skaiciai = ['1', '2', '3', '4']

for raid in raides:
    for skaic in skaiciai:
        print(raid+skaic)

res = [raid+skaic for raid in raides for skaic in skaiciai]
print(res)

res = [elem if elem % 2 == 0 else "nelyginis" for elem in duomenu_listas]
print(res)

res = [elem for elem in duomenu_listas if elem % 10 == 0]
print(res)