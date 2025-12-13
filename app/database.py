from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dbproduct_zfda_user:xEP9aNQpvXGXQtN3FX1PCPxTOoLPp0ga@dpg-d4ut4adactks73fa1k60-a.ohio-postgres.render.com/dbproduct_zfda"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
