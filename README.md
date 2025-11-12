# 🌡️ CalorSOS API Backend

## 🚀 Descripción
**CalorSOS** es una API (POR EL MOMENTO API) desarrollada en **FastAPI** para la gestión de información relacionada con puntos de hidratación, zonas frescas, reportes de calor y alertas climáticas.  
El sistema está completamente integrado con **Supabase** como base de datos y utiliza **JWT** para autenticación y control de roles (usuario / administrador).

---

## 🧱 Estructura del Proyecto
```
CALORSOS-APP/
│
├── .venv/                      # 💡 Entorno virtual de Python (no se sube a GitHub)
├── .gitignore                  # 🧹 Define qué archivos deben ignorarse en el control de versiones (ej: .venv/, __pycache__/)
├── calorsos.env                # 🔐 Archivo de variables de entorno con credenciales y llaves (Supabase, JWT_SECRET, API_KEY clima)
├── README.md                   # 📘 Documentación del proyecto: estructura, configuración y endpoints
│
├── backend/                    # ⚙️ Lógica del servidor (toda la API y conexión con la base de datos)
│   │
│   ├── __init__.py             # 🧩 Marca la carpeta como módulo de Python
│   ├── app/                    # 🚀 Núcleo de la aplicación FastAPI
│   │   ├── __init__.py         # 🧩 Indica que `app` es un paquete importable
│   │   ├── main.py             # 🏁 Punto de entrada principal del backend
│   │   │                       # - Crea la instancia de FastAPI
│   │   │                       # - Configura CORS
│   │   │                       # - Registra todos los routers de la API
│   │   │
│   │   ├── routers/            # 🌐 Módulos que definen las rutas (endpoints) del sistema
│   │   │    ├── __init__.py
│   │   │    ├── admin.py               # 🧠 Rutas exclusivas para validaciones y gestión de reportes (solo admin)
│   │   │    ├── alertas_calor.py       # ☀️ Rutas para crear, listar y eliminar alertas de calor
│   │   │    ├── clima.py               # 🌦️ Rutas que obtienen datos meteorológicos externos (públicas)
│   │   │    ├── notificaciones.py      # 🔔 Rutas de creación y lectura de notificaciones (según rol)
│   │   │    ├── puntos_hidratacion.py  # 💧 Rutas CRUD de los puntos de hidratación
│   │   │    ├── reportes.py            # 📝 Rutas CRUD de los reportes ciudadanos
│   │   │    ├── usuarios.py            # 👤 Registro, login, perfil y manejo de roles de usuarios
│   │   │    └── zonas_frescas.py       # 🌳 Rutas CRUD de zonas frescas del entorno
│   │   │
│   │   └── security/          # 🔒 Módulos encargados de la seguridad y autenticación
│   │       ├── __init__.py
│   │       ├── auth.py                 # 🧾 Dependencias para autenticación y autorización (uso de JWT y roles)
│   │       ├── hashing.py              # 🔑 Cifrado y verificación de contraseñas (bcrypt / passlib)
│   │       └── jwt_handler.py          # 🛡️ Generación y validación de tokens JWT
│   │
│   ├── database/              # 🗄️ Conexión con la base de datos Supabase
│   │   ├── __init__.py
│   │   └── supabase_config.py         # ⚙️ Inicializa el cliente Supabase usando las claves del archivo `.env`
│   │
│   └── models/                # 🧠 Modelos que manejan la lógica de base de datos
│       ├── __init__.py
│       ├── admin_mdls.py             # 🧠 Funciones para validar/rechazar reportes (rol admin)
│       ├── alertas_calor_mdls.py     # ☀️ CRUD y estructura de datos para alertas de calor
│       ├── clima_mdls.py             # 🌦️ Obtiene datos del clima desde una API externa
│       ├── notificaciones_mdls.py    # 🔔 Operaciones sobre la tabla de notificaciones (crear, listar, eliminar)
│       ├── puntos_hidratacion_mdls.py# 💧 CRUD de puntos de hidratación en Supabase
│       ├── reportes_mdls.py          # 📝 Inserción, actualización y eliminación de reportes ciudadanos
│       ├── usuarios_mdls.py          # 👤 Manejo de datos de usuario (crear, listar, actualizar, eliminar)
│       └── zonas_frescas_mdls.py     # 🌳 CRUD para zonas frescas (administración ambiental)
│
├── docs/                       # 📄 Carpeta destinada a documentación, diagramas o manuales del proyecto (vacía por ahora, pero se usará para manual técnico y API Reference) 
│
└── frontend/                   # 💻 Carpeta para la futura interfaz web o app móvil de CalorSOS (vacía por ahora, se integrará más adelante con el backend)

```

