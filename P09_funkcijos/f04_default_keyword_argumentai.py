
def priimk_pacienta(pacientas,gydytojas="gyd. Pagalnutylenis",lydintysis=None):
    irasas_gyd_zurnale = f'Pacientas: {pacientas}, priėmė gydytojas: {gydytojas}'
    if lydintysis:
        irasas_gyd_zurnale += f', lydintysis: {lydintysis}'
    return irasas_gyd_zurnale

print(priimk_pacienta("Benny"))
print(priimk_pacienta("Benny","gyd. Pakeitenis"))
print(priimk_pacienta("Benny","gyd. Pakeitenis","mama"))

def paciento_priemimas(pacientas,gydytojas="gyd. Pagalnutylenis",paslauga_mokama=False):
    irasas_gyd_zurnale = f'Pacientas: {pacientas}, priėmė gydytojas: {gydytojas}'
    if paslauga_mokama:
        kaina = input("Įveskite sąskaitos sumą: ")
        irasas_gyd_zurnale += f'\nPrijungiama {kaina} sąskaita.'
    return irasas_gyd_zurnale

print(paciento_priemimas("Benny", paslauga_mokama=True))
