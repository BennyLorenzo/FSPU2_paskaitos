sarasas = []
print(type(sarasas))
print(sarasas)

# duomenys sąrašui
men1 = "sausis"
men2 = "vasaris"

# .append() - prijungia naują elementą į sąrašo pabaigą
# Nieko negrąžina, tik padaro pakeitimą in-place

sarasas.append(men1)
print(sarasas)

sarasas.append(men2)
print(sarasas)

sarasas.append("kovas")
sarasas.append(2024)
print(sarasas)

# .insert() - prijungia naują elementą indeksu nurodytoje pozicijoje

sarasas.insert(1, "balandis")
sarasas.insert(2,"birzelis")
sarasas.insert(-1, "balandis")
print(sarasas)

# .remove() - ištrina pirmą rastą objektą
sarasas.remove("balandis")
print(sarasas)

# .pop() - pašalina paskutinį objektą sąraše, arba pagal indeksą
sarasas.pop()
print(sarasas)

# šalinamą elementą galim priskirti kintamajam
ismestas = sarasas.pop(1)
print(ismestas)
print(sarasas)

# del - python komanda trinti
del sarasas[-1]
print(sarasas)

# indeksai listuose
print(sarasas[1])
print(sarasas[1:])

print((sarasas))
sarasas[0] = "lapkritis"
print(sarasas)

# string negalima keisti pagal indeksą
# stringas = "ABCDEF"
# stringas[0] = "W"
# print(stringas)