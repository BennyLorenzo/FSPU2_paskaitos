# 1. rasti kiek išviso įvarčių buvo įmušta
# 2. rasti kiek įvarčių įmušė vartotojo įvesta komanda
# 3. kuri komanda įmušė daugiausiai įvarčių namuose per 1 rungtynes
# 4. rasti statistinius duomenis pagal savo sugalvotus kriterijus

######## čia nieko nereikia liesti
stats = open("futbolas.csv", mode="r", encoding='utf-8').readlines()
stats = [line.strip().split(";") for line in stats]
stats = [[nk, *res.split(":"), sk] for d, nk, res, sk, v in stats]
stats = [[nk, int(res1), int(res2), sk] for nk, res1, res2, sk in stats]

######## nuo čia rašom savo kodą
# bus atspausdintos tik pirmos 5 eilutės susipažinimui su duomenimis
print(stats[:12]) # printą galiom užkomentuoti ar ištrinti, susipažinę

# 1
visi_ivarciai = sum([sum([ivartis1, ivartis2]) for komanda1, ivartis1, ivartis2, komanda2 in stats])
print("Visi įmušti įvarčiai:",visi_ivarciai)

# 2
ivesta_komanda = "Šiauliai"
komandos_ivarciai = 0
for komanda1, ivartis1, ivartis2, komanda2 in stats:
    if ivesta_komanda in komanda1:
        komandos_ivarciai += ivartis1
    elif ivesta_komanda in komanda2:
        komandos_ivarciai += ivartis2
print(f'Komandos {ivesta_komanda} įmušti įvarčiai: {komandos_ivarciai}')

# 3
daugiausia_ivarciu_namuose = 0
daugiausiai_ivarciu_namuose_komanda = ""
for komanda1, ivartis1, ivartis2, komanda2 in stats:
    if ivartis1 > daugiausia_ivarciu_namuose:
        daugiausia_ivarciu_namuose = ivartis1
        daugiausiai_ivarciu_namuose_komanda = komanda1[:-1]
print(f"Daugiausia įvarčių namuose: {daugiausia_ivarciu_namuose}, įmušo {daugiausiai_ivarciu_namuose_komanda}.")