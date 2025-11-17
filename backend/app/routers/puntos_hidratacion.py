# Inicio backend/app/routers/puntos_hidratacion.py

# Importaciones necesarias para el router de puntos de hidratación
from fastapi import APIRouter, HTTPException, Depends, Body
from backend.models.punto_hidratacion_mdls import PuntoHidratacionModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol
from typing import Optional

# Creación del router con prefijo y tags
router = APIRouter(prefix="/puntos_hidratacion", tags=["Puntos de Hidratación"])

# Endpoint para crear punto de hidratación (usuario autenticado)
@router.post("/")
def crear_punto(
    nombre: str,
    descripcion: Optional[str] = None,
    latitud: float = None,
    longitud: float = None,
    datos_usuario: dict = Depends(verificar_token),
    estado: str = "activa"
):
    """Permite a un usuario registrar un nuevo punto (estado = activa por defecto)."""

    try:
        # Estado por defecto para nuevos puntos
        estado = "activa"
        validado_por = None

        # Crear punto usando el modelo
        punto = PuntoHidratacionModel.crear_punto(
            nombre, descripcion, latitud, longitud, estado, validado_por
        )

        return {"status": "success", "data": punto}

    except HTTPException as e:
        raise e

# Endpoint para listar puntos (acceso público)
@router.get("/")
def listar_puntos(estado: Optional[str] = None):
    """Lista todos los puntos. Si estado es None, muestra todos; si no, filtra por estado."""

    if estado is None:
        # Mostrar todos los puntos sin filtro (para administradores)
        return {
            "status": "success",
            "data": PuntoHidratacionModel.listar_puntos(None)
        }
    else:
        # Filtrar por estado (para usuarios normales)
        return {
            "status": "success",
            "data": PuntoHidratacionModel.listar_puntos(estado)
        }

# Endpoint para obtener punto por ID
@router.get("/{id_punto}")
def obtener_punto(id_punto: str):
    return {
        "status": "success",
        "data": PuntoHidratacionModel.obtener_punto_por_id(id_punto)
    }

# Endpoint para actualizar punto (solo administradores)
@router.put("/{id_punto}")
def actualizar_punto(
    id_punto: str,
    data: dict = Body(...),
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    return {
        "status": "success",
        "data": PuntoHidratacionModel.actualizar_punto(id_punto, data)
    }

# Endpoint para eliminar punto (solo administradores)
@router.delete("/{id_punto}")
def eliminar_punto(
    id_punto: str,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    return PuntoHidratacionModel.eliminar_punto(id_punto)

# Fin backend/app/routers/puntos_hidratacion.py
