# backend/routers/zonas_frescas.py
from fastapi import APIRouter, HTTPException
from backend.models.zonas_frescas_mdls import ZonaFrescaModel

router = APIRouter(prefix="/zonas_frescas", tags=["Zonas Frescas"])

@router.post("/")
def crear_zona(nombre: str, descripcion: str = None, latitud: float = None, longitud: float = None, tipo: str = "urbana", estado: str = "activa", validado_por: str = None):
    """ Crea una nueva zona fresca."""
    try:
        zona = ZonaFrescaModel.crear_zona(nombre, descripcion, latitud, longitud, tipo, estado, validado_por)
        return {"status": "success", "data": zona}
    except HTTPException as e:
        raise e

@router.get("/")
def listar_zonas(estado: str = None):
    """ Lista todas las zonas frescas, opcionalmente filtradas por estado."""
    return {"status": "success", "data": ZonaFrescaModel.listar_zonas(estado)}

@router.get("/{id_zona}")
def obtener_zona(id_zona: str):
    """ Obtiene una zona fresca por su ID."""
    return {"status": "success", "data": ZonaFrescaModel.obtener_zona_por_id(id_zona)}

@router.put("/{id_zona}")
def actualizar_zona(id_zona: str, data: dict):
    """ Actualiza los datos de una zona fresca."""
    return {"status": "success", "data": ZonaFrescaModel.actualizar_zona(id_zona, data)}

@router.delete("/{id_zona}")
def eliminar_zona(id_zona: str):
    """ Elimina una zona fresca."""
    return ZonaFrescaModel.eliminar_zona(id_zona)
