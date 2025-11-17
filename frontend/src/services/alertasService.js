// inicio alertasService.js

// frontend/src/services/alertasService.js

import api from "./api";

// Obtener alerta actual
export const obtenerAlertaActual = () => {
    return api.get("/alertas_calor/actual");
};

// Listar todas las alertas
export const listarAlertas = () => {
    return api.get("/alertas_calor/");
};

// Crear alerta manual
export const crearAlerta = (data) => {
    return api.post("/alertas_calor/", data);
};

// Generar alerta automática desde clima (solo admin)
export const generarAlertaAutomatica = () => {
    return api.post("/alertas_calor/generar-desde-clima");
};

export default {
    obtenerAlertaActual,
    listarAlertas,
    crearAlerta,
    generarAlertaAutomatica
};

// fin alertasService.js