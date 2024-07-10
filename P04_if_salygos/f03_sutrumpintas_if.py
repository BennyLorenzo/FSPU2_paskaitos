skaicius1 = 120

if skaicius1 < 0:
    res = "skaičius yra neigiamas"
else:
    res = "skaičius yra teigiamas"
print(res)

res = "skaičius yra neigiamas" if skaicius1 < 0 else "skaičius yra teigiamas"
print(res)

skaiciai = [1, 2, 4, 5, 10]
lyginiai = []

for skaicius in skaiciai:
    if (skaicius % 2) == 0:
        lyginiai.append(skaicius)

print(lyginiai)

lyginiai = []
for skaicius in skaiciai:
    lyginiai.append(skaicius) if (skaicius % 2) == 0 else (False)
print(lyginiai)