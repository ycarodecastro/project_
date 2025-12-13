from typing import Optional
from pydantic import BaseModel

class OffersBase(BaseModel):
    nome: str
    estoque: int
    precoAtual: float
    precoAntigo: float
    descricao: str
    image: Optional[str] = None


class OffersCreate(OffersBase):
    pass

class OffersResponse(OffersBase):
    id: int

    model_config = {
        "from_attributes": True
    }
