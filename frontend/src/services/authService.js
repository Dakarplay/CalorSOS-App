// src/services/authService.js
import { API_URL } from "./api.js";

export const loginUser = async (correo, password) => {
    const form = new FormData();
    form.append("correo", correo);
    form.append("password", password);

    const response = await fetch(`${API_URL}/usuarios/login`, {
        method: "POST",
        body: form
    });

    return response.json();
};
