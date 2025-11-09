from fastapi import APIRouter
from ..supabase_client import supabase

router = APIRouter(prefix="/zonas_frescas", tags=["Zonas Frescas"])

@router.get("/")
def obtener_zonas():
    
    # Devuelve todas las zonas frescas registradas en la base de datos.
    response = supabase.table("zonas_frescas").select("*").execute()
    return {"data": response.data}
