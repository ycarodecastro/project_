from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float

from app.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    email = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    # Relacionamentos
    store = relationship("Store", back_populates="user", uselist=False)
    user = relationship("UserProfile", back_populates="user", uselist=False)

