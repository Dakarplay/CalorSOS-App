import { API_URL } from "./api.js";

export const getClima = async () => {
    const res = await fetch(`${API_URL}/clima/`);
    if (!res.ok) throw new Error("Error obteniendo clima");
    const data = await res.json();
    return data.data;
};
