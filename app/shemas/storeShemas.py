from pydantic import BaseModel

class StoreCreate(BaseModel):
    nome: str
    email: str
    senha: str
    endereco: str
    horario: str
    cnpj: str


class StoreResponse(BaseModel):
    id: int
    nome: str
    endereco: str
    horario: str
    cnpj: str
    email: str
    tipo: str


    class Config:
        from_attributes = True
