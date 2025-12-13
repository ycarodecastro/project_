from pydantic import BaseModel

class OffersBase(BaseModel):
    nome: str
    preco: float

class OffersCreate(OffersBase):
    pass

class OffersResponse(OffersBase):
    id: int

    class Config:
        orm_mode = True
