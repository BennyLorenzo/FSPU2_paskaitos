from sqlalchemy.orm import sessionmaker
from models1 import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

# kad pakeisti konkrečios eilutės duomenis, pasiimame eilutės objektą į kintamąjį

for eilute_obj in session.query(Projektas).all():
    print(eilute_obj)

eilutes_id = 11
eilutes_obj = session.query(Projektas).get(eilutes_id)
print("------pagautas objektas, eilutė-----")
print(eilutes_obj)
#
# session.delete(eilutes_obj)
# session.commit()