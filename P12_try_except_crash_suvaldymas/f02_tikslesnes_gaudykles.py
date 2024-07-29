
while True:
    ivestis = input("Įveskite sveiką skaičių: ")
    if ivestis == 'q':
        break
    ivestis2 = input("Įveskite daliklį: ")
    if ivestis2 == 'q':
        break
    try:
        skaicius = int(ivestis)
        daliklis = int(ivestis2)
        res = skaicius / daliklis
        print(res)
        break
    except ValueError:
        print("Įveskite sveiką skaičių!")
    except ZeroDivisionError:
        print("Dalyba iš nulio negalima!")