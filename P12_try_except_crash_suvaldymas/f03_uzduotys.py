# 1
def skaiciaus_dalyba(skaicius, daliklis):
    try:
        res = int(skaicius) / int(daliklis)
        print(res)
    except ZeroDivisionError:
        print("Dalyba iš 0 negalima!")
    except ValueError:
        print("Įveskite sveikus skaičius.")

skaicius = input("Įveskite skaičių: ")
daliklis = input("Įveskite daliklį: ")
skaiciaus_dalyba(skaicius, daliklis)

# 2
while True:
    user_input = input("Įveskite skaičių: ")
    try:
        skaicius = float(user_input)
        print(f"Įvestas skaičius: {skaicius}")
        break
    except ValueError:
        print("Turite įvesti skaičių!")