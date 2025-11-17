# Inicio reportes_mdls.py

# backend/models/reportes_mdls.py

# Importaciones necesarias para el modelo de reportes
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional

# Clase principal para manejar reportes
class ReporteModel:
    """
    Modelo para interactuar con la tabla reportes en Supabase.
    Gestiona creación, consulta, actualización y eliminación de reportes de usuarios.
    """

    @staticmethod
    def crear_reporte(
        id_usuario: str,
        tipo: str,
        nombre: Optional[str] = None,
        descripcion: Optional[str] = None,
        latitud: Optional[float] = None,
        longitud: Optional[float] = None,
        tipo_zona_fresca: Optional[str] = None,
        estado: str = "pendiente"
    ):
        """
        Crea un nuevo reporte en la base de datos.
        Inserta los datos del reporte con campos opcionales según el tipo.
        """
        try:
            # Preparar datos base obligatorios
            data = {
                "id_usuario": id_usuario,
                "tipo": tipo,
                "estado": estado
            }

            # Agregar campos opcionales si están presentes
            if nombre is not None:
                data["nombre"] = nombre
            if descripcion is not None:
                data["descripcion"] = descripcion
            if latitud is not None:
                data["latitud"] = latitud
            if longitud is not None:
                data["longitud"] = longitud

            # Campo específico para zonas frescas
            if tipo == "zona_fresca":
                data["tipo_zona_fresca"] = tipo_zona_fresca
            else:
                data["tipo_zona_fresca"] = None

            # Ejecutar inserción en Supabase
            response = supabase.table("reportes").insert(data).execute()
            # Retornar el reporte creado
            return response.data[0] if response.data else None

        except Exception as e:
            # Manejar errores en la creación
            raise HTTPException(status_code=500, detail=f"Error al crear reporte: {str(e)}")

    @staticmethod
    def listar_reportes(
        id_usuario: Optional[str] = None,
        tipo: Optional[str] = None,
        estado: Optional[str] = None
    ):
        """
        Lista reportes con filtros opcionales por usuario, tipo y estado.
        Permite filtrar la lista de reportes según criterios específicos.
        """
        try:
            # Construir consulta base
            query = supabase.table("reportes").select("*")

            # Aplicar filtros opcionales
            if id_usuario:
                query = query.eq("id_usuario", id_usuario)
            if tipo:
                query = query.eq("tipo", tipo)
            if estado:
                query = query.eq("estado", estado)

            # Ejecutar consulta
            response = query.execute()
            return response.data

        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al listar reportes: {str(e)}")

    @staticmethod
    def obtener_reporte_por_id(id_reporte: str):
        """
        Obtiene un reporte específico por su ID.
        Busca en la base de datos y retorna el reporte si existe.
        """
        try:
            # Consultar reporte por ID
            response = supabase.table("reportes").select("*").eq("id_reporte", id_reporte).execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Reporte no encontrado")

            return response.data[0]

        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener reporte: {str(e)}")

    @staticmethod
    def actualizar_reporte(id_reporte: str, data: dict):
        """
        Actualiza un reporte existente con los datos proporcionados.
        Solo los campos incluidos en 'data' serán actualizados.
        """
        try:
            # Ejecutar actualización
            response = supabase.table("reportes").update(data).eq("id_reporte", id_reporte).execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Reporte no encontrado para actualizar")

            return response.data[0]

        except Exception as e:
            # Manejar errores en la actualización
            raise HTTPException(status_code=500, detail=f"Error al actualizar reporte: {str(e)}")

    @staticmethod
    def eliminar_reporte(id_reporte: str):
        """
        Elimina un reporte por su ID.
        Remueve el registro de la base de datos.
        """
        try:
            # Ejecutar eliminación
            response = supabase.table("reportes").delete().eq("id_reporte", id_reporte).execute()
            # Retornar mensaje de confirmación
            return {"message": "Reporte eliminado correctamente"} if response.data else {"message": "No se encontró el reporte"}

        except Exception as e:
            # Manejar errores en la eliminación
            raise HTTPException(status_code=500, detail=f"Error al eliminar reporte: {str(e)}")

# Fin reportes_mdls.py
