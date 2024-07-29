
daliklis = 0

try:
    res = 100 / daliklis
except (ZeroDivisionError):
    print("Dalyba iš 0 negalima!")
else:
    print(res)

while True:
    user_input = input("Įveskite skaičių: ")
    try:
        float_skaicius = float(user_input)
        print(f"Įvestas skaičius: {float_skaicius}")
        break
    except ValueError:
        print("Turite įvesti skaičių!")
    finally:
        print("FINALLY")