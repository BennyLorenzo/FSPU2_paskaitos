# 1 užd
# Leiskite vartotojui įvesti vartotojo vardą ir amžių.
# Išspausdinkite, ar vartotojas gali patekti į internetinį kazino, ar ne.
# 21 metai yra amžiaus riba.
# (sprendimas ~7 eilutės)
print('1 užduotis:')
user_input = input("Įveskite savo vardą ir amžių, atskirtus tarpu: ")
user_data_list = [user_input.split(" ")]
for vardas, amzius in user_data_list:
    print(f'Sveiki, {vardas}, galite patekti į kazino.') if int(amzius) >= 21 else print(f'Deja, {vardas}, esate per jauna(-s) patekti į kazino.')

# 2 užd
# 1-os užduoties sudėtingesnis variantas.
# Sukurkite privilegijuotų vartotojų sąrašą(list) su vardais,
# išspausdinkite konkretų pranešimą su asmeniniu pasveikinimu,
# jei naudotojas yra privilegijuotas, arba tik "Sveiki atvykę"
# kitu atveju.
# (sprendimas ~11 eilučių)
print('2 užduotis:')
vip_list = ['Baranis', 'Henyte', 'Timocha']
user_input = input("Įveskite savo vardą ir amžių, atskirtus tarpu: ")
user_data_list = [user_input.split(" ")]
for vardas, amzius in user_data_list:
    if int(amzius) >= 21:
        if (vardas in vip_list):
            print(f'Sveiki, vadeiva {vardas}, galite patekti į kazino.')
        else:
            print(f'Sveiki, {vardas}, galite patekti į kazino.')
    else:
        print(f'Deja, {vardas}, esate per jauna(-s) patekti į kazino.')

# 3 užd
# Leiskite naudotojui įvesti du skaičius. Išspausdinkite, kuris
# iš jų didesnis už kitą, arba ar jie lygūs.
# (sprendimas ~8 eilutės)
print('3 užduotis')
user_input = input("Įveskite du skaičius, atskirtus tarpu: ")
numbers = [user_input.split(" ")]
for number1, number2 in numbers:
    if int(number1) > int(number2):
        print(f'{number1} yra daugiau, nei {number2}.')
    elif int(number2) > int(number1):
        print(f'{number2} yra daugiau, nei {number1}.')
    else:
        print('Skaičiai lygūs.')

# 4 užd
# Parašykite nedidelę skaičiuotuvo programą, kuri leistų naudotojui
# įvesti du skaičius ir norimos aritmetinės operacijos simbolį(+-/*).
# Programa atlieka operaciją ir atspausdina rezultatą.
# (sprendimas ~13-17 eilučių)
print('4 užduotis')
user_input = input("Įveskite aritmetinę operaciją su tarpais (pvz. 2 + 2, 3 * 3): ")
operation_items = [user_input.split(" ")]
for skaicius1, operacija, skaicius2 in operation_items:
    if operacija == "+":
        print(f'{user_input} = {float(skaicius1)+float(skaicius2)}');
    elif operacija == "-":
        print(f'{user_input} = {float(skaicius1)-float(skaicius2)}');
    elif operacija == "/":
        print(f'{user_input} = {float(skaicius1)/float(skaicius2)}');
    elif operacija == "*":
        print(f'{user_input} = {float(skaicius1)*float(skaicius2)}');
    else:
        print('Tokia operacija negalima.')

# 5a užd
# Programa paklausia vartotojo, koks dabar mėnesis, priima įvestį
# nustato kokiam metų laikui priklauso įvestas mėnesis ir atprintina metų
# laiko pavadinimą ir sakinį apibūdinantį tą metų laiką
# pvz: vartotojas įveda "birželis", programos printai:
# "dabar yra vasara", "vasarą būna labai karšta"
# printai daromi atskirose eilutėse
# hint - sudarom listus pvz. pavasaris = ["kovas", "balandis", "gegužė"] ir tt
# naudojam in
# (sprendimas ~20 eilučių)
# 5b užd
# papildomas printas jeigu tai yra paskutinis
# metų laiko mėnuo
print('5 užduotis')
ziema = ["gruodis","sausis","vasaris"]
pavasaris = ["kovas","balandis","gegužė"]
vasara = ["birželis","liepa","rugpjūtis"]
ruduo = ["rugsėjis","spalis","lapkritis"]
paskutiniai_metu_laiku_menesiai = ["vasaris", "gegužė", "rugpjūtis", "lapkritis"]
menesis = input("Įveskite norimą mėnesį: ")
if menesis in ziema:
    print(f'{menesis.title()} yra žiemą.')
    print('Žiemą gan šaltoka.')
elif menesis in pavasaris:
    print(f'{menesis.title()} yra pavasarį.')
    print('Pavasarį žydi gėlės.')
elif menesis in vasara:
    print(f'{menesis.title()} yra vasarą.')
    print('Vasarą galima maudytis.')
elif menesis in ruduo:
    print(f'{menesis.title()} yra rudenį.')
    print('Rudenį krenta lapai.')
else:
    print("Įvedėte ne mėnesį.")
print(f'{menesis.title()} yra paskutinis metų laiko mėnuo.') if menesis in paskutiniai_metu_laiku_menesiai else None