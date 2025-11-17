# Inicio backend/app/routers/admin.py

# Importaciones necesarias para el router de administración
from fastapi import APIRouter, HTTPException, Depends
from backend.models.admin_mdls import AdminModel
from backend.app.security.jwt_handler import verificar_rol

# Creación del router con prefijo y tags
router = APIRouter(prefix="/admin", tags=["Administración"])

# Endpoint para validar reportes
@router.put("/validar_reporte/{id_reporte}")
def validar_reporte(id_reporte: str, datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        # Obtener ID del administrador
        admin_id = datos_usuario["id_usuario"]

        # Validar el reporte usando el modelo
        resultado = AdminModel.validar_reporte(id_reporte, admin_id)

        # Determinar tipo de entidad creada
        tipo_entidad = resultado["tipo"]
        entidad = resultado["entidad_creada"]

        # Mensaje según el tipo de entidad
        if tipo_entidad == "zona_fresca":
            mensaje = "Reporte validado y zona fresca creada correctamente"
        elif tipo_entidad == "hidratacion":
            mensaje = "Reporte validado y punto de hidratación creado correctamente"
        else:
            mensaje = "Reporte validado correctamente"

        # Respuesta exitosa
        return {
            "status": "success",
            "message": mensaje,
            "data": resultado
        }
    except HTTPException as e:
        raise e

# Endpoint para rechazar reportes
@router.put("/rechazar_reporte/{id_reporte}")
def rechazar_reporte(id_reporte: str, datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    try:
        # Rechazar el reporte usando el modelo
        reporte = AdminModel.rechazar_reporte(id_reporte)

        # Respuesta exitosa
        return {"status": "success", "message": "Reporte rechazado correctamente", "data": reporte}
    except HTTPException as e:
        raise e

# Fin backend/app/routers/admin.py
