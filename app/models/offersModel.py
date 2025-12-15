from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

from app.database import Base

class Offers(Base):
    __tablename__ = "ofertas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    loja = Column(String, nullable=False)
    estoque = Column(Integer, nullable=False)
    precoAtual = Column(Float, nullable=False)
    precoAntigo = Column(Float, nullable=False)
    descricao = Column(String, nullable=False)
    image = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
