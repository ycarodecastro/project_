from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class LoginResponse(BaseModel):
    id: int
    nome: str
    email: str
    tipo: str  # 'USER' ou 'STORE'

    class Config:
        from_attributes = True