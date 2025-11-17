# Inicio alertas_calor_mdls.py

# backend/models/alertas_calor_mdls.py

# Importaciones necesarias para el modelo de alertas de calor
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional

# Clase principal para manejar alertas de calor
class AlertaCalorModel:
    """
    Modelo para interactuar con la tabla alertas_calor en Supabase.
    Gestiona creación, consulta y eliminación de alertas relacionadas con el calor.
    """

    @staticmethod
    def crear_alerta(temperatura: float, humedad: float, indice_uv: float,
                    nivel_riesgo: str, fuente: str = "OpenWeatherMap"):
        """
        Crea una nueva alerta de calor en la base de datos.
        Inserta los datos proporcionados en la tabla alertas_calor.
        """
        try:
            # Preparar datos para la inserción
            data = {
                "temperatura": temperatura,
                "humedad": humedad,
                "indice_uv": indice_uv,
                "nivel_riesgo": nivel_riesgo,
                "fuente": fuente
            }
            # Ejecutar inserción en Supabase
            response = supabase.table("alertas_calor").insert(data).execute()
            # Retornar el registro creado o None si falla
            return response.data[0] if response.data else None
        except Exception as e:
            # Manejar errores durante la creación
            raise HTTPException(status_code=500, detail=f"Error al crear alerta de calor: {str(e)}")

    @staticmethod
    def listar_alertas():
        """
        Obtiene todas las alertas de calor registradas.
        Retorna una lista de todas las alertas en la base de datos.
        """
        try:
            # Consultar todas las alertas
            response = supabase.table("alertas_calor").select("*").execute()
            return response.data
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al listar alertas: {str(e)}")

    @staticmethod
    def obtener_alerta_por_id(id_alerta: str):
        """
        Obtiene una alerta específica por su ID.
        Busca la alerta en la base de datos y la retorna si existe.
        """
        try:
            # Consultar alerta por ID
            response = supabase.table("alertas_calor").select("*").eq("id_alerta", id_alerta).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Alerta no encontrada")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener alerta: {str(e)}")

    @staticmethod
    def eliminar_alerta(id_alerta: str):
        """
        Elimina una alerta de calor existente.
        Remueve la alerta de la base de datos por su ID.
        """
        try:
            # Ejecutar eliminación
            response = supabase.table("alertas_calor").delete().eq("id_alerta", id_alerta).execute()
            # Retornar mensaje de confirmación
            return {"message": "Alerta eliminada correctamente"} if response.data else {"message": "No se encontró la alerta"}
        except Exception as e:
            # Manejar errores en la eliminación
            raise HTTPException(status_code=500, detail=f"Error al eliminar alerta: {str(e)}")

# Fin alertas_calor_mdls.py
