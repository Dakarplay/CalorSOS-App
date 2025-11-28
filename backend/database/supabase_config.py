# Inicio supabase_config.py

# backend/database/supabase_config.py

# Importaciones necesarias para configuración de Supabase
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde archivo específico
load_dotenv(dotenv_path="calorsos.env")

# Obtener credenciales de Supabase desde variables de entorno
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Verificar que las credenciales estén disponibles
if not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError("No se encontraron las variables SUPABASE_URL o SUPABASE_KEY en calorsos.env")

# Crear cliente global de Supabase para toda la aplicación
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fin supabase_config.py
