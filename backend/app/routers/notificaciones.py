# backend/routers/notificaciones.py
from fastapi import APIRouter, HTTPException
from backend.models.notificaciones_mdls import NotificacionModel

router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])

@router.post("/")
def crear_notificacion(id_usuario: str, mensaje: str, estado: str = "pendiente"):
    """Crea una nueva notificación."""
    try:
        notificacion = NotificacionModel.crear_notificacion(id_usuario, mensaje, estado)
        return {"status": "success", "data": notificacion}
    except HTTPException as e:
        raise e

@router.get("/")
def listar_notificaciones(id_usuario: str = None):
    """Lista todas las notificaciones o solo las de un usuario específico."""
    return {"status": "success", "data": NotificacionModel.listar_notificaciones(id_usuario)}

@router.get("/{id_notificacion}")
def obtener_notificacion(id_notificacion: str):
    """Obtiene una notificación específica por su ID."""
    return {"status": "success", "data": NotificacionModel.obtener_notificacion_por_id(id_notificacion)}

@router.put("/{id_notificacion}")
def actualizar_estado(id_notificacion: str, estado: str):
    """Actualiza el estado de una notificación (pendiente o enviada)."""
    return {"status": "success", "data": NotificacionModel.actualizar_estado(id_notificacion, estado)}

@router.delete("/{id_notificacion}")
def eliminar_notificacion(id_notificacion: str):
    """Elimina una notificación existente."""
    return NotificacionModel.eliminar_notificacion(id_notificacion)
