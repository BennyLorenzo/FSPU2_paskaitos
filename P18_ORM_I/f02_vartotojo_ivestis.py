from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

print("Įveskite projektą:")
pavadinimas = input("Pavadinimas: ")
kaina = float(input("Kaina: "))

eilute_o = Projektas(pavadinimas,kaina)
session.add(eilute_o)
session.commit()

query = session.query(Projektas)
visos_eilutes = query.all()
for eilute_o in visos_eilutes:
    print(eilute_o)

# užklausa sutrumpintai
visos_eilutes = session.query(Projektas).all()

#printinam kiekvieno objekto laukus atskirai
for eilute_o in visos_eilutes:
    print(eilute_o.kaina, eilute_o.pavadinimas,"ID",eilute_o.id,eilute_o.sukurimo_data)
