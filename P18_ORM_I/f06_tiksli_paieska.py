from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

# kad pakeisti konkrečios eilutės duomenis, pasiimame eilutės objektą į kintamąjį

for eilute_obj in session.query(Projektas).all():
    print(eilute_obj)

# vietoj .all() galim naudoti .first() - pirmas rezultatas, .one() - vienas rezultatas
eiluciu_obj = session.query(Projektas).filter_by(kaina=1010).all()
print(eiluciu_obj)

from sqlalchemy.exc import MultipleResultsFound
try:
    eiluciu_obj = session.query(Projektas).filter_by(kaina=1010).one()
except MultipleResultsFound:
    print("Egzistuoja ne viena tokia eilutė")

paieskos_fraze = "Ermitažas"

try:
    eiluciu_obj = session.query(Projektas).filter_by(pavadinimas=paieskos_fraze).one()
    print("Rastas vienas objektas")
except MultipleResultsFound:
    eiluciu_obj = session.query(Projektas).filter_by(pavadinimas=paieskos_fraze).all()
    print("Egzistuoja ne viena tokia eilutė")
print(eiluciu_obj)


