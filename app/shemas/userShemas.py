from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    tipo: str

    class Config:
        from_attributes = True
