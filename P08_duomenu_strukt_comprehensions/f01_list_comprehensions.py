# list comprehensions yra naujo listo sudarymo operacija
# naudojant for ir specialią sintaksę

duomenu_listas = [1, 10, 2, 20, 3, 30, 4, 40]
kaupiklis = [elem for elem in duomenu_listas] # [rezultatas, ciklas]
print(kaupiklis)

kaupiklis2 = [elem * 9 for elem in range(1,4)]
print(kaupiklis2)

kaupiklis3 = [[elem, elem**2] for elem in range(1,6)]
print(kaupiklis3)

# 1 užduotis
comprehensist = [[elem, elem**2, elem**3] for elem in range(1,6)]
print(comprehensist)

# 2 užduotis
comprehensist2 = {elem:[elem**2,elem**3] for elem in range(1,6)}
print(comprehensist2)