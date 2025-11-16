// src/services/reportesService.js
import API from "./api";

/**
 * Crear un nuevo reporte.
 * @param {Object} reporte - Datos del reporte: tipo, nombre, descripcion, latitud, longitud
 * @returns {Promise<Object>} - Respuesta del backend
 */
export const crearReporte = async (reporte) => {
    try {
        const formData = new FormData();
        formData.append("tipo", reporte.tipo);
        if (reporte.nombre) formData.append("nombre", reporte.nombre);
        if (reporte.descripcion) formData.append("descripcion", reporte.descripcion);
        if (reporte.latitud) formData.append("latitud", reporte.latitud);
        if (reporte.longitud) formData.append("longitud", reporte.longitud);

        if (reporte.tipo === "zona_fresca" && reporte.tipo_zona_fresca) {
            formData.append("tipo_zona_fresca", reporte.tipo_zona_fresca);
        }

        const response = await API.post("/reportes/", formData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        return response.data;
    } catch (error) {
        console.error("Error creando reporte:", error.response?.data || error.message);
        throw error;
    }
};

