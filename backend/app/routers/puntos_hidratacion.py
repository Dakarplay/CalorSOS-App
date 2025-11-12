from fastapi import APIRouter, HTTPException, Depends, Body
from backend.models.puntos_hidratacion_mdls import PuntoHidratacionModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol
from typing import Optional

router = APIRouter(prefix="/puntos_hidratacion", tags=["Puntos de Hidratación"])


# Crear punto (solo usuarios autenticados)
@router.post("/")
def crear_punto(
    nombre: str,
    direccion: str = None,
    latitud: float = None,
    longitud: float = None,
    fuente: str = "reporte ciudadano",
    datos_usuario: dict = Depends(verificar_token)
):
    """Permite a un usuario registrar un punto de hidratación (inicialmente pendiente)."""
    try:
        estado = "pendiente"
        validado_por = None
        punto = PuntoHidratacionModel.crear_punto(nombre, direccion, latitud, longitud, estado, fuente, validado_por)
        return {"status": "success", "data": punto}
    except HTTPException as e:
        raise e


# Listar puntos (público, sin restricciones)
@router.get("/")
def listar_puntos(estado: Optional[str] = None):
    """Lista todos los puntos (por defecto solo los activos)."""
    return {"status": "success", "data": PuntoHidratacionModel.listar_puntos(estado or "activo")}


# Obtener punto por ID (público)
@router.get("/{id_punto}")
def obtener_punto(id_punto: str):
    """Obtiene información de un punto de hidratación."""
    return {"status": "success", "data": PuntoHidratacionModel.obtener_punto_por_id(id_punto)}


# Actualizar punto (solo admin)
@router.put("/{id_punto}")
def actualizar_punto(
    id_punto: str,
    data: dict = Body(...),
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """Permite a un administrador modificar o validar un punto de hidratación."""
    return {"status": "success", "data": PuntoHidratacionModel.actualizar_punto(id_punto, data)}


# Eliminar punto (solo admin)
@router.delete("/{id_punto}")
def eliminar_punto(
    id_punto: str,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """Permite al administrador eliminar un punto de hidratación."""
    return PuntoHidratacionModel.eliminar_punto(id_punto)
