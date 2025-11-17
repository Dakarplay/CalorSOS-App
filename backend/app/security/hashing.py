# Inicio hashing.py

# backend/app/security/hashing.py

# Importaciones necesarias para el manejo de contraseñas
from passlib.context import CryptContext

# Configuración del contexto de bcrypt para hashing seguro
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Genera un hash seguro de la contraseña utilizando bcrypt.
    Retorna el hash de la contraseña para almacenamiento.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que la contraseña en texto plano coincida con el hash almacenado.
    Retorna True si coinciden, False en caso contrario.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Fin hashing.py
