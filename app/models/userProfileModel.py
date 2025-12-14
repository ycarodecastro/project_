from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float

from app.database import Base

class UserProfile(Base):
    __tablename__ = "userProfile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    nome = Column(String, nullable=False)
    endereco = Column(String)
    telefone = Column(String, unique=True)

    user = relationship("Users", back_populates="user")

