# Inicio backend/app/routers/zonas_frescas.py

# Importaciones necesarias para el router de zonas frescas
from fastapi import APIRouter, HTTPException, Depends, Body
from backend.models.zonas_frescas_mdls import ZonaFrescaModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol
from typing import Optional

# Creación del router con prefijo y tags
router = APIRouter(prefix="/zonas_frescas", tags=["Zonas Frescas"])

# Endpoint para crear zona fresca (usuario autenticado)
@router.post("/")
def crear_zona(
    nombre: str,
    descripcion: str = None,
    latitud: float = None,
    longitud: float = None,
    tipo: str = "urbana",
    estado: str = "activa",
    datos_usuario: dict = Depends(verificar_token)
):
    """Crea una nueva zona fresca (solo usuarios autenticados)."""
    try:
        # Estado inicial para nuevas zonas
        validado_por = None

        # Crear zona usando el modelo
        zona = ZonaFrescaModel.crear_zona(nombre, descripcion, latitud, longitud, tipo, estado, validado_por)
        return {"status": "success", "data": zona}
    except HTTPException as e:
        raise e

# Endpoint para listar zonas (acceso público)
@router.get("/")
def listar_zonas(estado: Optional[str] = None):
    """Lista todas las zonas frescas. Si estado es None, muestra todas; si no, filtra por estado."""
    if estado is None:
        # Mostrar todas las zonas sin filtro (para administradores)
        return {"status": "success", "data": ZonaFrescaModel.listar_zonas(None)}
    else:
        # Filtrar por estado (para usuarios normales)
        return {"status": "success", "data": ZonaFrescaModel.listar_zonas(estado)}

# Endpoint para obtener zona por ID (acceso público)
@router.get("/{id_zona}")
def obtener_zona(id_zona: str):
    """Obtiene una zona fresca por su ID (público)."""
    return {"status": "success", "data": ZonaFrescaModel.obtener_zona_por_id(id_zona)}

# Endpoint para actualizar zona (solo administradores)
@router.put("/{id_zona}")
def actualizar_zona(
    id_zona: str,
    data: dict = Body(...),
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """Actualiza una zona fresca (solo administradores)."""
    return {"status": "success", "data": ZonaFrescaModel.actualizar_zona(id_zona, data)}

# Endpoint para eliminar zona (solo administradores)
@router.delete("/{id_zona}")
def eliminar_zona(
    id_zona: str,
    datos_usuario: dict = Depends(verificar_rol(["admin"]))
):
    """Elimina una zona fresca (solo administradores)."""
    return ZonaFrescaModel.eliminar_zona(id_zona)

# Fin backend/app/routers/zonas_frescas.py
