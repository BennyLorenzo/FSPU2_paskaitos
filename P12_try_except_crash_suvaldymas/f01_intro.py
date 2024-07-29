
while True:
    ivestis = input("Įveskite sveiką skaičių: ")
    try:
        skaicius = int(ivestis)
        res = skaicius / 2
        print(res)
        break
    except:
        print("Įveskite sveiką skaičių!")

print("Programa tęsia darbą.")