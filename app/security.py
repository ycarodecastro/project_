from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # truncar para 72 bytes se quiser, ou deixar o passlib cuidar
    password_bytes = password.encode('utf-8')[:72]
    return pwd_context.hash(password_bytes.decode('utf-8'))

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)
