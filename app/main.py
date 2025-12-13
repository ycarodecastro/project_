from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Api de Promoções")

# CORS (ESSENCIAL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROTA PRINCIPAL
@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

# ROTA DAS OFERTAS
@app.get("/offers")
def get_offers():
    return [
        {
            "id": 1,
            "title": "Pizza em promoção",
            "price": 29.90
        },
        {
            "id": 2,
            "title": "Supermercado desconto",
            "price": 99.90
        }
    ]