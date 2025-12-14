from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from app.models.usersModel import Users

Base = declarative_base()

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    cnpj = Column(String, nullable=False, unique=True)

    user = relationship("Users", back_populates="user")

