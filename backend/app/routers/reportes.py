# Inicio backend/app/routers/reportes.py

# Importaciones necesarias para el router de reportes
from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from backend.models.reportes_mdls import ReporteModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol
from fastapi import Form

# Creación del router con prefijo y tags
router = APIRouter(prefix="/reportes", tags=["Reportes"])

# Endpoint para crear reporte (usuario autenticado)
@router.post("/")
def crear_reporte(
    tipo: str = Form(...),
    nombre: str = Form(None),
    descripcion: str = Form(None),
    latitud: float = Form(None),
    longitud: float = Form(None),
    tipo_zona_fresca: str = Form(None),
    datos_usuario: dict = Depends(verificar_token)
):
    try:
        # Validación para reportes de zona fresca
        if tipo == "zona_fresca" and not tipo_zona_fresca:
            raise HTTPException(status_code=400, detail="El campo 'tipo_zona_fresca' es obligatorio para reportes de zona fresca.")

        # Obtener ID del usuario autenticado
        id_usuario = datos_usuario["id_usuario"]

        # Crear reporte usando el modelo
        reporte = ReporteModel.crear_reporte(
            id_usuario,
            tipo,
            nombre,
            descripcion,
            latitud,
            longitud,
            tipo_zona_fresca
        )
        return {"status": "success", "data": reporte}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para listar reportes (solo administradores)
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

# Endpoint para obtener reporte específico (usuario autenticado)
@router.get("/{id_reporte}")
def obtener_reporte(
    id_reporte: str,
    datos_usuario: dict = Depends(verificar_token)
):
    """
    Obtiene un reporte por su ID. Requiere autenticación.
    """
    return {"status": "success", "data": ReporteModel.obtener_reporte_por_id(id_reporte)}

# Endpoint para actualizar reporte (solo administradores)
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

# Endpoint para eliminar reporte (solo administradores)
@router.delete("/{id_reporte}")
def eliminar_reporte(
    id_reporte: str,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """
    Elimina un reporte por su ID. Solo los administradores pueden hacerlo.
    """
    return ReporteModel.eliminar_reporte(id_reporte)

# Fin backend/app/routers/reportes.py
