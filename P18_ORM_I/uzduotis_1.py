import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

# duomenų bazės failo sukūrimas (jei jau sukurtas, tada prisijungiama)
engine = create_engine("sqlite:///darbuotojai.db")
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'darbuotojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    gimimo_data = Column(DateTime)
    pareigos = Column(String)
    atlyginimas = Column(Float)
    idarbinimo_data = Column(DateTime)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas, idarbinimo_data):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
        self.idarbinimo_data = idarbinimo_data

    def __repr__(self):
        return f'{self.vardas} {self.pavarde}, {self.pareigos}, {self.atlyginimas}'

Base.metadata.create_all(engine)

# #############################
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("--------------------------\n"
          "Pasirinkimo meniu:\n"
          "1. Įvesti naują darbuotoja\n"
          "2. Peržiūrėti darbuotojus\n"
          "q. Išeiti iš programos")
    menu_choice = input("Įveskite pasirinkimą: ")
    if menu_choice == "1":
        vardas = input("Įveskite darbuotojo vardą: ")
        pavarde = input("Įveskite darbuotojo pavardę: ")
        gimimo_data_input = input("Įveskite darbuotojo gimimo datą (formatas 2000-12-30): ")
        year, month, day = map(int, gimimo_data_input.split('-'))
        gimimo_data = datetime.date(year, month, day)
        pareigos = input("Įveskite darbuotojo pareigas: ")
        atlyginimas = float(input("Įveskite darbuotojo mėnesinį atlyginimą: "))
        idarbinimo_data_input = input("Įveskite darbuotojo įdarbinimo datą (formatas 2000-12-30): ")
        year, month, day = map(int, gimimo_data_input.split('-'))
        idarbinimo_data = datetime.date(year, month, day)
        eilute_o = Darbuotojas(vardas, pavarde, gimimo_data, pareigos, atlyginimas, idarbinimo_data)
        session.add(eilute_o)
        session.commit()
    elif menu_choice == "2":
        query = session.query(Darbuotojas)
        visos_eilutes = query.all()
        for eilute_o in visos_eilutes:
            print(eilute_o)
    elif menu_choice == "q":
        print("Programa baigė darbą.")
        break
    else:
        print("Tokio pasirinkimo nėra!")