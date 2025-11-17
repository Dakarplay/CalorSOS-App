// Inicio ReportCTA.jsx

// frontend/src/components/ui/ReportCTA.jsx

// Componente de llamada a acción para crear nuevos reportes

// Importaciones de React
import React from "react";

// Importación de estilos
import "../../assets/styles/ReportCTA.css";

// Componente funcional principal
export default function ReportCallToAction({ onClick }) {
    return (
        <div className="rca-wrap">
            <div className="rca-inner">
                <div className="rca-text">
                    ¿Deseas reportar un nuevo punto de hidratación o zona fresca? Envía un reporte comunitario.
                </div>
                <div className="rca-action">
                    <button className="rca-btn" onClick={onClick}>
                        Nuevo reporte
                    </button>
                </div>
            </div>
        </div>
    );
}

// Fin ReportCTA.jsx
