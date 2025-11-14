// src/context/UserContext.jsx
import { createContext, useState, useEffect } from "react";
import API from "../services/api.js";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem("token") || null);
    const [loading, setLoading] = useState(true);

    // Verificar token al iniciar la app
    useEffect(() => {
        const verify = async () => {
            if (!token) { setLoading(false); return; }
            try {
            const me = await API.get("/usuarios/perfil");
            setUser(me.data.usuario_actual);
            } catch {
            localStorage.removeItem("token");
            setToken(null);
            }
            setLoading(false);
        };
    verify();
    }, [token]);


    // LOGIN
    const login = async (correo, password) => {
        const form = new FormData();
        form.append("correo", correo);
        form.append("password", password);

        const res = await fetch("http://localhost:8000/usuarios/login", {
            method: "POST",
            body: form,
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.detail || "Credenciales incorrectas");
        }

        const data = await res.json();
        const token = data.access_token;

        // Guardar token
        localStorage.setItem("token", token);
        setToken(token);

        // Obtener perfil del usuario (ruta segura)
        const me = await API.get("/usuarios/perfil");
        setUser(me.data.data);

        return me.data.data; // <-- retornamos el usuario
    };


    const logout = () => {
        localStorage.removeItem("token");
        setUser(null);
        setToken(null);
    };

    return (
        <UserContext.Provider value={{ user, setUser, token, loading, login, logout }}>
        {children}
        </UserContext.Provider>
    );
};
