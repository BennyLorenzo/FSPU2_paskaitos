# turi būti tik funkcijos, be funkcijos iškvietimų

# 1 užduotis
def hello_name(name, count):
    for i in range(count):
        print(f"Hello, {name}!")

# 2 užduotis
def lyginis_nelyginis_print(number):
    if number % 2 == 0:
        print(f"Skaičius {number} yra lyginis.")
    else:
        print(f"Skaičius {number} yra nelyginis.")

# 3 užduotis
def lyginis_nelyginis_return(number):
    if number % 2 == 0:
        res = f"Skaičius {number} yra lyginis."
    else:
        res = f"Skaičius {number} yra nelyginis."
    return res

# 4 užduotis
def ar_lyginis(number):
    if number % 2 == 0:
        return True
    else:
        return False

# papildomos funkcijos

# kalkuliatorius
def calculator(number1, operation, number2):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2
    else:
        return "Operacija negalima."

# add to list
list = []
def add_to_list(item):
    list.append(item)
    return list

# loop in loop
def looping_over(letters, numbers):
    for letter in letters:
        for number in range(1,numbers+1):
            print(letter, number)

# 5 užduotis
def sudek(skaicius1,skaicius2):
    return skaicius1 + skaicius2
def atimk(skaicius1, skaicius2):
    return skaicius1 - skaicius2
def daugink(skaicius1, skaicius2):
    return skaicius1 * skaicius2
def dalink(skaicius1, skaicius2):
    return skaicius1 / skaicius2

# 6 užduotis
def skaiciuok_palukanas(indelis, metines_palukanos, menesiu_skaicius):
    procentas = metines_palukanos / 100
    return indelis + (indelis * procentas) * menesiu_skaicius / 12

# 7 užduotis
def amortizuok(daikto_verte, metu_skaicius, procentas):
    return daikto_verte - (metu_skaicius * (daikto_verte * procentas / 100))