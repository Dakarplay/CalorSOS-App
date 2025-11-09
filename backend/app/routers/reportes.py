from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..supabase_client import supabase

router = APIRouter(prefix="/reportes", tags=["Reportes Comunitarios"])

class Reporte(BaseModel):
    descripcion: str
    ubicacion: str
    foto_url: str | None = None

@router.post("/")
def crear_reporte(reporte: Reporte):
    
    # Permite a los usuarios enviar un reporte comunitario de puntos de agua o riesgos.
    try:
        data = reporte.dict()
        data["estado"] = "pendiente"
        response = supabase.table("reportes").insert(data).execute()
        return {"message": "Reporte enviado correctamente", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear reporte: {str(e)}")
