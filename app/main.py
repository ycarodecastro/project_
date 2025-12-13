from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app import offersModel
from app import offersShemas
from app.database import SessionLocal
from app.database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI(title="Api de Promoções")

Base = declarative_base()

# Criar engine SQLite
engine = create_engine("postgresql://dbproject_mh38_user:Ocd5Uwtw8Y5oZ6q6rrW15x7XiaVdhGOF@dpg-d4uoad8gjchc73cdu700-a.ohio-postgres.render.com/dbproject_mh38")

# Sessão para manipular o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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

# Criar tabelas
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

@app.get("/offers", response_model=list[offersShemas.OffersResponse])
def get_offers(db: Session = Depends(get_db)):
    return db.query(offersModel.Offers).all()

@app.post("/offers/create", response_model=offersShemas.OffersResponse)
def post_offers(oferta: offersShemas.OffersCreate, db: Session = Depends(get_db)):
    nova_oferta = offersModel.Offers(nome=oferta.nome, preco=oferta.preco)
    db.add(nova_oferta)
    db.commit()
    db.refresh(nova_oferta)
    return nova_oferta
