# Inicio supabase_config.py

# backend/database/supabase_config.py

# Importaciones necesarias para configuración de Supabase
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde archivo específico
load_dotenv(dotenv_path="calorsos.env")

# Obtener credenciales de Supabase desde variables de entorno
VITE_SUPABASE_URL = os.getenv("VITE_SUPABASE_URL")
VITE_SUPABASE_KEY = os.getenv("VITE_SUPABASE_KEY")

# Verificar que las credenciales estén disponibles
if not VITE_SUPABASE_URL or not VITE_SUPABASE_KEY:
    raise EnvironmentError("No se encontraron las variables VITE_SUPABASE_URL o VITE_SUPABASE_KEY en calorsos.env")

# Crear cliente global de Supabase para toda la aplicación
supabase: Client = create_client(VITE_SUPABASE_URL, VITE_SUPABASE_KEY)

# Fin supabase_config.py
