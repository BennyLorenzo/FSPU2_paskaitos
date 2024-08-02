from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

# kad pakeisti konkrečios eilutės duomenis, pasiimame eilutės objektą į kintamąjį

for eilute_obj in session.query(Projektas).all():
    print(eilute_obj)

eilutes_id = 34
eilutes_obj = session.query(Projektas).get(eilutes_id)
print("------pagautas objektas, eilutė-----")
print(eilutes_obj)
# eilutes_obj.pavadinimas = "Sons and Akelis INC."
# eilutes_obj.kaina = 790.5
#
# import datetime
#
# eilutes_obj.sukurimo_data = datetime.datetime(1999,9,19,17,1,1)
# print(eilutes_obj)
# session.commit()