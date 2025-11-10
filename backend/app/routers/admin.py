# backend/routers/admin.py
from fastapi import APIRouter, HTTPException
from backend.models.admin_mdls import AdminModel

router = APIRouter(prefix="/admin", tags=["Administración"])

@router.put("/validar_reporte/{id_reporte}")
def validar_reporte(id_reporte: str):
    """Permite al administrador validar un reporte comunitario (cambiar estado a 'validado')."""
    try:
        reporte = AdminModel.validar_reporte(id_reporte)
        return {"status": "success", "message": "Reporte validado correctamente", "data": reporte}
    except HTTPException as e:
        raise e

@router.put("/rechazar_reporte/{id_reporte}")
def rechazar_reporte(id_reporte: str):
    """Permite al administrador rechazar un reporte comunitario (cambiar estado a 'rechazado')."""
    try:
        reporte = AdminModel.rechazar_reporte(id_reporte)
        return {"status": "success", "message": "Reporte rechazado correctamente", "data": reporte}
    except HTTPException as e:
        raise e
