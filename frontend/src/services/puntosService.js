// Inicio puntosService.js

// frontend/src/services/puntosService.js

// Importación del cliente API configurado
import API from "./api.js";

// Función para obtener puntos de hidratación
const obtenerPuntosHidratacion = async (estado = "activa") => {
    const url = estado !== "activa" ? "/puntos_hidratacion/" : `/puntos_hidratacion/?estado=${estado}`;
    const res = await API.get(url);
    return res.data.data;
};

// Función para obtener punto específico por ID
const obtenerPuntoPorId = async (id) => {
    const res = await API.get(`/puntos_hidratacion/${id}`);
    return res.data.data;
};

// Función para actualizar punto (solo admin)
const actualizarPunto = async (id, data) => {
    try {
        const res = await API.put(`/puntos_hidratacion/${id}`, data);
        return res.data.data;
    } catch (error) {
        console.error("Error al actualizar punto de hidratación:", error);
        throw error;
    }
};

// Función para eliminar punto (solo admin)
const eliminarPunto = async (id) => {
    try {
        const res = await API.delete(`/puntos_hidratacion/${id}`);
        return res.data;
    } catch (error) {
        console.error("Error al eliminar punto de hidratación:", error);
        throw error;
    }
};

// Exportar objeto con todas las funciones
export default {
    obtenerPuntosHidratacion,
    obtenerPuntoPorId,
    actualizarPunto,
    eliminarPunto,
};

// Fin puntosService.js
