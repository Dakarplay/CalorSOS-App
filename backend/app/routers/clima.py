# backend/app/routers/clima.py
from fastapi import APIRouter, Query
from backend.models.clima_mdls import ClimaModel

router = APIRouter(prefix="/clima", tags=["Datos Climáticos"])

@router.get("/")
def obtener_clima(ciudad: str = "Cartagena"):
    """Información climática actual"""
    return ClimaModel.obtener_clima(ciudad)

@router.get("/historico")
def obtener_historico_temp_humedad(
    dias: int = Query(1, ge=1, le=7, description="Número de días históricos a consultar (1-7)")
):
    """Sensación térmica horaria de los últimos días"""
    return ClimaModel.obtener_historico_temp_humedad(dias)

@router.get("/historico-temp-humedad")
def clima_historico_temp_humedad(
    dias: int = Query(1, ge=1, le=7, description="Número de días históricos a consultar (1-7)")
):
    """Devuelve temperatura y humedad horaria de los últimos N días"""
    return ClimaModel.obtener_historico_temp_humedad(dias)
