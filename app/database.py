from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dblogin_u1me_user:hZSGx7Zyix6WlzOTSVR4GxZTmQb4HUbF@dpg-d4vht2euk2gs739ehsjg-a.ohio-postgres.render.com/dblogin_u1me"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
