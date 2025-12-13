from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import ofertas
from schemas import ofertas  # assumindo que ofertas é o schema Pydantic
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Api de Promoções")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência para pegar a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ROTA PRINCIPAL
@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

# ROTA DAS OFERTAS
@app.get("/offers")
def get_offers(db: Session = Depends(get_db)):
    return db.query(ofertas).all()

# POST de ofertas
@app.post("/offers", response_model=ofertas.OfertaResponse)
def post_offers(oferta: ofertas.OfertaCreate, db: Session = Depends(get_db)):
    nova_oferta = ofertas(nome=oferta.nome, preco=oferta.preco)
    db.add(nova_oferta)
    db.commit()
    db.refresh(nova_oferta)
    return nova_oferta
