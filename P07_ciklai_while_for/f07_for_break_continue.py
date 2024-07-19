listas = ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']

for elem in listas:
    if elem == 'balandis':
        break
    print(elem)
    print("stringe", elem, "yra", len(elem),"raidės")

for elem in listas:
    if elem == 'sausis': # sausis praleidžiamas
        continue # grįžta į ciklo pradžią
    print(elem)
    print("stringe", elem, "yra", len(elem), "raidės")

listas = [34, 18, 2, 8, 30, 19, 5, 22, 25, 70]
print("------------------")
for elem in listas:
    if elem > 40:
        break
    print(elem)

print("------------------")
for elem in listas:
    if elem % 2 == 0:
        continue
    print(elem)
