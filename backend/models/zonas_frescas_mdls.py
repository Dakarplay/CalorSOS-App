# Inicio zonas_frescas_mdls.py

# backend/models/zonas_frescas_mdls.py

# Importaciones necesarias para el modelo de zonas frescas
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional

# Clase principal para manejar zonas frescas
class ZonaFrescaModel:
    """
    Modelo para interactuar con la tabla zonas_frescas en Supabase.
    Gestiona creación, consulta, actualización y eliminación de zonas frescas.
    """

    @staticmethod
    def crear_zona(nombre: str, descripcion: Optional[str], latitud: float, longitud: float, tipo: str = "urbana", estado: str = "activa", validado_por: Optional[str] = None):
        """
        Crea una nueva zona fresca en la base de datos.
        Inserta los datos de la zona con coordenadas y tipo especificado.
        """
        try:
            # Preparar datos para inserción
            data = {
                "nombre": nombre,
                "descripcion": descripcion,
                "latitud": latitud,
                "longitud": longitud,
                "tipo": tipo,
                "estado": estado,
                "validado_por": validado_por
            }
            # Ejecutar inserción en Supabase
            response = supabase.table("zonas_frescas").insert(data).execute()
            # Retornar la zona creada
            return response.data[0] if response.data else None
        except Exception as e:
            # Manejar errores en la creación
            raise HTTPException(status_code=500, detail=f"Error al crear zona fresca: {str(e)}")

    @staticmethod
    def listar_zonas(estado: Optional[str] = None):
        """
        Lista todas las zonas frescas, con opción de filtrar por estado.
        Si estado es None, retorna todas las zonas.
        """
        try:
            # Construir consulta base
            query = supabase.table("zonas_frescas").select("*")
            # Aplicar filtro de estado si se especifica
            if estado is not None:
                query = query.eq("estado", estado)
            # Ejecutar consulta
            response = query.execute()
            return response.data
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al listar zonas: {str(e)}")

    @staticmethod
    def obtener_zona_por_id(id_zona: str):
        """
        Obtiene una zona fresca específica por su ID.
        Busca en la base de datos y retorna la zona si existe.
        """
        try:
            # Consultar zona por ID
            response = supabase.table("zonas_frescas").select("*").eq("id_zona", id_zona).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Zona fresca no encontrada")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener zona: {str(e)}")

    @staticmethod
    def actualizar_zona(id_zona: str, data: dict):
        """
        Actualiza la información de una zona fresca.
        Modifica los campos especificados en el diccionario data.
        """
        try:
            # Ejecutar actualización
            response = supabase.table("zonas_frescas").update(data).eq("id_zona", id_zona).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Zona no encontrada para actualizar")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la actualización
            raise HTTPException(status_code=500, detail=f"Error al actualizar zona: {str(e)}")

    @staticmethod
    def eliminar_zona(id_zona: str):
        """
        Elimina una zona fresca por su ID.
        Remueve el registro de la base de datos.
        """
        try:
            # Ejecutar eliminación
            response = supabase.table("zonas_frescas").delete().eq("id_zona", id_zona).execute()
            # Retornar mensaje de confirmación
            return {"message": "Zona eliminada correctamente"} if response.data else {"message": "No se encontró la zona"}
        except Exception as e:
            # Manejar errores en la eliminación
            raise HTTPException(status_code=500, detail=f"Error al eliminar zona: {str(e)}")

# Fin zonas_frescas_mdls.py
