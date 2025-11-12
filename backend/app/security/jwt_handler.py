# backend/app/security/jwt_handler.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

# Cargar variables del entorno
load_dotenv("calorsos.env")

SECRET_KEY = os.getenv("JWT_SECRET", "super_secret_key_calorsos")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hora

# Configuración de seguridad
security = HTTPBearer()

def crear_token(datos: dict):
    """Genera un JWT con expiración."""
    to_encode = datos.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verifica el JWT recibido y devuelve los datos decodificados."""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

def verificar_rol(roles_permitidos: list):
    """
    Dependencia que permite verificar si el usuario tiene uno de los roles autorizados.
    Ejemplo de uso:
    @router.get("/admin", dependencies=[Depends(verificar_rol(["admin"]))])
    """
    def wrapper(credentials: HTTPAuthorizationCredentials = Security(security)):
        token = credentials.credentials
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            rol = payload.get("rol")
            if rol not in roles_permitidos:
                raise HTTPException(
                    status_code=403,
                    detail="No tienes permisos para acceder a esta ruta"
                )
            return payload  # devuelve datos del usuario autenticado
        except JWTError:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return wrapper