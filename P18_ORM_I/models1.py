import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

# duomenų bazės failo sukūrimas (jei jau sukurtas, tada prisijungiama)
engine = create_engine("sqlite:///projektai.db")
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'projektas'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    kaina = Column(Float)
    sukurimo_data = Column(DateTime, default=datetime.datetime(2000,1,1))

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def __repr__(self):
        return f'{self.id} {self.pavadinimas} {self.kaina} {self.sukurimo_data}'

Base.metadata.create_all(engine)

# #############################
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
#
# #############################
# eilute_o = Projektas("Pirmas projektas",15000.5)
# session.add(eilute_o)
#
# eilute2_o = Projektas("Rojaus sodai",50000.7)
# session.add(eilute2_o)
# session.commit()
#
# query = session.query(Projektas) # suformuojama SQL užklausa per Projektas klasę į projektas lentelę
# visos_eilutes = query.all()
# print(visos_eilutes)






