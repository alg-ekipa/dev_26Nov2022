# Povezivanje tablica - relacije

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

class Kupac(Base):
   __tablename__ = 'kupci'

   id = Column(Integer, primary_key = True)
   ime = Column(String)
   adresa = Column(String)
   email = Column(String)

class Racun(Base):
   __tablename__ = 'racuni'
   
   id = Column(Integer, primary_key = True)
   id_kupca = Column(Integer, ForeignKey('kupci.id'))
   broj = Column(Integer)
   iznos = Column(Integer)
   kupac = relationship("Kupac", back_populates = "racuni")

Kupac.invoices = relationship("Racun", order_by = Racun.id, back_populates = "kupac")
Base.metadata.create_all(engine)