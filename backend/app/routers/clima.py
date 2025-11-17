# Inicio backend/app/routers/clima.py

# Importaciones necesarias para el router de clima
from fastapi import APIRouter, Query
from backend.models.clima_mdls import ClimaModel

# Creación del router con prefijo y tags
router = APIRouter(prefix="/clima", tags=["Datos Climáticos"])

# Endpoint para obtener información climática actual
@router.get("/")
def obtener_clima(ciudad: str = "Cartagena"):
    """Información climática actual"""
    return ClimaModel.obtener_clima(ciudad)

# Endpoint para obtener histórico de sensación térmica
@router.get("/historico")
def obtener_historico_temp_humedad(
    dias: int = Query(1, ge=1, le=7, description="Número de días históricos a consultar (1-7)")
):
    """Sensación térmica horaria de los últimos días"""
    return ClimaModel.obtener_historico_temp_humedad(dias)

# Endpoint para obtener histórico de temperatura y humedad
@router.get("/historico-temp-humedad")
def clima_historico_temp_humedad(
    dias: int = Query(1, ge=1, le=7, description="Número de días históricos a consultar (1-7)")
):
    """Devuelve temperatura y humedad horaria de los últimos N días"""
    return ClimaModel.obtener_historico_temp_humedad(dias)

# Fin backend/app/routers/clima.py
