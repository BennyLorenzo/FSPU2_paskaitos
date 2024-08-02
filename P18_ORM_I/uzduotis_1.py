import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, func
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
    idarbinimo_data = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f'{self.id}. {self.vardas} {self.pavarde}, {self.pareigos}, {self.atlyginimas}, {self.idarbinimo_data.date()}'
Base.metadata.create_all(engine)

# #############################
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("--------------------------\n"
          "Pasirinkimo meniu:\n"
          "1. Įvesti naują darbuotoją\n"
          "2. Peržiūrėti darbuotojus\n"
          "3. Rasti darbutoją pagal pavardę\n"
          "4. Ištrinti darbuotoją pagal ID\n"
          "5. Keisti duomenis pagal ID\n"
          "6. Rasti darbuotojus pagal atlyginimų lubas\n"
          "7. Peržiūrėti atlyginimų statistiką\n"
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
        eilute_o = Darbuotojas(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
        session.add(eilute_o)
        session.commit()

    elif menu_choice == "2":
        query = session.query(Darbuotojas)
        visos_eilutes = query.all()
        for eilute_o in visos_eilutes:
            print(eilute_o)

    elif menu_choice == "3":
        pavarde = input("Įveskite ieškomo darbuotojo pavardę: ")
        ieskomos_eilutes = session.query(Darbuotojas).filter(Darbuotojas.pavarde.ilike(f'%{pavarde}%')).all()
        if len(ieskomos_eilutes) < 1:
            print("Darbuotojų nerasta.")
        else:
            print("Rasti darbuotojai: ")
            for eilute in ieskomos_eilutes:
                print(eilute)




    elif menu_choice == "4":
        eilutes_id = int(input("Įveskite darbuotojo ID: "))
        eilutes_obj = session.query(Darbuotojas).get(eilutes_id)
        if(eilutes_obj == None):
            print("Darbuotojas su tokiu ID nerastas!")
        else:
            print("Rastas darbuotojas:", eilutes_obj)
            while True:
                delete_confirm = input(f"Ar norite ištrinti darbuotoją {eilutes_obj.vardas} {eilutes_obj.pavarde}? (taip/ne): ")
                if delete_confirm == "taip":
                    session.delete(eilutes_obj)
                    session.commit()
                    print("Darbuotojas ištrintas!")
                    break
                elif delete_confirm == "ne":
                    break
                else:
                    continue

    elif menu_choice == "5":
        eilutes_id = int(input("Įveskite darbuotojo ID: "))
        eilutes_obj = session.query(Darbuotojas).get(eilutes_id)
        if(eilutes_obj == None):
            print("Darbuotojas su tokiu ID nerastas!")
        else:
            print("Rastas darbuotojas:", eilutes_obj)
            while True:
                print("Pasirinkite, kokius duomenis norite pakeisti\n"
                      "1. Vardas\n"
                      "2. Pavardė\n"
                      "3. Gimimo data\n"
                      "4. Pareigos\n"
                      "5. Atlyginimas\n"
                      "6. Įdarbinimo data\n"
                      "q. Nutraukti duomenų keitimą")
                update_choice = input("Įveskite pasirinkimą: ")
                if update_choice == "1":
                    update_name = input("Įveskite naują vardą: ")
                    eilutes_obj.vardas = update_name
                    session.commit()
                elif update_choice == "2":
                    update_surname = input("Įveskite naują pavardę: ")
                    eilutes_obj.pavarde = update_surname
                    session.commit()
                elif update_choice == "3":
                    update_birth_date = input("Įveskite naują gimimo datą (formatas 2000-12-30): ")
                    year, month, day = map(int, update_birth_date.split('-'))
                    update_birth_date = datetime.date(year, month, day)
                    eilutes_obj.gimimo_data = update_birth_date
                    session.commit()
                elif update_choice == "4":
                    update_position = input("Įveskite naujas pareigas: ")
                    eilutes_obj.pareigos = update_position
                    session.commit()
                elif update_choice == "5":
                    update_salary = float(input("Įveskite naują atlyginimą: "))
                    eilutes_obj.atlyginimas = update_salary
                    session.commit()
                elif update_choice == "6":
                    update_work_date = input("Įveskite naują įdarbinimo datą (formatas 2000-12-30): ")
                    year, month, day = map(int, update_work_date.split('-'))
                    update_work_date = datetime.date(year, month, day)
                    eilutes_obj.idarbinimo_data = update_work_date
                    session.commit()
                elif update_choice == "q":
                    break
                else:
                    print("Tokio pasirinkimo nėra!")

    elif menu_choice == "6":
        atlyginimo_lubos = float(input("Įveskite atlyginimo lubas: "))
        filtruoti_objektai = session.query(Darbuotojas).filter(Darbuotojas.atlyginimas <= atlyginimo_lubos).all()
        print(f"Darbuotojai su algomis iki {atlyginimo_lubos}: ")
        for eil in filtruoti_objektai:
            print(eil)

    elif menu_choice == "7":
        print("----------Atlyginimų statistika----------")
        atlyginimu_suma = session.query(func.sum(Darbuotojas.atlyginimas)).scalar()
        print("Atlyginimų suma:",atlyginimu_suma)

        atlyginimu_vidurkis = session.query(func.avg(Darbuotojas.atlyginimas)).scalar()
        print("Atlyginimų vidurkis:",round(atlyginimu_vidurkis,2))

        maziausias_atlyginimas = session.query(func.min(Darbuotojas.atlyginimas)).scalar()
        print("Mažiausias atlyginimas:",maziausias_atlyginimas)

        didziausias_atlyginimas = session.query(func.max(Darbuotojas.atlyginimas)).scalar()
        print("Didžiausias atlyginimas:",didziausias_atlyginimas)

    elif menu_choice == "q":
        print("Programa baigė darbą.")
        break
    else:
        print("Tokio pasirinkimo nėra!")