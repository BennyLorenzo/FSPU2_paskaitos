from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Projektas)
visos_eilutes = query.all()

for eilute_o in visos_eilutes:
    print(eilute_o)

visos_eilutes = session.query(Projektas).all()

for eilute_o in visos_eilutes:
    print(eilute_o.kaina, eilute_o.pavadinimas,"ID",eilute_o.id,eilute_o.sukurimo_data)