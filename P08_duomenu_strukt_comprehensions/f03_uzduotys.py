# 1 užduotis
skaiciai = [7423, 8419, 5960, 9661, 8073, 5161, 7189, 9346, 8202, 7351, 9391, 9492, 8756, 9932, 5631]

# 1
print("Lyginių skaičių suma: ",sum([elem for elem in skaiciai if elem % 2 == 0]))

# 2
print("Didžiausias lyginis skaičius: ",max([elem for elem in skaiciai if elem % 2 == 0]))

# 3
print("Nelyginių skaičių suma: ",sum([elem for elem in skaiciai if elem % 2 != 0]))

# 4
print("Didžiausias nelyginis skaičius: ",max([elem for elem in skaiciai if elem % 2 != 0]))

# 5
print("Skaičių, kurie dalinasi iš 7, suma: ",sum([elem for elem in skaiciai if elem % 7 == 0]))


# 2 užduotis
stringai = ["apple", "angora", "banana", "berry", "cherry", "day", "date"]

# 1
prasideda_a = [symbol for symbol in stringai if symbol[0] == 'a']
print(prasideda_a)

# 2
prasideda_a_ir_d = [symbol for symbol in stringai if symbol[0] == 'a' or symbol[0] == 'd']
print(prasideda_a_ir_d)

# 3
ilgesni_nei_5 = [symbol for symbol in stringai if len(symbol) > 5]
print(ilgesni_nei_5)

# 4
ilgesni_nei_5_ir_prasideda_a = [symbol for symbol in stringai if symbol[0] == 'a' and len(symbol) > 5]
print(ilgesni_nei_5_ir_prasideda_a)

# 5
nesibaigia_a = [symbol for symbol in stringai if symbol[-1] != 'a']
print(nesibaigia_a)

# 3 užduotis
listukas = [[number, number**2, number**3] for number in range(1,9)]
print(listukas)

# 4 užduotis
darbuotojai = [
    ['Adomas', 'technikas', 1000],
    ['Romas', 'technikas', 1000],
    ['Kazys', 'technikas', 1200],
    ['Domas', 'vadybininkas', 1500],
    ['Valentas', 'vadybininkas', 1000],
    ['Bosas', 'direktorius', 1000]
]

# 1
tik_atlyginimai = sum([atlyginimas for vardas, pareigos, atlyginimas in darbuotojai if pareigos == "technikas"])
print("Technikų atlyginimai:",tik_atlyginimai)

# 2
tik_turciai = [elem for elem in darbuotojai if elem[2] > 1000]
print(tik_turciai)

# 3
tik_pareigos = list(set([pareigos for vardas, pareigos, atlyginimas in darbuotojai]))
print(tik_pareigos)

# 4
surikiuoti_vardai = [vardas for vardas, pareigos, atlyginimas in darbuotojai]
surikiuoti_vardai.sort()
count = 1
for vardas in surikiuoti_vardai:
    print(f'{count}. {vardas}')
    count += 1