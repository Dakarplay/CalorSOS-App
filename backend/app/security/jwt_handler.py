# Inicio jwt_handler.py

# backend/app/security/jwt_handler.py

# Importaciones necesarias para manejo de JWT
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv("calorsos.env")

# Configuración de JWT
SECRET_KEY = os.getenv("JWT_SECRET", "super_secret_key_calorsos")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hora

# Instancia de HTTPBearer para autenticación
security = HTTPBearer()

def crear_token(datos: dict):
    """
    Genera un token JWT con expiración.
    Agrega el tiempo de expiración y codifica los datos.
    """
    to_encode = datos.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifica el token JWT recibido y devuelve los datos decodificados.
    Lanza excepción si el token es inválido o expirado.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

def verificar_rol(roles_permitidos: list):
    """
    Dependencia que verifica si el usuario tiene uno de los roles autorizados.
    Retorna los datos del usuario si tiene permisos, lanza excepción si no.
    Ejemplo de uso: @router.get("/admin", dependencies=[Depends(verificar_rol(["admin"]))])
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

# Fin jwt_handler.py
