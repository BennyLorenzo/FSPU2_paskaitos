skaicius1 = 100
skaicius2 = 500
skaicius3 = 100

if skaicius1 < skaicius2:
    print("skaicius1 yra mažesnis, nei skaicius2")

if skaicius2 < skaicius1:
    print("skaicius2 yra mažesnis, nei skaicius1") # print neįvyks

if skaicius1 > skaicius2:
    print("skaicius1 yra didesnis, nei skaicius2")
else:
    print("skaicius1 nėra didesnis, nei skaicius2")

if (skaicius1 % 2) == 0:
    print(skaicius1, "skaičius lyginis")
else:
    print(skaicius1, "skaičius nelyginis")

if (skaicius2 % 2) == 0:
    print(skaicius2, "skaičius lyginis")
elif (skaicius2 % 3) == 0:
    print(skaicius2, "dalinasi iš 3")
elif (skaicius2 % 5) == 0:
    print(skaicius2, "dalinasi iš 5")
else:
    print(skaicius2, "nesidalina iš 2, 3, 5")

if skaicius2 > 10:
    print(skaicius2, "daugiau už 10")
elif skaicius2 > 100:
    print(skaicius2, "daugiau už 100")
elif skaicius2 > 200:
    print(skaicius2, "daugiau už 200")
else:
    print(skaicius2, "mažesnis arba lygus 10")
