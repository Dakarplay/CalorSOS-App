# backend/routers/clima.py
from fastapi import APIRouter, HTTPException
from backend.models.clima_mdls import ClimaModel

router = APIRouter(prefix="/clima", tags=["Datos Climáticos"])

@router.get("/")
def obtener_clima(ciudad: str = "Cartagena"):
    """Obtiene información climática actual (temperatura, humedad, condición, etc.)."""
    try:
        clima = ClimaModel.obtener_clima(ciudad)
        return {"status": "success", "data": clima}
    except HTTPException as e:
        raise e
