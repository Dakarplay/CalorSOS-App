// Inicio main.jsx

// frontend/src/main.jsx

// Punto de entrada principal de la aplicación React

// Importaciones de React y ReactDOM
import React from "react";
import ReactDOM from "react-dom/client";

// ADD: register SW for PWA
import { registerSW } from "virtual:pwa-register";
registerSW();

import App from "./app.jsx";
import { UserProvider } from "./context/UserContext.jsx";

// Importación del enrutador de React
import { BrowserRouter } from "react-router-dom";

// Importaciones de estilos globales y configuraciones
import "./assets/styles/global.css";
import "./utils/leafletConfig.js";

// Renderizado de la aplicación en el DOM
ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <BrowserRouter>
            <UserProvider>
                <App />
            </UserProvider>
        </BrowserRouter>
    </React.StrictMode>
);

// Fin main.jsx
