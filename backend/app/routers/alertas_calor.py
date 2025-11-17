# Inicio backend/app/routers/alertas_calor.py

# Importaciones necesarias para el router de alertas de calor
from fastapi import APIRouter, HTTPException, Depends, Body
from typing import Optional
from backend.models.alertas_calor_mdls import AlertaCalorModel
from backend.app.security.jwt_handler import verificar_token, verificar_rol
from backend.models.clima_mdls import ClimaModel
from backend.models.notificaciones_mdls import NotificacionModel


# Creación del router con prefijo y tags
router = APIRouter(prefix="/alertas_calor", tags=["Alertas de Calor"])

# Endpoint para crear alerta de calor (solo administradores)
@router.post("/")
def crear_alerta(temperatura: float = Body(...), humedad: float = Body(...), indice_uv: float = Body(...),
                  nivel_riesgo: str = Body(...), fuente: str = Body("OpenMeteo"),
                  datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        # Crear nueva alerta usando el modelo
        alerta = AlertaCalorModel.crear_alerta(temperatura, humedad, indice_uv, nivel_riesgo, fuente)
        return {"status": "success", "data": alerta}
    except HTTPException as e:
        raise e

# Endpoint para generar alerta automática desde datos climáticos (solo administradores)    
@router.post("/generar-desde-clima")
def generar_alerta_automatica(datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    clima = ClimaModel.obtener_clima("Cartagena")
    nivel_alerta = ClimaModel.evaluar_alerta_climatica(clima)
    clima["nivel_alerta"] = nivel_alerta

    # crear alerta en BD
    alerta = AlertaCalorModel.crear_alerta_desde_clima(clima)

    # mensaje de notificación
    mensaje = f"⚠️ ALERTA DE CALOR {nivel_alerta.upper()} — Temp: {clima['temperatura']}°C, UV: {clima['uv_index']}"

    NotificacionModel.crear_notificaciones_globales(mensaje)

    return {
        "status": "ok",
        "alerta": alerta,
        "notificaciones_enviadas": True
    }

# Endpoint para obtener la alerta actual (acceso público)
@router.get("/actual")
def alerta_actual():
    alerts = AlertaCalorModel.listar_alertas()
    
    # si no hay alertas
    if not alerts:
        return {"status": "success", "data": None}

    # última por fecha
    alerts_sorted = sorted(alerts, key=lambda x: x["fecha_alerta"], reverse=True)
    return {"status": "success", "data": alerts_sorted[0]}

# Endpoint para listar todas las alertas (acceso público)
@router.get("/")
def listar_alertas():
    return {"status": "success", "data": AlertaCalorModel.listar_alertas()}

# Endpoint para obtener alerta por ID (acceso público)
@router.get("/{id_alerta}")
def obtener_alerta(id_alerta: str):
    return {"status": "success", "data": AlertaCalorModel.obtener_alerta_por_id(id_alerta)}

# Endpoint para eliminar alerta (solo administradores)
@router.delete("/{id_alerta}")
def eliminar_alerta(id_alerta: str, datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        return AlertaCalorModel.eliminar_alerta(id_alerta)
    except HTTPException as e:
        raise e

# Fin backend/app/routers/alertas_calor.py
