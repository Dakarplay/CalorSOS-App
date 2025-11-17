# Inicio admin_mdls.py

# backend/models/admin_mdls.py

# Importaciones necesarias para el modelo administrativo
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from backend.models.punto_hidratacion_mdls import PuntoHidratacionModel
from backend.models.zonas_frescas_mdls import ZonaFrescaModel
from backend.models.reportes_mdls import ReporteModel

# Clase principal para operaciones administrativas
class AdminModel:
    """
    Modelo para operaciones administrativas relacionadas con los reportes.
    Maneja validación y rechazo de reportes enviados por usuarios.
    """

    @staticmethod
    def validar_reporte(id_reporte: str, admin_id: str):
        """
        Valida un reporte y lo convierte en zona fresca o punto de hidratación según su tipo.
        Obtiene el reporte, verifica su estado y crea la entidad correspondiente.
        """
        try:
            # Obtener el reporte completo desde la base de datos
            reporte = ReporteModel.obtener_reporte_por_id(id_reporte)

            # Verificar que el reporte esté pendiente de validación
            if reporte["estado"] != "pendiente":
                raise HTTPException(status_code=400, detail="El reporte ya ha sido procesado")

            # Procesar según el tipo de reporte
            if reporte["tipo"] == "zona_fresca":
                # Preparar datos para crear zona fresca
                zona_data = {
                    "nombre": reporte.get("nombre", "Zona Fresca Reportada"),
                    "descripcion": reporte.get("descripcion"),
                    "latitud": reporte["latitud"],
                    "longitud": reporte["longitud"],
                    "tipo": reporte.get("tipo_zona_fresca", "urbana"),
                    "estado": "activa",
                    "validado_por": admin_id
                }
                # Crear la nueva zona fresca
                nueva_zona = ZonaFrescaModel.crear_zona(**zona_data)

                # Eliminar el reporte después de crear la zona
                ReporteModel.eliminar_reporte(id_reporte)

                # Retornar resultado de la validación
                return {
                    "tipo": "zona_fresca",
                    "entidad_creada": nueva_zona,
                    "reporte_eliminado": reporte
                }

            elif reporte["tipo"] == "hidratacion":
                # Preparar datos para crear punto de hidratación
                punto_data = {
                    "nombre": reporte.get("nombre", "Punto de Hidratación Reportado"),
                    "descripcion": reporte.get("descripcion"),
                    "latitud": reporte["latitud"],
                    "longitud": reporte["longitud"],
                    "estado": "activa",
                    "validado_por": admin_id
                }
                # Crear el nuevo punto de hidratación
                nuevo_punto = PuntoHidratacionModel.crear_punto(**punto_data)

                # Eliminar el reporte después de crear el punto
                ReporteModel.eliminar_reporte(id_reporte)

                # Retornar resultado de la validación
                return {
                    "tipo": "hidratacion",
                    "entidad_creada": nuevo_punto,
                    "reporte_eliminado": reporte
                }

            else:
                # Tipo de reporte no soportado
                raise HTTPException(status_code=400, detail=f"Tipo de reporte '{reporte['tipo']}' no soportado")

        except HTTPException as e:
            # Re-lanzar excepciones HTTP conocidas
            raise e
        except Exception as e:
            # Manejar errores generales
            raise HTTPException(status_code=500, detail=f"Error al validar reporte: {str(e)}")

    @staticmethod
    def rechazar_reporte(id_reporte: str):
        """
        Rechaza un reporte eliminándolo completamente de la base de datos.
        Obtiene el reporte antes de eliminarlo para devolver información.
        """
        try:
            # Obtener el reporte antes de eliminarlo
            reporte = ReporteModel.obtener_reporte_por_id(id_reporte)

            # Eliminar el reporte de la base de datos
            ReporteModel.eliminar_reporte(id_reporte)

            # Retornar confirmación del rechazo
            return {
                "message": "Reporte rechazado y eliminado correctamente",
                "reporte_eliminado": reporte
            }

        except HTTPException as e:
            # Re-lanzar excepciones HTTP conocidas
            raise e
        except Exception as e:
            # Manejar errores generales
            raise HTTPException(status_code=500, detail=f"Error al rechazar reporte: {str(e)}")

# Fin admin_mdls.py
