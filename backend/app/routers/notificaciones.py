# Inicio backend/app/routers/notificaciones.py

# Importaciones necesarias para el router de notificaciones
from fastapi import APIRouter, HTTPException, Depends, Body
from typing import Optional
from backend.models.notificaciones_mdls import NotificacionModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol

# Creación del router con prefijo y tags
router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])

# Endpoint para crear notificación (solo administradores)
@router.post("/")
def crear_notificacion(mensaje: str = Body(...), id_usuario: str = Body(...), datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        # Crear nueva notificación usando el modelo
        notificacion = NotificacionModel.crear_notificacion(id_usuario, mensaje)
        return {"status": "success", "data": notificacion}
    except HTTPException as e:
        raise e

# Endpoint para listar notificaciones con permisos diferenciados
@router.get("/")
def listar_notificaciones(id_usuario: Optional[str] = None, datos_usuario: dict = Depends(verificar_token)):
    try:
        # Administradores pueden listar todas o filtrar por usuario
        if datos_usuario["rol"] == "admin":
            return {"status": "success", "data": NotificacionModel.listar_notificaciones(id_usuario)}
        # Usuarios normales solo ven sus propias notificaciones
        return {"status": "success", "data": NotificacionModel.listar_notificaciones(datos_usuario["id_usuario"])}
    except HTTPException as e:
        raise e

# Endpoint para obtener notificación por ID (con verificación de permisos)
@router.get("/{id_notificacion}")
def obtener_notificacion(id_notificacion: str, datos_usuario: dict = Depends(verificar_token)):
    try:
        # Obtener notificación del modelo
        notif = NotificacionModel.obtener_notificacion_por_id(id_notificacion)

        # Verificar permisos: admin puede ver todas, usuario solo las suyas
        if datos_usuario["rol"] != "admin" and notif["id_usuario"] != datos_usuario["id_usuario"]:
            raise HTTPException(status_code=403, detail="No tienes permisos para ver esta notificación")

        return {"status": "success", "data": notif}
    except HTTPException as e:
        raise e

# Endpoint para actualizar estado de notificación (solo administradores)
@router.put("/{id_notificacion}")
def actualizar_estado(id_notificacion: str, estado: str = Body(...), datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        # Actualizar estado usando el modelo
        return {"status": "success", "data": NotificacionModel.actualizar_estado(id_notificacion, estado)}
    except HTTPException as e:
        raise e

# Endpoint para eliminar notificación (solo administradores)
@router.delete("/{id_notificacion}")
def eliminar_notificacion(id_notificacion: str, datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        # Eliminar notificación usando el modelo
        return NotificacionModel.eliminar_notificacion(id_notificacion)
    except HTTPException as e:
        raise e

# Fin backend/app/routers/notificaciones.py
