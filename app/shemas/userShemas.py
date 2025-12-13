from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    senha: str
    nome: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    email: str
    tipo: str

    class Config:
        from_attributes = True
