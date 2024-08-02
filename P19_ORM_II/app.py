from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

def rodyk_visas_eilutes():
    visos_eilutes = session.query(Projektas).all()
    for eilute_o in visos_eilutes:
        print(eilute_o)

def paieska():
    ivestis = input("Įveskite pavadinimo pradžią: ")
    paieskos_fraze = f"{ivestis}%"
    filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike(paieskos_fraze)).all()

    for eil in filtruoti_eilutes_objektai:
        print(eil)

def ivesti_nauja_projekta():
    print("Įveskite projektą:")
    pavadinimas = input("Pavadinimas: ")
    kaina = float(input("Kaina: "))

    eilute_o = Projektas(pavadinimas,kaina)
    session.add(eilute_o)
    session.commit()

while True:
    print("---------------------\n"
          "1. Visi projektai\n"
          "2. Paieška\n"
          "3. Įvesti naują projektą\n"
          "...\n"
          "q. Išeiti iš programos\n"
          "---------------------")
    pasirinkimas = input(">>> ")

    if pasirinkimas == 'q':
        print("Programa baigė darbą.")
        break

    if pasirinkimas == '1':
        rodyk_visas_eilutes()

    elif pasirinkimas == '2':
        paieska()

    elif pasirinkimas == '3':
        ivesti_nauja_projekta()
