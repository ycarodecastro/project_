from pydantic import BaseModel

# Dados enviados pelo front-end
class OfertaCreate(BaseModel):
    nome: str
    preco: float

# Dados retornados para o front-end (inclui id)
class OfertaResponse(BaseModel):
    id: int
    nome: str
    preco: float