from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import offersModel
import offersShemas
from app.database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Api de Promoções")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

@app.get("/offers", response_model=list[offersShemas.OffersResponse])
def get_offers(db: Session = Depends(get_db)):
    return db.query(offersModel.Offers).all()

@app.post("/offers", response_model=offersShemas.OffersResponse)
def post_offers(oferta: offersShemas.OffersCreate, db: Session = Depends(get_db)):
    nova_oferta = offersModel.Offers(nome=oferta.nome, preco=oferta.preco)
    db.add(nova_oferta)
    db.commit()
    db.refresh(nova_oferta)
    return nova_oferta
