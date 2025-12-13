from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Criar engine SQLite
engine = create_engine("sqlite:///./db.sqlite3", connect_args={"check_same_thread": False})

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Sessão para manipular o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
