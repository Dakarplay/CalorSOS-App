# backend/app/routers/reportes.py
from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from backend.models.reportes_mdls import ReporteModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol

router = APIRouter(prefix="/reportes", tags=["Reportes"])

from fastapi import Form

@router.post("/")
def crear_reporte(
    tipo: str = Form(...),
    nombre: str = Form(None),
    descripcion: str = Form(None),
    latitud: float = Form(None),
    longitud: float = Form(None),
    tipo_zona_fresca: str = Form(None),   # 👈 nuevo campo
    datos_usuario: dict = Depends(verificar_token)
):
    try:
        # Validación: si el tipo es zona_fresca, tipo_zona_fresca es obligatorio
        if tipo == "zona_fresca" and not tipo_zona_fresca:
            raise HTTPException(status_code=400, detail="El campo 'tipo_zona_fresca' es obligatorio para reportes de zona fresca.")

        id_usuario = datos_usuario["id_usuario"]
        reporte = ReporteModel.crear_reporte(
            id_usuario,
            tipo,
            nombre,
            descripcion,
            latitud,
            longitud,
            tipo_zona_fresca  # 👈 pasarlo al modelo
        )
        return {"status": "success", "data": reporte}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Listar todos los reportes (solo administradores)
@router.get("/")
def listar_reportes(
    id_usuario: Optional[str] = None,
    tipo: Optional[str] = None,
    estado: Optional[str] = None,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """
    Lista reportes. Solo los administradores pueden acceder a esta ruta.
    """
    return {"status": "success", "data": ReporteModel.listar_reportes(id_usuario, tipo, estado)}


# Obtener un reporte específico (solo usuarios autenticados)
@router.get("/{id_reporte}")
def obtener_reporte(
    id_reporte: str,
    datos_usuario: dict = Depends(verificar_token)
):
    """
    Obtiene un reporte por su ID. Requiere autenticación.
    """
    return {"status": "success", "data": ReporteModel.obtener_reporte_por_id(id_reporte)}


# Actualizar un reporte (solo administradores)
@router.put("/{id_reporte}")
def actualizar_reporte(
    id_reporte: str,
    data: dict,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """
    Actualiza un reporte existente. Solo los administradores pueden hacerlo.
    """
    return {"status": "success", "data": ReporteModel.actualizar_reporte(id_reporte, data)}


# Eliminar un reporte (solo administradores)
@router.delete("/{id_reporte}")
def eliminar_reporte(
    id_reporte: str,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """
    Elimina un reporte por su ID. Solo los administradores pueden hacerlo.
    """
    return ReporteModel.eliminar_reporte(id_reporte)
