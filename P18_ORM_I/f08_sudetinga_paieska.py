from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

pavadinimo_salyga = "ga%"
kainos_lubos = 800.0
filtruoti_eilutes_objektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike(pavadinimo_salyga),
                                                             Projektas.kaina <= kainos_lubos).all()
for eil in filtruoti_eilutes_objektai:
    print(eil.kaina, eil.pavadinimas)
print('---------------------------')
# OR sąlygos
pavadinimo_salyga = "%inc%"
maziausia_kaina = 1000.0

filtruoti_eilutes_objektai = session.query(Projektas).filter((Projektas.pavadinimas.ilike(pavadinimo_salyga))
                                                             |(Projektas.kaina >= maziausia_kaina)).all()

for eil in filtruoti_eilutes_objektai:
    print(eil.kaina, eil.pavadinimas)

