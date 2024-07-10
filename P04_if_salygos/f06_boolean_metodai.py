miestas1 = 'Vilnius'
miestas2 = 'Kaunas'

# .istitle() - tikrina, ar string prasideda iš didžiosios raidės
print(miestas1.istitle())

# .isupper() - tikrina, ar string sudarytas iš didžiųjų raidžių
print(miestas1.isupper())

# .startswith() - tikrina, ar string prasideda iš nurodyto elemento (gali būti tuple)
print(miestas1.startswith(('V', 'K')))
print(miestas2.startswith(('V', 'K')))

print(miestas1.islower())

listas = ['vasaris', 'sausis', 'Vilnius', 'Kaunas','balandis','Panevėžys','45']
menesiai = []
miestai = []
print('Pirmas pratimas:')
for item in listas:
    if item.istitle():
        miestai.append(item)
    elif item.islower():
        menesiai.append(item)

print(menesiai, miestai)

# PRATIMAS 2
listas = [
'gegužė',
'vasaris',
'sausis',
'Vilnius',
'Kaunas',
'balandis',
'Panevėžys',
'LTU',
'LR',
'UK',
'10000',
'1973',
]
menesiai = []
miestai = []
santrumpos = []
kita = []

print('Antras pratimas:')
for item in listas:
    if (item.isupper()):
        santrumpos.append(item)
    elif (item.istitle()):
        miestai.append(item)
    elif (item.islower()):
        menesiai.append(item)
    else:
        kita.append(item)
print(santrumpos, miestai, menesiai, kita)