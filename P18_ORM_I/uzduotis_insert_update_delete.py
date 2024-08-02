from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas
import datetime

Session = sessionmaker(bind=engine)
session = Session()
visos_eilutes = session.query(Projektas).all()

#printinam kiekvieno objekto laukus atskirai
for eilute_o in visos_eilutes:
    print(eilute_o.kaina, eilute_o.pavadinimas,"ID",eilute_o.id,eilute_o.sukurimo_data)
#
# print("Įveskite projektą:")
# pavadinimas = input("Pavadinimas: ")
# kaina = float(input("Kaina: "))
#
# eilute_o = Projektas(pavadinimas,kaina)
# session.add(eilute_o)
# session.commit()

#printinam kiekvieno objekto laukus atskirai
# for eilute_o in visos_eilutes:
#     print(eilute_o.kaina, eilute_o.pavadinimas,"ID",eilute_o.id,eilute_o.sukurimo_data)
#
# eilutes_id = 36
# eilutes_obj = session.query(Projektas).get(eilutes_id)
# print("------pagautas objektas, eilutė-----")
# print(eilutes_obj)
#
# eilutes_obj.pavadinimas = "Atnaujintasis Projektas LLC"
# eilutes_obj.kaina = 150_000
# eilutes_obj.sukurimo_data = datetime.datetime(2020,10,20,14,0,0)
# print(eilutes_obj)
#
# session.delete(eilutes_obj)
# session.commit()
#
# print(eilutes_obj)

