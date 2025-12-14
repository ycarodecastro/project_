from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class LoginResponse(BaseModel):
    id: int
    nome: str
    email: str
    tipo: str
    token: str  # se quiser autenticação futura
    endereco: str | None = None
    telefone: str | None = None
    cnpj: str | None = None
    horario: str | None = None

    class Config:
        from_attributes = True