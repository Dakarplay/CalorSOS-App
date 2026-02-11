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
- **Registro y autenticación de usuarios** con validación de datos.
- **Visualización de puntos de hidratación** en mapa interactivo con Leaflet.
- **Consulta de zonas frescas disponibles** con filtros por tipo y ubicación.
- **Creación de reportes ciudadanos** sobre necesidades de hidratación o zonas frescas.
- **Recepción de notificaciones** sobre alertas climáticas y actualizaciones.
- **Acceso a consejos y recomendaciones** de prevención del calor.
- **Perfil personal** para gestionar información y configuración.
- **Sistema de configuración** para preferencias de notificaciones.

### Para Administradores
- **Validación y gestión de reportes ciudadanos** con conversión automática a entidades.
- **Creación y administración completa de puntos de hidratación**.
- **Gestión integral de zonas frescas** con diferentes tipos.
- **Emisión de alertas climáticas** manuales y automáticas.
- **Envío de notificaciones globales** a todos los usuarios.
- **Administración completa de usuarios** y roles del sistema.
- **Monitoreo del sistema** y actividad de usuarios.
- **Panel de administración** con estadísticas y métricas.

### Funcionalidades Generales
- **Datos climáticos en tiempo real** desde APIs externas (Open-Meteo).
- **Mapa interactivo con Leaflet** para visualización geográfica completa.
- **Sistema de autenticación JWT** con roles diferenciados.
- **Interfaz completamente responsiva** optimizada para móvil y desktop.
- **Integración completa con base de datos Supabase**.
- **Sistema de notificaciones push** para alertas importantes.
- **Gráficos y visualizaciones** de datos climáticos históricos.
- **Modal de mapas a pantalla completa** para mejor navegación.

## Tecnologías Utilizadas

### Backend
- **FastAPI**: Framework web moderno y rápido para APIs REST.
- **Supabase**: Base de datos PostgreSQL como servicio con autenticación integrada.
- **Python 3.11.9**: Lenguaje de programación principal.
- **JWT**: Autenticación basada en tokens con roles.
- **Bcrypt**: Hashing seguro de contraseñas.
- **Open-Meteo API**: Fuente externa de datos climáticos.
- **Uvicorn**: Servidor ASGI para despliegue.

### Frontend
- **React 18**: Biblioteca para interfaces de usuario con hooks modernos.
- **Vite**: Herramienta de construcción rápida para desarrollo moderno.
- **Leaflet**: Biblioteca para mapas interactivos con marcadores personalizados.
- **Axios**: Cliente HTTP para comunicación asíncrona con la API.
- **CSS Modules**: Estilos modulares y organizados por componente.
- **React Router**: Navegación SPA con rutas protegidas.
- **Context API**: Gestión global del estado de autenticación.

### Infraestructura
- **Git**: Control de versiones con repositorio en GitHub.
- **VS Code**: Entorno de desarrollo integrado con extensiones.
- **Postman/Swagger**: Pruebas y documentación interactiva de API.
- **Responsive Design**: Optimización completa para dispositivos móviles.

## Estructura Completa del Proyecto

