import { API_URL } from "./api.js";

export const registerUser = async (data) => {
    const form = new FormData();
    form.append("nombre", data.nombre);
    form.append("correo", data.correo);
    form.append("password", data.password);
    form.append("telefono", "");
    form.append("rol", "usuario");

    const response = await fetch(`${API_URL}/usuarios/register`, {
        method: "POST",
        body: form,
    });

    return response;
};
