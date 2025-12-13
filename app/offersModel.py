from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Offers(Base):
    __tablename__ = "ofertas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    estoque = Column(Integer, nullabla=False)
    precoAtual = Column(Float, nullable=False)
    precoAntigo = Column(Float, nullable=False)
    descricao = Column(String, nullable=False)
