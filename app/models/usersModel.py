from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    email = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    # Relacionamentos
    user = relationship("UserProfile", back_populates="user", uselist=False)
    store = relationship("Store", back_populates="users", uselist=False)

