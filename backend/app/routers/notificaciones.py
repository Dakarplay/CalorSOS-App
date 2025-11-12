from fastapi import APIRouter, HTTPException, Depends, Body
from typing import Optional
from backend.models.notificaciones_mdls import NotificacionModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol

router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])


# Crear notificación (solo admin)
@router.post("/")
def crear_notificacion(mensaje: str = Body(...), id_usuario: str = Body(...), datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        notificacion = NotificacionModel.crear_notificacion(id_usuario, mensaje)
        return {"status": "success", "data": notificacion}
    except HTTPException as e:
        raise e

# Listar notificaciones:
# - admin: lista todas
# - usuario: lista solo las suyas (si pasa ?id_usuario)
@router.get("/")
def listar_notificaciones(id_usuario: Optional[str] = None, datos_usuario: dict = Depends(verificar_token)):
    try:
        # Si es admin, puede listar por cualquier id o todas
        if datos_usuario["rol"] == "admin":
            return {"status": "success", "data": NotificacionModel.listar_notificaciones(id_usuario)}
        # si es usuario, forzamos su id
        return {"status": "success", "data": NotificacionModel.listar_notificaciones(datos_usuario["id_usuario"])}
    except HTTPException as e:
        raise e

# Obtener por id (autenticado)
@router.get("/{id_notificacion}")
def obtener_notificacion(id_notificacion: str, datos_usuario: dict = Depends(verificar_token)):
    try:
        notif = NotificacionModel.obtener_notificacion_por_id(id_notificacion)
        # Si no es admin, revisar que la notificación pertenezca al usuario
        if datos_usuario["rol"] != "admin" and notif["id_usuario"] != datos_usuario["id_usuario"]:
            raise HTTPException(status_code=403, detail="No tienes permisos para ver esta notificación")
        return {"status": "success", "data": notif}
    except HTTPException as e:
        raise e

# Actualizar estado (solo admin)
@router.put("/{id_notificacion}")
def actualizar_estado(id_notificacion: str, estado: str = Body(...), datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        return {"status": "success", "data": NotificacionModel.actualizar_estado(id_notificacion, estado)}
    except HTTPException as e:
        raise e

# Eliminar (solo admin)
@router.delete("/{id_notificacion}")
def eliminar_notificacion(id_notificacion: str, datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        return NotificacionModel.eliminar_notificacion(id_notificacion)
    except HTTPException as e:
        raise e
