# backend/routers/reportes.py
from fastapi import APIRouter, HTTPException
from backend.models.reportes_mdls import ReporteModel
from typing import Optional

router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.post("/")
def crear_reporte(id_usuario: str, tipo: str, descripcion: str = None,
                latitud: float = None, longitud: float = None, foto_url: str = None,
                estado: str = "pendiente"):
    """Crea un nuevo reporte."""
    try:
        reporte = ReporteModel.crear_reporte(id_usuario, tipo, descripcion, latitud, longitud, foto_url, estado)
        return {"status": "success", "data": reporte}
    except HTTPException as e:
        raise e

@router.get("/")
def listar_reportes(id_usuario: Optional[str] = None, tipo: Optional[str] = None, estado: Optional[str] = None):
    """Lista reportes. Se pueden filtrar por id_usuario, tipo o estado."""
    return {"status": "success", "data": ReporteModel.listar_reportes(id_usuario, tipo, estado)}

@router.get("/{id_reporte}")
def obtener_reporte(id_reporte: str):
    """Obtiene un reporte por su ID."""
    return {"status": "success", "data": ReporteModel.obtener_reporte_por_id(id_reporte)}

@router.put("/{id_reporte}")
def actualizar_reporte(id_reporte: str, data: dict):
    """Actualiza un reporte existente. 'data' debe contener los campos a modificar."""
    return {"status": "success", "data": ReporteModel.actualizar_reporte(id_reporte, data)}

@router.delete("/{id_reporte}")
def eliminar_reporte(id_reporte: str):
    """Elimina un reporte por su ID."""
    return ReporteModel.eliminar_reporte(id_reporte)
