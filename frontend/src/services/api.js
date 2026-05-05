// Inicio api.js

// frontend/src/services/api.js

// Importación de axios para peticiones HTTP
import axios from "axios";

// URL base de la API del backend
export const API_URL = import.meta.env.VITE_API_URL;

// Creación del cliente Axios con configuración base
const API = axios.create({
  baseURL: API_URL,
});

// Interceptor de solicitud para añadir automáticamente el token JWT
API.interceptors.request.use((config) => {
    // Obtener token del localStorage
    const token = localStorage.getItem("token");
    // Añadir token a los headers si existe
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
});

// Exportar cliente configurado
export default API;

// Fin api.js