```
CalorSOS-App/
│
├── .gitignore                          # Configuración de archivos ignorados en Git
├── calorsos.env                        # Variables de entorno (Supabase URL, JWT Secret)
├── README.md                           # Documentación principal del proyecto
├── requirements.txt                    # Dependencias Python del backend
│
├── backend/                            # 🏗️ Lógica del servidor y API REST
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                     # 🚀 Punto de entrada principal de FastAPI
│   │   ├── routers/                    # 🔗 Definición de endpoints de la API
│   │   │   ├── __init__.py
│   │   │   ├── admin.py                # 👑 Endpoints de administración
│   │   │   ├── alertas_calor.py        # ⚠️ Gestión de alertas climáticas
│   │   │   ├── clima.py                # 🌤️ Datos climáticos y pronósticos
│   │   │   ├── notificaciones.py       # 📢 Sistema de notificaciones
│   │   │   ├── puntos_hidratacion.py   # 💧 Puntos de hidratación
│   │   │   ├── reportes.py             # 📝 Reportes ciudadanos
│   │   │   ├── usuarios.py             # 👤 Gestión de usuarios y autenticación
│   │   │   └── zonas_frescas.py        # 🌳 Zonas frescas
│   │   └── security/                   # 🔐 Módulos de seguridad y autenticación
│   │       ├── __init__.py
│   │       ├── hashing.py              # 🔒 Hashing de contraseñas con bcrypt
│   │       └── jwt_handler.py          # 🎫 Manejo de tokens JWT
│   ├── database/
│   │   ├── __init__.py
│   │   └── supabase_config.py          # 🗄️ Configuración de conexión a Supabase
│   └── models/                         # 📊 Modelos de datos y lógica de negocio
│       ├── __init__.py
│       ├── admin_mdls.py               # 👑 Lógica de administración
│       ├── alertas_calor_mdls.py       # ⚠️ Modelo de alertas climáticas
│       ├── clima_mdls.py               # 🌤️ Modelo de datos climáticos
│       ├── notificaciones_mdls.py      # 📢 Modelo de notificaciones
│       ├── punto_hidratacion_mdls.py   # 💧 Modelo de puntos de hidratación
│       ├── reportes_mdls.py            # 📝 Modelo de reportes ciudadanos
│       ├── usuarios_mdls.py            # 👤 Modelo de usuarios
│       └── zonas_frescas_mdls.py       # 🌳 Modelo de zonas frescas
│
├── frontend/                           # 🎨 Interfaz de usuario React
│   ├── index.html                      # 📄 Punto de entrada HTML
│   ├── node_modules/                   # 📦 Dependencias de Node.js
│   ├── package.json                    # ⚙️ Configuración de dependencias
│   ├── package-lock.json               # 🔒 Lock de versiones
│   ├── vite.config.js                  # ⚡ Configuración de Vite
│   └── src/
│       ├── app.jsx                     # 🏠 Componente raíz de la aplicación
│       ├── main.jsx                    # 🚀 Punto de entrada de React
│       ├── assets/
│       │   ├── images/
│       │   │   └── logo.svg            # 🖼️ Logo de la aplicación
│       │   └── styles/                 # 🎨 Estilos CSS organizados
│       │       ├── Admin.css           # 👑 Estilos del panel admin
│       │       ├── Alertas.css         # ⚠️ Estilos de alertas
│       │       ├── Auth.css            # 🔐 Estilos de autenticación
│       │       ├── ClimateChart.css    # 📊 Estilos de gráficos climáticos
│       │       ├── Configuracion.css   # ⚙️ Estilos de configuración
│       │       ├── Consejos.css        # 💡 Estilos de consejos
│       │       ├── global.css          # 🌐 Estilos globales
│       │       ├── Home.css            # 🏠 Estilos de la página principal
│       │       ├── IndicatorsPanel.css # 📈 Estilos del panel de indicadores
│       │       ├── NavbarSmart.css     # 🧭 Estilos de la navegación
│       │       ├── Perfil.css          # 👤 Estilos del perfil
│       │       ├── PuntosHidratacion.css # 💧 Estilos de puntos
│       │       ├── ReportCTA.css       # 📝 Estilos de CTA de reportes
│       │       ├── StatCard.css        # 📊 Estilos de tarjetas estadísticas
│       │       └── ZonasFrescas.css    # 🌳 Estilos de zonas frescas
│       ├── components/                 # 🧩 Componentes reutilizables
│       │   ├── common/
│       │   │   └── LoaderPremium.jsx   # ⏳ Loader animado premium
│       │   ├── maps/
│       │   │   ├── MapFullscreenModal.css
│       │   │   ├── MapFullscreenModal.jsx # 🗺️ Modal de mapa a pantalla completa
│       │   │   ├── MapView.css
│       │   │   └── MapView.jsx         # 🗺️ Vista de mapa interactivo
│       │   ├── report/
│       │   │   ├── ReportForm.jsx      # 📝 Formulario de reportes
│       │   │   ├── ReportModal.css
│       │   │   └── ReportModal.jsx     # 📝 Modal de creación de reportes
│       │   └── ui/                     # 🎛️ Componentes de interfaz
│       │       ├── ClimateChart.jsx    # 📊 Gráfico de datos climáticos
│       │       ├── EditPuntoModal.jsx  # ✏️ Modal de edición de puntos
│       │       ├── EditZonaModal.jsx   # ✏️ Modal de edición de zonas
│       │       ├── IndicatorsPanel.jsx # 📈 Panel de indicadores climáticos
│       │       ├── MapPreview.jsx      # 🗺️ Vista previa de mapa
│       │       ├── NavbarSmart.jsx     # 🧭 Barra de navegación inteligente
│       │       ├── NotificationSettings.css
│       │       ├── NotificationSettings.jsx # 🔔 Configuración de notificaciones
│       │       ├── ReportCTA.jsx       # 📝 Call-to-action de reportes
│       │       └── StatCard.jsx        # 📊 Tarjeta de estadísticas
│       ├── context/
│       │   └── UserContext.jsx         # 🔄 Contexto global de usuario
│       ├── data/
│       │   └── consejosData.js         # 💡 Datos de consejos preventivos
│       │
│       ├── pages/                      # 📄 Páginas principales
│       │   ├── Admin.jsx               # 👑 Panel de administración
│       │   ├── Alertas.jsx             # ⚠️ Página de alertas climáticas
│       │   ├── Configuracion.jsx       # ⚙️ Página de configuración
│       │   ├── Consejos.jsx            # 💡 Página de consejos
│       │   ├── Home.jsx                # 🏠 Página principal
│       │   ├── Login.jsx               # 🔐 Página de inicio de sesión
│       │   ├── Perfil.jsx              # 👤 Página de perfil de usuario
│       │   ├── PuntosHidratacion.jsx   # 💧 Página de puntos de hidratación
│       │   ├── Register.jsx            # 📝 Página de registro
│       │   └── ZonasFrescas.jsx        # 🌳 Página de zonas frescas
│       ├── router/
│       │   └── AppRouter.jsx           # 🛣️ Configuración de rutas
│       └── services/                   # 🔗 Servicios de API
│           ├── alertasService.js       # ⚠️ Servicio de alertas
│           ├── api.js                  # 🌐 Configuración base de API
│           ├── authService.js          # 🔐 Servicio de autenticación
│           ├── climaService.js         # 🌤️ Servicio de datos climáticos
│           ├── notificacionesApiService.js
│           ├── notificacionesGlobalesService.js
│           ├── notificacionesService.js # 📢 Servicios de notificaciones
│           ├── puntosService.js        # 💧 Servicio de puntos de hidratación
│           ├── reportesService.js      # 📝 Servicio de reportes
│           ├── usuariosService.js      # 👤 Servicio de usuarios
│           └── zonasService.js         # 🌳 Servicio de zonas frescas
│
└── docs/                               # 📚 Documentación adicional (vacío por ahora)
```

