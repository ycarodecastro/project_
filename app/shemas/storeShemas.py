from pydantic import BaseModel

class StoreCreate(BaseModel):
    email: str
    senha: str
    nome: str
    endereco: str
    horario: str
    cnpj: str


class StoreResponse(BaseModel):
    id: int
    nome: str
    endereco: str
    horario: str
    cnpj: str

    class Config:
        from_attributes = True
