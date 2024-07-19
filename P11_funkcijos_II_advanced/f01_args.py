
# * - supakavimas

def funkcija(*args):
    print(args, type(args))

funkcija()
funkcija("Hello")
funkcija("Hello","World",2024,"liepa",19)

def spausdink_viska_didziosiom(*args):
    for stringy in args:
        print(stringy.upper())

spausdink_viska_didziosiom("hello","bro","what's","up")

def sudaugink_visus_is_vieno(daugiklis, *args):
    if len(args) == 0:
        print("Neturime ką sudauginti.")
    for elem in args:
        print(daugiklis * elem)

sudaugink_visus_is_vieno(2,5,4,10,5,7,8)

def sudaugink_visus_is_vieno_i_list(daugiklis, *args, info=False):
    listas = []
    for elem in args:
        listas.append(daugiklis * elem)
    if info:
        print(f"Daugiklis: {daugiklis}, args: {args}, rezultatas: {listas}")
    return listas

print(sudaugink_visus_is_vieno_i_list(2))
print(sudaugink_visus_is_vieno_i_list(9,10,45,48,99))
sudaugink_visus_is_vieno_i_list(9,10,45,48,99,info=True)