## Instalación y Configuración

### Prerrequisitos
- **Python 3.8 o superior** (Recomendado: `Python 3.11.9`)
- **Node.js 16 o superior**
- **Git**
- **Cuenta en Supabase**: https://supabase.com/

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
- **Nota**: El backend debe ejecutarse desde la carpeta raíz del proyecto `/calorsos-app`
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
- **Nota**: Para ejecutar el frontend, debe ubicarse dentro de la carpeta `/frontend`
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

## API Endpoints Detallados

### 🔐 Autenticación de Usuarios

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `POST` | `/usuarios/register` | Registro de nuevos usuarios | ❌ Público | Ninguno |
| `POST` | `/usuarios/login` | Inicio de sesión y obtención de token JWT | ❌ Público | Ninguno |
| `GET` | `/usuarios/perfil` | Obtener perfil del usuario autenticado | ✅ Token | usuario/admin |
| `GET` | `/usuarios/` | Listar todos los usuarios | ✅ Token | admin |
| `GET` | `/usuarios/{id_usuario}` | Obtener usuario específico por ID | ✅ Token | usuario*/admin |
| `PUT` | `/usuarios/{id_usuario}` | Actualizar información de usuario | ✅ Token | usuario*/admin |
| `DELETE` | `/usuarios/{id_usuario}` | Eliminar usuario del sistema | ✅ Token | admin |
| `PUT` | `/usuarios/{id_usuario}/cambiar-password` | Cambiar contraseña del usuario | ✅ Token | usuario*/admin |

**Notas**: *usuario solo puede modificar su propio perfil

### 💧 Gestión de Puntos de Hidratación

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `GET` | `/puntos_hidratacion/` | Listar puntos activos (con filtro opcional por estado) | ❌ Público | Ninguno |
| `GET` | `/puntos_hidratacion/{id_punto}` | Obtener detalles de un punto específico | ❌ Público | Ninguno |
| `POST` | `/puntos_hidratacion/` | Crear nuevo punto de hidratación | ✅ Token | usuario/admin |
| `PUT` | `/puntos_hidratacion/{id_punto}` | Actualizar información de punto | ✅ Token | admin |
| `DELETE` | `/puntos_hidratacion/{id_punto}` | Eliminar punto del sistema | ✅ Token | admin |

### 🌳 Gestión de Zonas Frescas

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `GET` | `/zonas_frescas/` | Listar zonas frescas activas (con filtro opcional por estado) | ❌ Público | Ninguno |
| `GET` | `/zonas_frescas/{id_zona}` | Obtener detalles de una zona específica | ❌ Público | Ninguno |
| `POST` | `/zonas_frescas/` | Crear nueva zona fresca | ✅ Token | usuario/admin |
| `PUT` | `/zonas_frescas/{id_zona}` | Actualizar información de zona | ✅ Token | admin |
| `DELETE` | `/zonas_frescas/{id_zona}` | Eliminar zona del sistema | ✅ Token | admin |

