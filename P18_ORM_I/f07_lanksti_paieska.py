from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

# for eilute_obj in session.query(Projektas).all():
#     print(eilute_obj)

kainos_lubos = 610
filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.kaina <= kainos_lubos).all()
for eil in filtruoti_eilutes_objektai:
    print(eil.kaina, eil.pavadinimas)

# .ilike() palaiko kaukes, .like(<paieskos_fraze>)
paieskos_fraze = "S%" # visi pavadinimai, prasidedantys S, po to seka bet kokie simboliai
filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike(paieskos_fraze)).all()
for eil in filtruoti_eilutes_objektai:
    print(eil)
print('------------------------------')
paieskos_fraze = "%Inc%"
filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike(paieskos_fraze)).all()
for eil in filtruoti_eilutes_objektai:
    print(eil)

# panaudojame vartotojo įvestį
ivestis = input("Įveskite pavadinimo pradžią: ")
paieskos_fraze = f"%{ivestis}%"
filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike(paieskos_fraze)).all()
for eil in filtruoti_eilutes_objektai:
    print(eil)
