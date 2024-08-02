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
