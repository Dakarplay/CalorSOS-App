# Inicio notificaciones_mdls.py

# backend/models/notificaciones_mdls.py

# Importaciones necesarias para el modelo de notificaciones
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional
from datetime import datetime, timedelta

# Clase principal para manejar notificaciones
class NotificacionModel:
    """
    Modelo para interactuar con la tabla notificaciones en Supabase.
    Gestiona creación, consulta, actualización y eliminación de notificaciones.
    """
    # Crear una nueva notificación
    @staticmethod
    def crear_notificacion(id_usuario: str, mensaje: str, estado: str = "pendiente"):
        """
        Crea una nueva notificación para un usuario específico.
        Args:
            id_usuario (str): ID del usuario destinatario.
        """
        try:
            data = {
                "id_usuario": id_usuario,
                "mensaje": mensaje,
                "estado": estado,
            }

            response = supabase.table("notificaciones").insert(data).execute()
            return response.data[0] if response.data else None

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear notificación: {str(e)}")

    # Crear notificaciones globales sin spam
    @staticmethod
    def crear_notificaciones_globales(mensaje):
        """
        Evita spam: no genera la misma notificación más de 1 vez por hora.
        """

        hace_una_hora = (datetime.utcnow() - timedelta(hours=1)).isoformat()

        # ¿Ya se envió este mensaje recientemente?
        ya_existe = supabase.table("notificaciones") \
            .select("*") \
            .eq("mensaje", mensaje) \
            .gte("fecha_envio", hace_una_hora) \
            .execute()

        if ya_existe.data:
            return ya_existe.data # no repetir si ya existe

        # Enviar a todos
        usuarios = supabase.table("usuarios").select("id_usuario").execute().data
        notifs = []

        for u in usuarios:
            item = {
                "id_usuario": u["id_usuario"],
                "mensaje": mensaje,
                "estado": "pendiente",
            }

            res = supabase.table("notificaciones").insert(item).execute()
            notifs.append(res.data[0])

        return notifs
    
    @staticmethod
    def listar_notificaciones(id_usuario: Optional[str] = None):
        """
        Lista todas las notificaciones o filtra por usuario específico.
        Si se proporciona id_usuario, retorna solo sus notificaciones.
        """
        try:
            # Construir consulta base
            query = supabase.table("notificaciones").select("*")
            # Aplicar filtro si se especifica usuario
            if id_usuario:
                query = query.eq("id_usuario", id_usuario)
            # Ejecutar consulta
            response = query.execute()
            return response.data
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al listar notificaciones: {str(e)}")

    @staticmethod
    def obtener_notificacion_por_id(id_notificacion: str):
        """
        Obtiene una notificación específica por su ID.
        Busca en la base de datos y retorna la notificación si existe.
        """
        try:
            # Consultar notificación por ID
            response = supabase.table("notificaciones").select("*").eq("id_notificacion", id_notificacion).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Notificación no encontrada")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener notificación: {str(e)}")

    @staticmethod
    def actualizar_estado(id_notificacion: str, estado: str):
        """
        Actualiza el estado de una notificación.
        Cambia el estado (ej. pendiente a enviada) por ID.
        """
        try:
            # Ejecutar actualización de estado
            response = supabase.table("notificaciones").update({"estado": estado}).eq("id_notificacion", id_notificacion).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Notificación no encontrada para actualizar")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la actualización
            raise HTTPException(status_code=500, detail=f"Error al actualizar notificación: {str(e)}")

    @staticmethod
    def eliminar_notificacion(id_notificacion: str):
        """
        Elimina una notificación por su ID.
        Remueve el registro de la base de datos.
        """
        try:
            # Ejecutar eliminación
            response = supabase.table("notificaciones").delete().eq("id_notificacion", id_notificacion).execute()
            # Retornar mensaje de confirmación
            return {"message": "Notificación eliminada correctamente"} if response.data else {"message": "No se encontró la notificación"}
        except Exception as e:
            # Manejar errores en la eliminación
            raise HTTPException(status_code=500, detail=f"Error al eliminar notificación: {str(e)}")

# Fin notificaciones_mdls.py
