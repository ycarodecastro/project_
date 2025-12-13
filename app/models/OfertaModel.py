from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OfertaModel(Base):
    __tablename__ = "ofertas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)