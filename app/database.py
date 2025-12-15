from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexão PostgreSQL
DATABASE_URL = "postgresql://dbprincipal_user:Pc3O8hOpHog0VIV4zXtChim6lkGpydOH@dpg-d4voih7pm1nc73bsnsig-a.ohio-postgres.render.com/dbprincipal"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
