# lambda - anoniminė funkcija, sutrumpinta sintaksė, neturi pavadinimo
# pagrinde lambda naudojama su kitom funkcijom, kurios priima lambda kaip argumentus

darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500],
    ['Adomas', 'direktorius', 3000]
]

surikiuoti_darbuotojai = sorted(darbuotojai)
print(surikiuoti_darbuotojai)

def grazink_index_2(listas):
    return listas[2]

print(grazink_index_2(darbuotojai))

surikiuoti_darbuotojai = sorted(darbuotojai,key=grazink_index_2) # funckija kaip parametras, pati nekviečiama
print(surikiuoti_darbuotojai)

surikiuoti_darbuotojai = sorted(darbuotojai, key=lambda listas: listas[1])
print(surikiuoti_darbuotojai)

surikiuoti_atlyginimus_mazejimo_tvarka = sorted(darbuotojai, key = lambda listas: listas[2], reverse=True)
print(surikiuoti_atlyginimus_mazejimo_tvarka)