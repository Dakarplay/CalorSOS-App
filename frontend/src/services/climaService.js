// Inicio climaService.js

// frontend/src/services/climaService.js

// Importación del cliente API configurado
import API from "./api.js";

// Función para obtener datos climáticos actuales
export const getClima = async () => {
    try {
        const res = await API.get("/clima/");
        return res.data;
    } catch (error) {
        console.error("Error obteniendo clima:", error);
        return null;
    }
};

// Función para obtener histórico de sensación térmica
export const getClimaHistorico = async (dias = 1) => {
    try {
        const res = await API.get("/clima/historico", {
            params: { dias },
        });
        return res.data;
    } catch (error) {
        console.error("Error obteniendo histórico del clima:", error);
        return [];
    }
};

// Función para obtener histórico de temperatura y humedad
export const getClimaHistoricoTempHumedad = async (dias = 1) => {
    try {
        const res = await API.get("/clima/historico-temp-humedad", {
            params: { dias },
        });
        return res.data;
    } catch (error) {
        console.error("Error obteniendo histórico temp/humedad:", error);
        return [];
    }
};

// Fin climaService.js