### 📝 Sistema de Reportes Ciudadanos

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `GET` | `/reportes/` | Listar reportes (con filtros por usuario, tipo, estado) | ✅ Token | admin |
| `GET` | `/reportes/{id_reporte}` | Obtener detalles de un reporte específico | ✅ Token | usuario/admin |
| `POST` | `/reportes/` | Crear nuevo reporte ciudadano | ✅ Token | usuario/admin |
| `PUT` | `/reportes/{id_reporte}` | Actualizar información de reporte | ✅ Token | admin |
| `DELETE` | `/reportes/{id_reporte}` | Eliminar reporte del sistema | ✅ Token | admin |

### 👑 Panel de Administración

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `PUT` | `/admin/validar_reporte/{id_reporte}` | Validar reporte y crear entidad correspondiente | ✅ Token | admin |
| `PUT` | `/admin/rechazar_reporte/{id_reporte}` | Rechazar y eliminar reporte | ✅ Token | admin |

### ⚠️ Sistema de Alertas de Calor

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `GET` | `/alertas_calor/actual` | Obtener alerta climática actual activa | ❌ Público | Ninguno |
| `GET` | `/alertas_calor/` | Listar todas las alertas históricas | ❌ Público | Ninguno |
| `GET` | `/alertas_calor/{id_alerta}` | Obtener detalles de alerta específica | ❌ Público | Ninguno |
| `POST` | `/alertas_calor/` | Crear nueva alerta manual | ✅ Token | admin |
| `POST` | `/alertas_calor/generar-desde-clima` | Generar alerta automática desde datos climáticos | ✅ Token | admin |
| `DELETE` | `/alertas_calor/{id_alerta}` | Eliminar alerta del sistema | ✅ Token | admin |

### 📢 Sistema de Notificaciones

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `GET` | `/notificaciones/` | Listar notificaciones (usuario ve las suyas, admin ve todas) | ✅ Token | usuario/admin |
| `GET` | `/notificaciones/{id_notificacion}` | Obtener notificación específica | ✅ Token | usuario*/admin |
| `POST` | `/notificaciones/` | Crear notificación individual | ✅ Token | admin |
| `POST` | `/notificaciones/global` | Enviar notificación a todos los usuarios | ✅ Token | admin |
| `PUT` | `/notificaciones/{id_notificacion}` | Actualizar estado de notificación | ✅ Token | admin |
| `DELETE` | `/notificaciones/{id_notificacion}` | Eliminar notificación | ✅ Token | admin |

**Notas**: *usuario solo puede ver sus propias notificaciones

### 🌤️ Datos Climáticos

| Método | Endpoint | Descripción | Autenticación | Rol Requerido |
|--------|----------|-------------|---------------|---------------|
| `GET` | `/clima/` | Obtener datos climáticos actuales | ❌ Público | Ninguno |
| `GET` | `/clima/historico` | Obtener histórico de sensación térmica (1-7 días) | ❌ Público | Ninguno |
| `GET` | `/clima/historico-temp-humedad` | Obtener histórico de temperatura y humedad (1-7 días) | ❌ Público | Ninguno |

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

El sistema utiliza **Supabase (PostgreSQL)** con las siguientes tablas principales:

### Tablas Principales
- **`usuarios`**: Información de usuarios y roles
- **`puntos_hidratacion`**: Ubicación y detalles de puntos de hidratación
- **`zonas_frescas`**: Información sobre zonas frescas
- **`reportes`**: Reportes ciudadanos pendientes de validación
- **`alertas_calor`**: Alertas climáticas activas
- **`notificaciones`**: Mensajes para usuarios

### Relaciones
- Un usuario puede crear múltiples reportes
- Los administradores validan reportes y crean puntos/zonas
- Las alertas generan notificaciones automáticas
- Los puntos y zonas tienen coordenadas geográficas

## Desarrollado por

**Dago David Palmera Navarro**   

**Proyecto académico** - Ingeniería de Servicios de Internet (ISI)  
**Universidad:** Universidad de Cartagena - Cartagena de Indias - COLOMBIA  
**Semestre:** 5to Semestre  
**Periodo:** 2025-2  

---

## 📊 Estadísticas del Proyecto

- **Líneas de código**: ~15,000+ líneas
- **Endpoints API**: 25+ endpoints documentados
- **Componentes React**: 20+ componentes reutilizables
- **Páginas**: 10 páginas principales
- **Estilos CSS**: 15+ archivos de estilos modulares
- **Modelos de datos**: 8 modelos principales
- **Servicios**: 11 servicios de API

<!-- Fin README.md -->
