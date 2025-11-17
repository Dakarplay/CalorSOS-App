# Inicio main.py

# backend/app/main.py

# Importaciones necesarias para la aplicación FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar routers desde la carpeta de routers
from backend.app.routers import (
    usuarios,
    puntos_hidratacion,
    zonas_frescas,
    alertas_calor,
    notificaciones,
    reportes,
    admin,
    clima,
)

# Crear instancia de la aplicación FastAPI
app = FastAPI(title="CalorSOS API")

# Configurar middleware CORS para permitir acceso desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplazar con el dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar todos los routers en la aplicación
app.include_router(usuarios.router)
app.include_router(puntos_hidratacion.router)
app.include_router(zonas_frescas.router)
app.include_router(alertas_calor.router)
app.include_router(notificaciones.router)
app.include_router(reportes.router)
app.include_router(admin.router)
app.include_router(clima.router)

@app.get("/")
def root():
    """
    Endpoint raíz que confirma que la API está funcionando.
    Retorna un mensaje de estado.
    """
    return {"message": "API CalorSOS funcionando correctamente"}

# Fin main.py
