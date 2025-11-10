# backend/routers/alertas_calor.py
from fastapi import APIRouter, HTTPException
from backend.models.alertas_calor_mdls import AlertaCalorModel

router = APIRouter(prefix="/alertas_calor", tags=["Alertas de Calor"])

@router.post("/")
def crear_alerta(temperatura: float, humedad: float, indice_uv: float, nivel_riesgo: str, fuente: str = "OpenWeatherMap"):
    """Crea una nueva alerta de calor."""
    try:
        alerta = AlertaCalorModel.crear_alerta(temperatura, humedad, indice_uv, nivel_riesgo, fuente)
        return {"status": "success", "data": alerta}
    except HTTPException as e:
        raise e

@router.get("/")
def listar_alertas():
    """Lista todas las alertas de calor registradas."""
    return {"status": "success", "data": AlertaCalorModel.listar_alertas()}

@router.get("/{id_alerta}")
def obtener_alerta(id_alerta: str):
    """Obtiene una alerta de calor específica por su ID."""
    return {"status": "success", "data": AlertaCalorModel.obtener_alerta_por_id(id_alerta)}

@router.delete("/{id_alerta}")
def eliminar_alerta(id_alerta: str):
    """Elimina una alerta de calor existente."""
    return AlertaCalorModel.eliminar_alerta(id_alerta)