---

## ⚙️ Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Dakarplay/CalorSOS-App.git
cd CalorSOS-App
```

### 2️⃣ Crear entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate     # En Linux/Mac
.venv\Scripts\activate      # En Windows
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Crear archivo `.env` en la raíz
```env
SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_key
JWT_SECRET=tu_clave_secreta_segura
```

### 5️⃣ Ejecutar el servidor
```bash
uvicorn backend.app.main:app --reload --port 8000
```

### 6️⃣ Abrir la documentación interactiva
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔐 Autenticación JWT

### Flujo de autenticación:
1. Registrar usuario → `/usuarios/register`
2. Iniciar sesión → `/usuarios/login`
3. Copiar el token JWT recibido
4. En Swagger → “Authorize” → pegar `Bearer <tu_token>`

---

## 👥 Roles de usuario

| Rol | Descripción | Permisos principales |
|------|--------------|----------------------|
| **usuario** | Usuario común | Crear reportes, ver zonas frescas, puntos de hidratación |
| **admin** | Administrador del sistema | Validar reportes, crear alertas, eliminar o actualizar registros |

---

## 📡 Endpoints Principales

### 👤 Usuarios
| Método | Ruta | Acceso |
|--------|------|--------|
| POST | `/usuarios/register` | Público |
| POST | `/usuarios/login` | Público |
| GET | `/usuarios/perfil` | Token |
| GET | `/usuarios/` | Admin |
| PUT | `/usuarios/{id}` | Propietario / Admin |
| DELETE | `/usuarios/{id}` | Admin|

### 💧 Puntos de Hidratación
| Método | Ruta | Acceso |
|--------|------|--------|
| POST | `/puntos_hidratacion/` | Token |
| GET | `/puntos_hidratacion/` | Público |
| PUT | `/puntos_hidratacion/{id}` | Admin |
| DELETE | `/puntos_hidratacion/{id}` | Admin |

### 🌳 Zonas Frescas
| Método | Ruta | Acceso |
|--------|------|--------|
| POST | `/zonas_frescas/` | Token |
| GET | `/zonas_frescas/` | Público |
| PUT | `/zonas_frescas/{id}` | Admin |
| DELETE | `/zonas_frescas/{id}` | Admin |

### ☀️ Alertas de Calor
| Método | Ruta | Acceso |
|--------|------|--------|
| GET | `/alertas_calor/` | Público |
| POST | `/alertas_calor/` | Admin |
| DELETE | `/alertas_calor/{id}` | Admin |

### 🔔 Notificaciones
| Método | Ruta | Acceso |
|--------|------|--------|
| POST | `/notificaciones/` | Admin |
| GET | `/notificaciones/` | Token |
| PUT | `/notificaciones/{id}` | Admin |
| DELETE | `/notificaciones/{id}` | Admin |

### 🧠 Administración
| Método | Ruta | Acceso |
|--------|------|--------|
| PUT | `/admin/validar_reporte/{id}` | Admin |
| PUT | `/admin/rechazar_reporte/{id}` | Admin |

---

## 🧩 Dependencias principales
- **FastAPI** — Framework backend
- **Uvicorn** — Servidor ASGI
- **Supabase-py** — Conexión con Supabase
- **Passlib / Bcrypt** — Hash de contraseñas
- **PyJWT** — Manejo de tokens JWT

---

## 🧠 Desarrollado por
👤 **Dago David Palmera Navarro**  
💻 Proyecto académico – Ingeniería de Sistemas  
📆 Año: 2025  
