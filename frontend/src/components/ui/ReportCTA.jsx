// Inicio ReportCTA.jsx

// frontend/src/components/ui/ReportCTA.jsx

// Componente de llamada a acción para crear nuevos reportes

// Importaciones de React
import React from "react";

// Importación de estilos
import "../../assets/styles/ReportCTA.css";

// Componente funcional principal
export default function ReportCallToAction() {
    return (
        <div className="rca-wrap">
            <div className="rca-inner">
                <div className="rca-text">
                    ¿Deseas reportar un nuevo punto de hidratación o zona fresca? Envía un reporte comunitario.
                </div>
                <div className="rca-action">
                    <a href="/zonas-frescas" className="rca-btn rca-btn-zona">
                        Reportar Zona Fresca
                    </a>
                    <a href="/puntos-hidratacion" className="rca-btn rca-btn-punto">
                        Reportar Punto de Hidratación
                    </a>
                </div>
            </div>
        </div>
    );
}

// Fin ReportCTA.jsx
