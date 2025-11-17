// Inicio ReportModal.jsx

// frontend/src/components/report/ReportModal.jsx

// Componente modal para mostrar formularios de reportes

// Importaciones de React
import React from "react";

// Importación de estilos
import "./ReportModal.css";

// Componente funcional principal
export default function ReportModal({ open, onClose, children }) {
    // No renderizar si el modal no está abierto
    if (!open) return null;

    return (
        <div className="rm-backdrop">
            <div className="rm-window">
                {/* Botón para cerrar el modal */}
                <button className="rm-close-btn" onClick={onClose}>
                    ✕
                </button>

                {/* Contenido del modal */}
                <div className="rm-content">
                    {children}
                </div>
            </div>
        </div>
    );
}

// Fin ReportModal.jsx
