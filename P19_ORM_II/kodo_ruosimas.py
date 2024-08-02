from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

def paieska():
    ivestis = input("Įveskite pavadinimo pradžią: ")
    paieskos_fraze = f"{ivestis}%"
    filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike(paieskos_fraze)).all()

    for eil in filtruoti_eilutes_objektai:
        print(eil)

def prideti():
    print("Įveskite projektą:")
    pavadinimas = input("Pavadinimas: ")
    kaina = float(input("Kaina: "))

    eilute_o = Projektas(pavadinimas,kaina)
    session.add(eilute_o)
    session.commit()

prideti()