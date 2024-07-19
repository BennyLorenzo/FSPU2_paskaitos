# 1 užduotis
zodynas = {}
while True:
    user_input = input('Įveskite raktą ir reikšmę, atskirtus tarpu (norint išeiti, įveskite "break"): ')
    user_data = user_input.split(" ")
    if user_data[0] == 'break':
        break
    else:
        zodynas[user_data[0]] = user_data[1]
    print("Žodyno elementai: ")
    for key, value in zodynas.items():
        print(key, value)

    quit = input('Jei norite išeiti, paspauskite "q": ')
    if quit == 'q':
        print("Viso gero!")
        break

# 2 užduotis
pajamos = []
islaidos = []
while True:
    print("Įvedimo pasirinkimai:\n"
    "1 - įvesti pajamas\n"
    "2 - įvesti išlaidas\n"
    "3 - išeiti iš programos\n"
    "4 - ataskaita\n")
    user_input = input("Įvedimas: ")
    if user_input == "1":
        pajamos_input = input("Įveskite pajamas: ")
        pajamos.append(float(pajamos_input))
        print(f'Visos pajamos: {pajamos}')
    elif user_input == "2":
        islaidos_input = input("Įveskite išlaidas: ")
        islaidos.append(float(islaidos_input))
        print(f'Visos išlaidos: {islaidos}')
    elif user_input == "3":
        print("Programa baigė darbą.")
        break
    elif user_input == "4":
        print(f'Pajamų suma: {round(sum(pajamos), 2)}\n'
        f'Išlaidų suma: {round(sum(islaidos), 2)}\n'
        f'Balansas: {round(sum(pajamos) - sum(islaidos), 2)}\n')
    else:
        print("Įveskite vieną iš įvedimo pasirinkimų!")

# 4 užduotis
for number in range(1,101):
    print(number)
    if number == 20:
        break
print("--------------")

for number in range(1,101):
    if number < 11:
        continue
    print(number)
print("--------------")

for number in range(1,101):
    if number % 2 == 0:
        continue
    if number > 19:
        break
    print(number)

# 5 užduotis
stringas = "Šiame stringe yra daug balsių aeouioiuioiuyoo"
balses = "aeiouy"
kaupiklis = []
for symbol in stringas:
    if symbol in balses:
        kaupiklis.append(symbol)
    if len(kaupiklis) == 7:
        print("Sukauptos balsės:",kaupiklis)
        break

# 6 užduotis
sum = 0
while True:
    user_input = float(input("Įveskite skaičių (jei skaičius neigiamas, programa baigs darbą): "))
    if user_input < 0:
        print('Įvestų skaičių suma: ',sum)
        print('Programa baigė darbą.')
        break
    sum += user_input

# 7 užduotis
pin = '3333'
guesses = 0
limit = 5
numbers = ['0','1','2','3','4','5','6','7','8','9']
while True:
    user_input = input("Įveskite keturių skaitmenų PIN kodą: ")
    guesses += 1
    for symbol in user_input:
        if symbol not in numbers or len(user_input) > 4:
            guesses -= 1
            print("Įveskite keturis skaitmenis.")
            break
    if user_input == pin:
        print(f"Teisingas PIN kodas, seifas atsidarė. Teisingą kodą įvedėte iš {guesses}-o karto.")
        break
    if guesses == limit:
        print("Pasiektas limitas, PIN įvedimas blokuojamas.")
        break

