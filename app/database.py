from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Criar engine SQLite
engine = create_engine("postgresql://dbproject_mh38_user:Ocd5Uwtw8Y5oZ6q6rrW15x7XiaVdhGOF@dpg-d4uoad8gjchc73cdu700-a.ohio-postgres.render.com/dbproject_mh38")

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Sessão para manipular o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
