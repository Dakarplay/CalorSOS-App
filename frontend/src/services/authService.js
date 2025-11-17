// Inicio authService.js

// frontend/src/services/authService.js

// Importación de la URL base de la API
import { API_URL } from "./api.js";

// Función para autenticar usuario
export const loginUser = async (correo, password) => {
    // Crear FormData para enviar credenciales
    const form = new FormData();
    form.append("correo", correo);
    form.append("password", password);

    // Realizar petición POST al endpoint de login
    const response = await fetch(`${API_URL}/usuarios/login`, {
        method: "POST",
        body: form
    });

    // Retornar respuesta en formato JSON
    return response.json();
};

// Fin authService.js
