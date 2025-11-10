# backend/routers/usuarios.py
from fastapi import APIRouter, HTTPException
from backend.models.usuarios_mdls import UsuarioModel

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/")
def crear_usuario(nombre: str, telefono: str = None, correo: str = None, rol: str = "usuario"):
    """ Crear un nuevo usuario en la base de datos."""
    try:
        nuevo_usuario = UsuarioModel.crear_usuario(nombre, telefono, correo, rol)
        return {"status": "success", "data": nuevo_usuario}
    except HTTPException as e:
        raise e

@router.get("/")
def listar_usuarios():
    """ Listar todos los usuarios (solo administradores)."""
    return {"status": "success", "data": UsuarioModel.listar_usuarios()}

@router.get("/{id_usuario}")
def obtener_usuario(id_usuario: str):
    """ Obtener usuario por ID."""
    return {"status": "success", "data": UsuarioModel.obtener_usuario_por_id(id_usuario)}

@router.put("/{id_usuario}")
def actualizar_usuario(id_usuario: str, data: dict):
    """ Actualizar información de un usuario."""
    return {"status": "success", "data": UsuarioModel.actualizar_usuario(id_usuario, data)}

@router.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: str):
    """ Eliminar usuario por ID."""
    return UsuarioModel.eliminar_usuario(id_usuario)
