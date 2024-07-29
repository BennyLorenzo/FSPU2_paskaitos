
# generatoriai - tai jau suformuoti iteratoriai, reaguojantys į next().
# Jie kuriami kaip funkcijos, tačiau naudoja yield wietoje return.
# Generatorius gali būti sustabdytas ir po to paleistas tęsti darbą.

# generatorius galės skaičiuoti iki stop'o ir sustoti

def skaiciuok_iki(stop):
    skaitliukas = 0
    while skaitliukas <= stop:
        yield skaitliukas
        skaitliukas += 1

generatorius = skaiciuok_iki(4)
print(next(generatorius))
print(next(generatorius))
# input()
print(next(generatorius))

for i in skaiciuok_iki(10):
    print(i)


# generator comprehension
listas = [(x * 999 / 7000) ** 2 for x in range(10_000, 10_500)]
print(listas[:5])

# generator comprehension, elementai generuojami po 1 taupant atmintį
# su galimybe generuoti porcijomis, sustabdyti

generatorius = ((x * 999 / 7000) ** 2 for x in range(10_000, 10_500))
print(generatorius)
print(next(generatorius))
print(next(generatorius))
print(next(generatorius))
print("---------------------")
# porcijomis po 5
for i in range(5):
    print(next(generatorius))

# Papildoma informacija
# *args, **kwargs - https://calmcode.io/course/args-kwargs/introduction
# dekoratoriai - https://calmcode.io/course/decorators/introduction
