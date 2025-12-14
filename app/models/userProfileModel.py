from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from usersModel import Users

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = "userProfile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String, nullable=False, unique=True)

    user = relationship("Users", back_populates="user")

