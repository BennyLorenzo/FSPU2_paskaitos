def print_kwargs(**kwargs):
    print(kwargs,type(kwargs))
    print(kwargs.items())

print_kwargs(miestas="Vilnius",salis="Lietuva",metai=2024)

# be kwargs
listas_duom = ['sausis', 'vasaris', 'kovas']
print("a","b","c",sep="///",end=" & \n")

def print_list(listas, skirtukas=None, eilutes_pabaiga="\n"):
    if not skirtukas:
        skirtukas = " "
    for elem in listas:
        print(elem,"mėn.",sep=skirtukas,end=eilutes_pabaiga)

print_list(listas_duom,"----"," & ")
print()

# su kwargs
def print_listas_kwargs(listas, **kwargs):
    for elem in listas:
        print(elem,"mėn.", **kwargs)

print_listas_kwargs(listas_duom,sep="---",end="!!!")