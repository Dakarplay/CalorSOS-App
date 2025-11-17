# Inicio punto_hidratacion_mdls.py

# backend/models/punto_hidratacion_mdls.py

# Importaciones necesarias para el modelo de puntos de hidratación
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional

# Clase principal para manejar puntos de hidratación
class PuntoHidratacionModel:
    """
    Modelo para interactuar con la tabla puntos_hidratacion en Supabase.
    Gestiona creación, consulta, actualización y eliminación de puntos de hidratación.
    """

    @staticmethod
    def crear_punto(nombre: str, descripcion: Optional[str], latitud: float, longitud: float,
                    estado: str = "activa", validado_por: Optional[str] = None):
        """
        Inserta un nuevo punto de hidratación en la base de datos.
        Crea el registro con los datos proporcionados.
        """
        try:
            # Preparar datos para inserción
            data = {
                "nombre": nombre,
                "descripcion": descripcion,
                "latitud": latitud,
                "longitud": longitud,
                "estado": estado,
                "validado_por": validado_por
                # fecha_registro se genera automáticamente en la BD
            }

            # Ejecutar inserción en Supabase
            response = supabase.table("puntos_hidratacion").insert(data).execute()
            # Retornar el punto creado
            return response.data[0] if response.data else None

        except Exception as e:
            # Manejar errores en la creación
            raise HTTPException(status_code=500, detail=f"Error al crear punto de hidratación: {str(e)}")

    @staticmethod
    def listar_puntos(estado: Optional[str] = None):
        """
        Obtiene todos los puntos de hidratación, con opción de filtrar por estado.
        Si estado es None, retorna todos los puntos.
        """
        try:
            # Construir consulta base
            query = supabase.table("puntos_hidratacion").select("*")

            # Aplicar filtro de estado si se especifica
            if estado is not None:
                query = query.eq("estado", estado)

            # Ejecutar consulta
            response = query.execute()
            return response.data

        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al listar puntos: {str(e)}")

    @staticmethod
    def obtener_punto_por_id(id_punto: str):
        """
        Obtiene un punto de hidratación específico por su ID.
        Busca en la base de datos y retorna el punto si existe.
        """
        try:
            # Consultar punto por ID
            response = supabase.table("puntos_hidratacion")\
                .select("*").eq("id_punto", id_punto).execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Punto de hidratación no encontrado")

            return response.data[0]

        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener punto: {str(e)}")

    @staticmethod
    def actualizar_punto(id_punto: str, data: dict):
        """
        Actualiza la información de un punto de hidratación.
        Modifica los campos especificados en el diccionario data.
        """
        try:
            # Ejecutar actualización
            response = supabase.table("puntos_hidratacion")\
                .update(data).eq("id_punto", id_punto).execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Punto no encontrado para actualizar")

            return response.data[0]

        except Exception as e:
            # Manejar errores en la actualización
            raise HTTPException(status_code=500, detail=f"Error al actualizar punto: {str(e)}")

    @staticmethod
    def eliminar_punto(id_punto: str):
        """
        Elimina un punto de hidratación por su ID.
        Remueve el registro de la base de datos.
        """
        try:
            # Ejecutar eliminación
            supabase.table("puntos_hidratacion").delete().eq("id_punto", id_punto).execute()
            # Retornar mensaje de confirmación
            return {"message": "Punto eliminado correctamente"}

        except Exception as e:
            # Manejar errores en la eliminación
            raise HTTPException(status_code=500, detail=f"Error al eliminar punto: {str(e)}")

# Fin punto_hidratacion_mdls.py
