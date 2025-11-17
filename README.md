<!-- Inicio README.md -->

<!-- README.md -->

<!-- Archivo de documentación principal del proyecto CalorSOS -->

# CalorSOS - Sistema de Gestión de Calor Extremo

## Descripción del Proyecto

**CalorSOS** es una aplicación web completa desarrollada para ayudar a la ciudadanía en situaciones de calor extremo en Cartagena, Colombia. El sistema permite a los usuarios acceder a información vital sobre puntos de hidratación, zonas frescas, reportes ciudadanos, alertas climáticas y consejos de prevención, facilitando la toma de decisiones informadas para proteger la salud en condiciones de altas temperaturas.

El proyecto consta de dos componentes principales:
- **Backend**: API REST desarrollada en FastAPI que maneja la lógica de negocio, autenticación y conexión con la base de datos.
- **Frontend**: Interfaz de usuario desarrollada en React con Vite que proporciona una experiencia intuitiva y responsiva.

## Fin del Proyecto

El objetivo principal de CalorSOS es contribuir a la reducción de riesgos asociados con el calor extremo mediante:
- Información accesible sobre recursos de hidratación y zonas frescas.
- Sistema de reportes ciudadanos para identificar nuevas necesidades.
- Alertas climáticas en tiempo real basadas en datos meteorológicos.
- Consejos preventivos y educativos sobre el manejo del calor.
- Gestión administrativa eficiente para mantener la información actualizada.

## Funcionalidades Principales

### Para Usuarios Comunes
- Registro y autenticación de usuarios.
- Visualización de puntos de hidratación en mapa interactivo.
- Consulta de zonas frescas disponibles.
- Creación de reportes ciudadanos sobre necesidades de hidratación o zonas frescas.
- Recepción de notificaciones sobre alertas climáticas.
- Acceso a consejos y recomendaciones de prevención.
- Perfil personal para gestionar información.

### Para Administradores
- Validación y gestión de reportes ciudadanos.
- Creación y administración de puntos de hidratación.
- Gestión de zonas frescas.
- Emisión de alertas climáticas.
- Administración de usuarios y roles.
- Envío de notificaciones a usuarios.

### Funcionalidades Generales
- Datos climáticos en tiempo real desde APIs externas.
- Mapa interactivo con Leaflet para visualización geográfica.
- Sistema de autenticación JWT con roles.
- Interfaz responsiva y accesible.
- Integración completa con base de datos Supabase.

## Tecnologías Utilizadas

### Backend
- **FastAPI**: Framework web moderno y rápido para APIs REST.
- **Supabase**: Base de datos PostgreSQL como servicio con autenticación integrada.
- **Python 3.11.9**: Lenguaje de programación principal.
- **JWT**: Autenticación basada en tokens.
- **Bcrypt**: Hashing seguro de contraseñas.
- **Open-Meteo API**: Fuente de datos climáticos.

### Frontend
- **React 18**: Biblioteca para interfaces de usuario.
- **Vite**: Herramienta de construcción rápida para desarrollo moderno.
- **Leaflet**: Biblioteca para mapas interactivos.
- **Axios**: Cliente HTTP para comunicación con la API.
- **CSS Modules**: Estilos modulares y organizados.
- **React Router**: Navegación entre páginas.

### Infraestructura
- **Git**: Control de versiones.
- **VS Code**: Entorno de desarrollo integrado.
- **Postman/Swagger**: Pruebas y documentación de API.

## Estructura del Proyecto

