menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']

for men in menesiai:
    print(men)
    print(men.upper())

print("-------------")

skaiciai = [10, 7, 50, 111]

for number in skaiciai:
    print(number * 100)

print("-------------")

suma = 0
for number in skaiciai:
        suma += number
print(suma)

print("-------------")

# sudėti kas antrą skaičių
suma = 0
for number in skaiciai[1::2]:
    print(number)
    suma += number
print(suma)