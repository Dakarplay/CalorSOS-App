# backend/routers/puntos_hidratacion.py
from fastapi import APIRouter, HTTPException
from backend.models.puntos_hidratacion_mdls import PuntoHidratacionModel

router = APIRouter(prefix="/puntos_hidratacion", tags=["Puntos de Hidratación"])

@router.post("/")
def crear_punto(nombre: str, direccion: str = None, latitud: float = None, longitud: float = None, estado: str = "pendiente", fuente: str = "reporte ciudadano", validado_por: str = None):
    """ Crea un nuevo punto de hidratación."""
    try:
        punto = PuntoHidratacionModel.crear_punto(nombre, direccion, latitud, longitud, estado, fuente, validado_por)
        return {"status": "success", "data": punto}
    except HTTPException as e:
        raise e

@router.get("/")
def listar_puntos(estado: str = None):
    """ Lista todos los puntos de hidratación (filtrados por estado si se indica)."""
    return {"status": "success", "data": PuntoHidratacionModel.listar_puntos(estado)}

@router.get("/{id_punto}")
def obtener_punto(id_punto: str):
    """ Obtiene un punto de hidratación por su ID."""
    return {"status": "success", "data": PuntoHidratacionModel.obtener_punto_por_id(id_punto)}

@router.put("/{id_punto}")
def actualizar_punto(id_punto: str, data: dict):
    """ Actualiza los datos de un punto de hidratación."""
    return {"status": "success", "data": PuntoHidratacionModel.actualizar_punto(id_punto, data)}

@router.delete("/{id_punto}")
def eliminar_punto(id_punto: str):
    """ Elimina un punto de hidratación."""
    return PuntoHidratacionModel.eliminar_punto(id_punto)
