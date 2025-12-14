from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, SessionLocal, engine
from app.models.offersModel import Offers
from app.security import hash_password
from app.shemas.offersShemas import OffersCreate, OffersResponse
from app.models.storeModel import Store
from app.shemas.storeShemas import StoreCreate, StoreResponse
from app.models.userProfileModel import UserProfile
from app.shemas.userShemas import UserCreate, UserResponse
from app.models.usersModel import Users

app = FastAPI(title="API de Promoções")


Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")

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
    return {"message": "API funcionando "}

@app.get("/offers", response_model=list[OffersResponse])
def get_offers(db: Session = Depends(get_db)):
    return db.query(Offers).all()

@app.post("/offers/create", response_model=OffersResponse)
def post_offers(oferta: OffersCreate, db: Session = Depends(get_db)):
    nova_oferta = Offers(nome=oferta.nome, loja=oferta.loja, estoque=oferta.estoque, precoAtual=oferta.precoAtual,precoAntigo=oferta.precoAntigo, descricao=oferta.descricao, image=oferta.image)
    db.add(nova_oferta)
    db.commit()
    db.refresh(nova_oferta)
    return nova_oferta

@app.post("/register/store", response_model=StoreResponse)
def post_store(store: StoreCreate, db: Session = Depends(get_db)):

    # Verifica email
    if db.query(Users).filter(Users.email == store.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = Users(
        email=store.email,
        senha_hash=hash_password(store.senha),
        tipo="STORE"
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    nova_loja = Store(
        user_id=novo_usuario.id,
        nome=store.nome,
        endereco=store.endereco,
        horario=store.horario,
        cnpj=store.cnpj
    )

    db.add(nova_loja)
    db.commit()
    db.refresh(nova_loja)

    return nova_loja

@app.post("/register/userProfile", response_model=UserResponse)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica email
    if db.query(Users).filter(Users.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    # Cria usuário
    novo_user = Users(
        email=user.email,
        senha_hash=hash_password(user.senha),
        tipo="USER"
    )
    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)

    # Cria perfil
    novo_usuario = UserProfile(
        user_id=novo_user.id,
        nome=user.nome,
        endereco=user.endereco if user.endereco != '' else None,
        telefone=user.telefone if user.telefone != '' else None  # aqui
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    # Retorna UserResponse explicitamente
    return UserResponse(
        id=novo_user.id,
        nome=novo_usuario.nome,
        email=novo_user.email,
        tipo=novo_user.tipo
    )


@app.get("/userProfile", response_model=list[UserResponse])
def get_user(db: Session = Depends(get_db)):
    resultados = (
        db.query(UserProfile, Users)
        .join(Users, Users.id == UserProfile.user_id)
        .all()
    )

    return [
        UserResponse(
            id=user.id,
            nome=profile.nome,
            email=user.email,
            tipo=user.tipo
        )
        for profile, user in resultados
    ]


@app.get("/store", response_model=list[StoreResponse])
def get_store(db: Session = Depends(get_db)):
    return db.query(Store).all()
