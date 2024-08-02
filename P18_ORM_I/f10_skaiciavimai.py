from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

# visos_eilutes = session.query(Projektas).all()
#
# for eilute_obj in visos_eilutes:
#     print(eilute_obj)

kainu_suma = session.query(func.sum(Projektas.kaina)).scalar()
print(kainu_suma)

kainu_vidurkis = session.query(func.avg(Projektas.kaina)).scalar()
print(kainu_vidurkis)

maziausia_kaina = session.query(func.min(Projektas.kaina)).scalar()
print(maziausia_kaina)

didziausia_kaina = session.query(func.max(Projektas.kaina)).scalar()
print(didziausia_kaina)