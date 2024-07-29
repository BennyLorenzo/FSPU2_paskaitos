
# iterators and iterables

# `__iter__` iteruojamasis, turi šį metodą, grąžina iteratorių
# `__next__` iteratorius, turi šį metodą, suteikia galimybę perrinkti po vieną elementą su next()

listas = ['sausis','kovas','vasaris']

for elem in listas: # for automatiškai sukuria iteratorių ir kviečia next()
    print(elem)

# iteratoriai reaguoja į next() funkciją
# next(listas) - listas nėra iteratorius

# listas yra iterable ir gali atiduoti iteratorių
iteratorius = iter(listas)

# print(dir(iteratorius)) - turi __next__
print(next(iteratorius))
print(next(iteratorius))
print(next(iteratorius))

iteratorius = iter(listas)
while True:
    try:
        elem = next(iteratorius)
        print(elem)
    except StopIteration:
        print("Nebėra iteratorių!")
        break
