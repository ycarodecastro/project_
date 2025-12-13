from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware

from offersModel import Base, Offers
from offersShemas import OffersCreate, OffersResponse

app = FastAPI(title="API de Promoções")

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dbproject_mh38_user:Ocd5Uwtw8Y5oZ6q6rrW15x7XiaVdhGOF@dpg-d4uoad8gjchc73cdu700-a.ohio-postgres.render.com/dbproject_mh38"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência do DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas
@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

@app.get("/offers", response_model=list[OffersResponse])
def get_offers(db: Session = Depends(get_db)):
    return db.query(Offers).all()

@app.post("/offers/create", response_model=OffersResponse)
def post_offers(oferta: OffersCreate, db: Session = Depends(get_db)):
    nova_oferta = Offers(nome=oferta.nome, preco=oferta.preco)
    db.add(nova_oferta)
    db.commit()
    db.refresh(nova_oferta)
    return nova_oferta
