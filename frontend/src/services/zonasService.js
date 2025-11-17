// Inicio zonasService.js

// frontend/src/services/zonasService.js

// Importación del cliente API configurado
import API from "./api";

// Servicio para manejar operaciones con zonas frescas
const zonasService = {
    // Función para listar zonas frescas
    async listarZonas(estado = "activa") {
        try {
            // Si estado es null o vacío, obtener todas las zonas (para admin)
            const url = estado ? `/zonas_frescas?estado=${estado}` : "/zonas_frescas";
            const res = await API.get(url);
            return res.data.data;
        } catch (error) {
            console.error("Error al listar zonas frescas:", error);
            throw error;
        }
    },

    // Función para obtener zona específica por ID
    async obtenerZona(id) {
        try {
            const res = await API.get(`/zonas_frescas/${id}`);
            return res.data.data;
        } catch (error) {
            console.error("Error al obtener zona fresca:", error);
            throw error;
        }
    },

    // Función para crear nueva zona fresca
    async crearZona(data) {
        try {
            const res = await API.post("/zonas_frescas", data);
            return res.data.data;
        } catch (error) {
            console.error("Error al crear zona fresca:", error);
            throw error;
        }
    },

    // Función para actualizar zona fresca
    async actualizarZona(id, data) {
        try {
            const res = await API.put(`/zonas_frescas/${id}`, data);
            return res.data.data;
        } catch (error) {
            console.error("Error al actualizar zona fresca:", error);
            throw error;
        }
    },

    // Función para eliminar zona fresca
    async eliminarZona(id) {
        try {
            const res = await API.delete(`/zonas_frescas/${id}`);
            return res.data;
        } catch (error) {
            console.error("Error al eliminar zona fresca:", error);
            throw error;
        }
    },
};

// Exportar servicio
export default zonasService;

// Fin zonasService.js
