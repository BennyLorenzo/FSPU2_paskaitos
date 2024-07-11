# .range() - returnina nurodytą skaičių diapozoną, naudojama su for ciklu

res = range(9)
print(res) # range(0, 9) - nematom visų skaičių

for skaicius in range(9):
    print(skaicius ** 2)

for i in range(3):
    print("Hello!")

print(*range(9)) # išpakuojame range
print(*range(4,9))
print(*range(10, 18, 2))
print(*range(18, 10, -1))