from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dbprofiles_user:4JReo5cKlwKs1ja5gYdpQl5oJtDEOy4J@dpg-d4v2chali9vc73dfm5fg-a.ohio-postgres.render.com/dbprofiles"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

