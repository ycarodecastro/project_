from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, SessionLocal, engine
from app.models.offersModel import Offers
from app.security import hash_password
from app.shemas.loginShemas import LoginRequest, LoginResponse
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

# Endpoint de login
@app.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Tenta encontrar usuário (perfil + usuário)
    user = (
        db.query(UserProfile, Users)
        .join(Users, Users.id == UserProfile.user_id)
        .filter(Users.email == data.email)
        .first()
    )
    
    if user:
        profile, user_row = user
        if user_row.senha_hash == data.senha:  # ou use função de hash se aplicável
            return LoginResponse(
                id=user_row.id,
                nome=profile.nome,
                email=user_row.email,
                tipo=user_row.tipo
            )

    # Tenta encontrar loja
    store = (
        db.query(Store, Users)
        .join(Users, Users.id == Store.user_id)
        .filter(Users.email == data.email)
        .first()
    )
    if store:
        store_row, user_row = store
        if user_row.senha_hash == data.senha:
            return LoginResponse(
                id=store_row.id,
                nome=store_row.nome,
                email=user_row.email,
                tipo=user_row.tipo
            )

    raise HTTPException(status_code=401, detail="Email ou senha incorretos")



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
            endereco=profile.endereco if profile.endereco != '' else None,
            telefone=profile.telefone if profile.telefone != '' else None,
            tipo=user.tipo
        )
        for profile, user in resultados
    ]


@app.get("/store", response_model=list[StoreResponse])
def get_store(db: Session = Depends(get_db)):
    resultados = (
        db.query(Store, Users)
        .join(Users, Users.id == Store.user_id)
        .all()
    )

    return [
        StoreResponse(
            id=store.id,
            nome=store.nome,
            endereco=store.endereco,
            horario=store.horario,
            cnpj=store.cnpj,
            email=user.email,
            tipo=user.tipo,
        )
        for store, user in resultados
    ]