# 8 užduotis
operations = []
while True:
    print('Pasirinkite operaciją: \n'
          '1 - sudėtis\n'
          '2 - atimtis\n'
          '3 - daugyba\n'
          '4 - dalyba\n'
          '5 - skaičių sekos spausdinimas (nuo, iki)\n'
          '6 - išeitis iš programos\n'
          )
    user_input = input("Įvestis: ")
    if user_input == "1":
        operation_input = input("Įveskite du skaičius, kuriuos norite sudėti, atskirtus tarpu: ")
        operation_items = operation_input.split(" ")
        operations.append(operation_items[0]+" + "+operation_items[1])
        print(f'{operation_items[0]} + {operation_items[1]} = {float(operation_items[0]) + float(operation_items[1])}');
    elif user_input == "2":
        operation_input = input("Įveskite du skaičius, kuriuos norite atimti, atskirtus tarpu: ")
        operation_items = operation_input.split(" ")
        operations.append(operation_items[0] + " - " + operation_items[1])
        print(f'{operation_items[0]} - {operation_items[1]} = {float(operation_items[0]) - float(operation_items[1])}');
    elif user_input == "3":
        operation_input = input("Įveskite du skaičius, kuriuos norite sudauginti, atskirtus tarpu: ")
        operation_items = operation_input.split(" ")
        operations.append(operation_items[0] + " * " + operation_items[1])
        print(f'{operation_items[0]} * {operation_items[1]} = {float(operation_items[0]) * float(operation_items[1])}');
    elif user_input == "4":
        operation_input = input("Įveskite du skaičius, kuriuos norite padalinti, atskirtus tarpu: ")
        operation_items = operation_input.split(" ")
        operations.append(operation_items[0] + " / " + operation_items[1])
        print(f'{operation_items[0]} / {operation_items[1]} = {float(operation_items[0]) / float(operation_items[1])}');
    elif user_input == "5":
        operation_input = input("Įveskite du skaičius, pagal kuriuos bus spausdinama skaičių seka, atskirtus tarpu: ")
        operation_items = operation_input.split(" ")
        if int(operation_items[0]) > int(operation_items[1]):
            print("Pirmas skaičius turi būti mažesnis, nei antras skaičius.")
            continue
        operations.append("nuo: " + operation_items[0] + ", iki:  " + operation_items[1])
        print("Skaičių seka: ")
        for skaicius in range(int(operation_items[0]),int(operation_items[1])+1):
            print(skaicius)
    elif user_input == "6":
        print("Įvykdytos operacijos: ",operations)
        print("Programa baigė darbą.")
        break
    else:
        print("Neteisingai įvesta operacija.")

# 9 užduotis
pajamos = []
islaidos = []

while True:
    print("1. Įvesti pajamas\n"
    "2. Įvesti išlaidas\n"
    "3. Atspausdinti pajamų eilutes\n"
    "4. Atspausdinti išlaidų eilutes\n"
    "5. Atspausdinti statistiką\n"
    "q - Išeiti\n")
    menu_input = input("Įveskite pasirinkimą: ")
    if menu_input == "1":
        user_input = input("Įveskite pajamų mėnesio skaičių, kategoriją ir sumą, atskirtus kableliais: ")
        user_input = user_input.split(",")
        pajamos.append(user_input)
    elif menu_input == "2":
        user_input = input("Įveskite išlaidų mėnesio skaičių, kategoriją ir sumą, atskirtus kableliais: ")
        user_input = user_input.split(",")
        islaidos.append(user_input)
    elif menu_input == "3":
        print("Pajamų eilutės:")
        for menesis, kategorija, suma in pajamos:
            print(f'Mėnesis: {menesis}, kategorija: {kategorija}, suma: {suma}')
    elif menu_input == "4":
        print("Išlaidų eilutės:")
        for menesis, kategorija, suma in islaidos:
            print(f'Mėnesis: {menesis}, kategorija: {kategorija}, suma: {suma}')
    elif menu_input == "5":
        visos_pajamos = 0
        visos_islaidos = 0
        for menesis, kategorija, suma in pajamos:
            visos_pajamos += float(suma)
        for menesis, kategorija, suma in islaidos:
            visos_islaidos += float(suma)
        print(f"Visos pajamos: {visos_pajamos}\n"
              f"Visos išlaidos: {visos_islaidos}\n"
              f"Balansas: {visos_pajamos - visos_islaidos}")
    elif menu_input == "q":
        print("Programa baigė darbą.")
        break
    else:
        print("Tokios operacijos nėra.")