from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

visos_eilutes = session.query(Projektas).all()

print("Nesurikiuotos eilutės:")
for eilute_obj in visos_eilutes:
    print(eilute_obj)

print("-------------------------")

print("Surikiuotos eilutės pagal pavadinimą:")
surikiuotos_eilutes = session.query(Projektas).order_by(Projektas.pavadinimas)
for eilute_obj in surikiuotos_eilutes:
    print(eilute_obj)

print("-------------------------")

print("Surikiuotos eilutės pagal kainą (didėjimo tvarka):")
surikiuotos_eilutes = session.query(Projektas).order_by(Projektas.kaina)
for eilute_obj in surikiuotos_eilutes:
    print(eilute_obj.kaina,eilute_obj.pavadinimas)

print("-------------------------")

print("Surikiuotos eilutės pagal kainą:")
surikiuotos_eilutes = session.query(Projektas).order_by(Projektas.kaina)
for eilute_obj in surikiuotos_eilutes:
    print(eilute_obj.kaina,eilute_obj.pavadinimas)