```
CalorSOS-App/
│
├── .gitignore                  # Configuración de archivos ignorados en Git
├── calorsos.env                # Archivo que contiene la informacion que necesita la api de supabase y la clave JWT
├── README.md                   # Documentación principal del proyecto
├── requirements.txt            # Dependencias de Python para el backend
│
├── backend/                    # Lógica del servidor y API
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py             # Punto de entrada principal de FastAPI
│   │   ├── routers/            # Definición de endpoints de la API
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── alertas_calor.py
│   │   │   ├── clima.py
│   │   │   ├── notificaciones.py
│   │   │   ├── puntos_hidratacion.py
│   │   │   ├── reportes.py
│   │   │   ├── usuarios.py
│   │   │   └── zonas_frescas.py
│   │   └── security/           # Módulos de seguridad y autenticación
│   │       ├── __init__.py
│   │       ├── hashing.py
│   │       └── jwt_handler.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── supabase_config.py  # Configuración de conexión a Supabase
│   └── models/                 # Modelos de datos y lógica de negocio
│       ├── __init__.py
│       ├── admin_mdls.py
│       ├── alertas_calor_mdls.py
│       ├── clima_mdls.py
│       ├── notificaciones_mdls.py
│       ├── punto_hidratacion_mdls.py
│       ├── reportes_mdls.py
│       ├── usuarios_mdls.py
│       └── zonas_frescas_mdls.py
│
├── frontend/                   # Interfaz de usuario
│   ├── index.html              # Punto de entrada HTML
|   ├── node_modules            # Carpeta con los modulos de Node.js
│   ├── package.json            # Configuración de dependencias de Node.js
│   ├── package-lock.json       # Lock de versiones de dependencias
│   ├── vite.config.js          # Configuración de Vite
│   └── src/
│       ├── app.jsx             # Componente raíz de la aplicación
│       ├── main.jsx            # Punto de entrada de React
│       ├── assets/
│       │   ├── images/
│       │   │   └── logo.svg
│       │   └── styles/         # Estilos CSS organizados
│       │       ├── Admin.css 
│       │       ├── Alertas.css
│       │       ├── Auth.css
│       │       ├── ClimateChart.css
│       │       ├── Configuracion.css
│       │       ├── Consejos.css
│       │       ├── global.css
│       │       ├── Home.css
│       │       ├── IndicatorsPanel.css
│       │       ├── NavbarSmart.css
│       │       ├── Perfil.css
│       │       ├── PuntosHidratacion.css
│       │       ├── ReportCTA.css
│       │       ├── StatCard.css
│       │       └── ZonasFrescas.css
│       ├── components/         # Componentes reutilizables
│       │   ├── common/
│       │   │   └── LoaderPremium.jsx
│       │   ├── maps/
│       │   │   ├── MapFullscreenModal.css
│       │   │   ├── MapFullscreenModal.jsx
│       │   │   ├── MapView.css
│       │   │   └── MapView.jsx
│       │   ├── report/
│       │   │   ├── ReportForm.jsx
│       │   │   ├── ReportModal.css
│       │   │   └── ReportModal.jsx
│       │   └── ui/
│       │       ├── ClimateChart.jsx
│       │       ├── IndicatorsPanel.jsx
│       │       ├── MapPreview.jsx
│       │       ├── NavbarSmart.jsx
│       │       ├── ReportCTA.jsx
│       │       └── StatCard.jsx
│       ├── context/
│       │   └── UserContext.jsx
│       ├── data/
│       │   └── consejosData.js
│       │
│       ├── pages/              # Páginas principales de la aplicación
│       │   ├── Admin.jsx
│       │   ├── Alertas.jsx
│       │   ├── Configuracion.jsx
│       │   ├── Consejos.jsx
│       │   ├── Home.jsx
│       │   ├── Login.jsx
│       │   ├── Perfil.jsx
│       │   ├── PuntosHidratacion.jsx
│       │   ├── Register.jsx
│       │   └── ZonasFrescas.jsx
│       ├── router/
│       │   └── AppRouter.jsx
│       ├── services/           # Servicios para comunicación con API
│       │   ├── api.js
│       │   ├── authService.js
│       │   ├── climaService.js
│       │   ├── puntosService.js
│       │   ├── reportesService.js
│       │   └── zonasService.js
│       └── utils/
│           └── leafletConfig.js
│
└── docs/                       # Documentación adicional (vacío por ahora)
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior (Preferiblemente se recomienda usar la version de python con la cual se trabajo en el proyecto: `Python 3.11.9`)
- Node.js 16 o superior
- Git
- Cuenta en Supabase: https://supabase.com/

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Dakarplay/CalorSOS-App.git
cd CalorSOS-App
```

### 2. Configuración del Backend

#### Crear Entorno Virtual
```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/Mac:
source .venv/bin/activate
```

#### Instalar Dependencias
```bash
pip install -r requirements.txt
```

#### Configurar Variables de Entorno
Crear archivo `calorsos.env` en la raíz del proyecto:
```env
SUPABASE_URL=tu_supabase_url_aqui
SUPABASE_KEY=tu_supabase_key_aqui
JWT_SECRET=tu_clave_secreta_muy_segura_aqui
```

#### Ejecutar el Backend
- Nota: El backend debe ejecutarse desde la carpeta raiz del proyecto `/calorsos-app` y ejecutar el siguiente comando:
```bash
uvicorn backend.app.main:app --reload --port 8000
```

### 3. Configuración del Frontend

#### Instalar Dependencias
```bash
cd frontend
npm install
```

#### Ejecutar el Frontend
- Nota: Para ejecutar el frontend, debe ubicarse dentro de la carpeta `/frontend` y ejecutar, de esta forma:
```bash
cd frontend
npm run dev
```

El frontend estará disponible en `http://localhost:5173` y el backend en `http://localhost:8000`.

## Uso de la Aplicación

