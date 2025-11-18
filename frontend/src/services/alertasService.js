// inicio alertasService.js

// frontend/src/services/alertasService.js

import api from "./api";

// Obtener alerta actual
export const obtenerAlertaActual = () => {
    return api.get("/alertas_calor/actual");
};

// Listar todas las alertas
export const listarAlertas = async () => {
    const response = await api.get("/alertas_calor/");
    return response.data.data || [];
};

// Crear alerta manual
export const crearAlerta = (data) => {
    return api.post("/alertas_calor/", data);
};

// Generar alerta automática desde clima (solo admin)
export const generarAlertaAutomatica = () => {
    return api.post("/alertas_calor/generar-desde-clima");
};

// Eliminar alerta por ID (solo admin)
export const eliminarAlerta = (id) => {
    return api.delete(`/alertas_calor/${id}`);
};

export default {
    obtenerAlertaActual,
    listarAlertas,
    crearAlerta,
    generarAlertaAutomatica
};

// fin alertasService.js