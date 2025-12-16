from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dbprincipal_1_user:z3AGdYYB6SlVGApslQPGWDVAIPgHhGZe@dpg-d50ppgnfte5s73csn9r0-a.ohio-postgres.render.com/dbprincipal_1"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
