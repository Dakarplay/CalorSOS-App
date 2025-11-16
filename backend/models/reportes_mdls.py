# backend/models/reportes_mdls.py
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional

class ReporteModel:
    """Modelo para interactuar con la tabla reportes en Supabase."""

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
        try:
            data = {
                "id_usuario": id_usuario,
                "tipo": tipo,
                "estado": estado
            }

            if nombre is not None:
                data["nombre"] = nombre
            if descripcion is not None:
                data["descripcion"] = descripcion
            if latitud is not None:
                data["latitud"] = latitud
            if longitud is not None:
                data["longitud"] = longitud

            if tipo == "zona_fresca" and tipo_zona_fresca is not None:
                data["tipo_zona_fresca"] = tipo_zona_fresca   # 👈 SOLO si aplica

            response = supabase.table("reportes").insert(data).execute()
            return response.data[0] if response.data else None

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear reporte: {str(e)}")


    @staticmethod
    def listar_reportes(
        id_usuario: Optional[str] = None,
        tipo: Optional[str] = None,
        estado: Optional[str] = None
    ):
        """Lista reportes, con filtros opcionales por id_usuario, tipo y estado."""
        try:
            query = supabase.table("reportes").select("*")

            if id_usuario:
                query = query.eq("id_usuario", id_usuario)
            if tipo:
                query = query.eq("tipo", tipo)
            if estado:
                query = query.eq("estado", estado)

            response = query.execute()
            return response.data

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al listar reportes: {str(e)}")

    @staticmethod
    def obtener_reporte_por_id(id_reporte: str):
        """Obtiene un reporte por su id_reporte."""
        try:
            response = supabase.table("reportes").select("*").eq("id_reporte", id_reporte).execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Reporte no encontrado")

            return response.data[0]

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener reporte: {str(e)}")

    @staticmethod
    def actualizar_reporte(id_reporte: str, data: dict):
        """Actualiza un reporte existente. Solo campos incluidos en 'data' serán actualizados."""
        try:
            response = supabase.table("reportes").update(data).eq("id_reporte", id_reporte).execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Reporte no encontrado para actualizar")

            return response.data[0]

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar reporte: {str(e)}")

    @staticmethod
    def eliminar_reporte(id_reporte: str):
        """Elimina un reporte por su id_reporte."""
        try:
            response = supabase.table("reportes").delete().eq("id_reporte", id_reporte).execute()
            return {"message": "Reporte eliminado correctamente"} if response.data else {"message": "No se encontró el reporte"}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar reporte: {str(e)}")
