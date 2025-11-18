// Inicio notificacionesApiService.js

// frontend/src/services/notificacionesApiService.js

import api from "./api";

// Crear notificación individual
export const crearNotificacion = (data) => {
    return api.post("/notificaciones/", data);
};

// Crear notificación global
export const crearNotificacionGlobal = (mensaje) => {
    return api.post("/notificaciones/global", { mensaje });
};

// Listar notificaciones
export const listarNotificaciones = async (idUsuario = null) => {
    const params = idUsuario ? { id_usuario: idUsuario } : {};
    const response = await api.get("/notificaciones/", { params });
    return response.data.data || [];
};

// Obtener notificación por ID
export const obtenerNotificacion = (id) => {
    return api.get(`/notificaciones/${id}`);
};

// Actualizar estado de notificación
export const actualizarEstadoNotificacion = (id, estado) => {
    return api.put(`/notificaciones/${id}`, { estado });
};

// Eliminar notificación
export const eliminarNotificacion = (id) => {
    return api.delete(`/notificaciones/${id}`);
};

export default {
    crearNotificacion,
    crearNotificacionGlobal,
    listarNotificaciones,
    obtenerNotificacion,
    actualizarEstadoNotificacion,
    eliminarNotificacion
};

// Fin notificacionesApiService.js