### Acceso a la Documentación de la API
Una vez ejecutado el backend, acceder a:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Autenticación
1. Registrar un nuevo usuario en `/usuarios/register`
2. Iniciar sesión en `/usuarios/login`
3. Copiar el token JWT recibido
4. Usar el token en el header `Authorization: Bearer <token>` para rutas protegidas

### Roles de Usuario
- **usuario**: Acceso básico a información y creación de reportes
- **admin**: Acceso completo a gestión del sistema

## API Endpoints Principales

### Autenticación
- `POST /usuarios/register` - Registro de usuarios
- `POST /usuarios/login` - Inicio de sesión
- `GET /usuarios/perfil` - Obtener perfil del usuario autenticado

### Gestión de Usuarios (Admin)
- `GET /usuarios/` - Listar todos los usuarios
- `PUT /usuarios/{id}` - Actualizar usuario
- `DELETE /usuarios/{id}` - Eliminar usuario

### Puntos de Hidratación
- `GET /puntos_hidratacion/` - Listar puntos activos
- `POST /puntos_hidratacion/` - Crear nuevo punto (requiere token)
- `PUT /puntos_hidratacion/{id}` - Actualizar punto (admin)
- `DELETE /puntos_hidratacion/{id}` - Eliminar punto (admin)

### Zonas Frescas
- `GET /zonas_frescas/` - Listar zonas activas
- `POST /zonas_frescas/` - Crear nueva zona (requiere token)
- `PUT /zonas_frescas/{id}` - Actualizar zona (admin)
- `DELETE /zonas_frescas/{id}` - Eliminar zona (admin)

### Reportes Ciudadanos
- `GET /reportes/` - Listar reportes (filtrado por usuario/estado)
- `POST /reportes/` - Crear nuevo reporte
- `PUT /reportes/{id}` - Actualizar reporte
- `DELETE /reportes/{id}` - Eliminar reporte

### Administración de Reportes
- `PUT /admin/validar_reporte/{id}` - Validar reporte y crear entidad correspondiente
- `PUT /admin/rechazar_reporte/{id}` - Rechazar y eliminar reporte

### Alertas de Calor
- `GET /alertas_calor/` - Listar alertas activas
- `POST /alertas_calor/` - Crear nueva alerta (admin)
- `DELETE /alertas_calor/{id}` - Eliminar alerta (admin)

### Notificaciones
- `GET /notificaciones/` - Listar notificaciones del usuario
- `POST /notificaciones/` - Crear notificación (admin)
- `PUT /notificaciones/{id}` - Actualizar estado (admin)
- `DELETE /notificaciones/{id}` - Eliminar notificación (admin)

### Datos Climáticos
- `GET /clima/` - Obtener clima actual
- `GET /clima/historico/{dias}` - Obtener datos históricos

## Funcionamiento del Sistema

### Flujo de Usuario Común
1. **Registro/Login**: El usuario se registra o inicia sesión.
2. **Visualización**: Accede al mapa principal con puntos de hidratación y zonas frescas.
3. **Reportes**: Puede crear reportes sobre necesidades no cubiertas.
4. **Alertas**: Recibe notificaciones sobre condiciones climáticas peligrosas.
5. **Consejos**: Consulta información preventiva sobre el calor.

### Flujo Administrativo
1. **Gestión de Contenido**: Los administradores mantienen actualizados los puntos y zonas.
2. **Validación de Reportes**: Revisan y procesan reportes ciudadanos, creando nuevas entidades si es necesario.
3. **Alertas**: Emiten alertas basadas en datos climáticos.
4. **Monitoreo**: Supervisan el uso del sistema y la actividad de usuarios.

### Integración Frontend-Backend
- El frontend consume la API REST del backend.
- La autenticación se maneja mediante JWT tokens.
- Los datos geográficos se visualizan usando Leaflet.
- La comunicación es asíncrona mediante Axios.

## Base de Datos

El sistema utiliza Supabase (PostgreSQL) con las siguientes tablas principales:
- `usuarios`: Información de usuarios y roles
- `puntos_hidratacion`: Ubicación y detalles de puntos de hidratación
- `zonas_frescas`: Información sobre zonas frescas
- `reportes`: Reportes ciudadanos pendientes de validación
- `alertas_calor`: Alertas climáticas activas
- `notificaciones`: Mensajes para usuarios

## Desarrollado por

**Dago David Palmera Navarro**
**Julian David Camargo Padilla**
- **Proyecto académico** - Ingeniería de Sistemas
- **Asignatura** - Ingenieria de Servicios de Internet (ISI)
- **Universidad:** Universidad de Cartagena - Cartagena de Indias - COLOMBIA
- **Semestre:** 5to Semestre
- **Periodo:** 2025-2

<!-- Fin README.md -->
