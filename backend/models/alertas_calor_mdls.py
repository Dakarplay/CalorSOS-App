# Inicio alertas_calor_mdls.py

# backend/models/alertas_calor_mdls.py

# Importaciones necesarias para el modelo de alertas de calor
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from datetime import datetime, timedelta

# Clase principal para manejar alertas de calor
class AlertaCalorModel:
    """
    Modelo para interactuar con la tabla alertas_calor en Supabase.
    Gestiona creación, consulta y eliminación de alertas relacionadas con el calor.
    """

    # Método para crear una nueva alerta de calor
    @staticmethod
    def crear_alerta(temperatura: float, humedad: float, indice_uv: float,
                        nivel_riesgo: str, fuente: str = "OpenMeteo", estado: str = "activa"):
        try:
            data = {
                "temperatura": temperatura,
                "humedad": humedad,
                "indice_uv": indice_uv,
                "nivel_riesgo": nivel_riesgo,
                "fuente": fuente,
                "estado": estado,
            }

            response = supabase.table("alertas_calor").insert(data).execute()
            return response.data[0] if response.data else None

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear alerta de calor: {str(e)}")

    # Método para crear una alerta basada en datos climáticos
    @staticmethod
    def crear_alerta_desde_clima(clima: dict):
        """
        Previene alertas duplicadas: si ya existe una alerta igual en la última hora, no crea otra.
        """

        temperatura = clima.get("temperatura")
        humedad = clima.get("humedad")
        indice_uv = clima.get("uv_index")
        nivel = clima.get("nivel_alerta", "desconocido")

        # Buscar alertas similares en la última hora
        hace_una_hora = (datetime.utcnow() - timedelta(hours=1)).isoformat()

        existing = supabase.table("alertas_calor") \
            .select("*") \
            .eq("nivel_riesgo", nivel) \
            .gte("fecha_alerta", hace_una_hora) \
            .execute()

        if existing.data:
            return existing.data[0]  # ya existe alerta reciente → no duplicar

        # Crear nueva alerta
        nueva = AlertaCalorModel.crear_alerta(
            temperatura=temperatura,
            humedad=humedad,
            indice_uv=indice_uv,
            nivel_riesgo=nivel,
            estado="activa"
        )

        return nueva
    
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
