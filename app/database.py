from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dbprincipal2_user:Rzf5M8K0nP6gTXnwCbbWsQCNoEzfWYA3@dpg-d50d7gt6ubrc739qsmug-a.ohio-postgres.render.com/dbprincipal2"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
