// Inicio ReportForm.jsx

// frontend/src/components/report/ReportForm.jsx

// Componente de formulario para crear reportes comunitarios

// Importaciones de React y hooks
import React, { useState } from "react";

// Importación del componente MapView
import MapView from "../maps/MapView.jsx";

// Importación del servicio de reportes
import { enviarReporte } from "../../services/reportesService.js";

// Importación de estilos
import "./ReportForm.css";

// Componente funcional principal
export default function ReportForm({ onClose, tipoPreseleccion = null }) {
    // Estados del formulario
    const [tipo, setTipo] = useState(tipoPreseleccion || "");
    const [nombre, setNombre] = useState("");
    const [descripcion, setDescripcion] = useState("");
    const [foto, setFoto] = useState(null);
    const [ubicacion, setUbicacion] = useState(null);

    // Estados de UI
    const [mensaje, setMensaje] = useState(null);
    const [enviando, setEnviando] = useState(false);

    // Manejar selección de ubicación en el mapa
    const handleMapClick = (coords) => {
        setUbicacion(coords);
    };

    // Manejar envío del formulario
    const handleSubmit = async (e) => {
        e.preventDefault();

        // Validación de campos obligatorios
        if (!tipo || !nombre || !descripcion || !ubicacion) {
            setMensaje("Completa todos los campos obligatorios.");
            return;
        }

        setEnviando(true);
        setMensaje(null);

        try {
            // Preparar datos del formulario
            const formData = new FormData();
            formData.append("tipo", tipo);
            formData.append("nombre", nombre);
            formData.append("descripcion", descripcion);
            formData.append("latitud", ubicacion.lat);
            formData.append("longitud", ubicacion.lng);
            if (foto) formData.append("foto", foto);

            // Enviar reporte
            const resp = await enviarReporte(formData);

            if (!resp.ok) throw new Error("Error enviando el reporte");

            setMensaje("Reporte enviado correctamente");
            setTimeout(onClose, 1200);

        } catch (err) {
            console.error(err);
            setMensaje("Ocurrió un error al enviar el reporte.");
        }

        setEnviando(false);
    };

    return (
        <div className="report-form">
            <h2>Nuevo reporte comunitario</h2>

            <form onSubmit={handleSubmit}>
                {/* Campo de tipo de reporte */}
                {!tipoPreseleccion && (
                    <label>
                        Tipo de reporte:
                        <select value={tipo} onChange={(e) => setTipo(e.target.value)} required>
                            <option value="">Seleccione</option>
                            <option value="zona_fresca">Zona fresca</option>
                            <option value="punto_hidratacion">Punto de hidratación</option>
                        </select>
                    </label>
                )}

                {/* Campo de nombre */}
                <label>
                    Nombre:
                    <input
                        type="text"
                        value={nombre}
                        onChange={(e) => setNombre(e.target.value)}
                        required
                    />
                </label>

                {/* Campo de descripción */}
                <label>
                    Descripción:
                    <textarea
                        value={descripcion}
                        onChange={(e) => setDescripcion(e.target.value)}
                        required
                    />
                </label>

                {/* Campo de foto opcional */}
                <label>
                    Foto (opcional):
                    <input type="file" accept="image/*" onChange={(e) => setFoto(e.target.files[0])} />
                </label>

                {/* Selector de ubicación con mapa */}
                <div className="map-selector">
                    <p>Selecciona la ubicación en el mapa:</p>
                    <MapView
                        mini={true}
                        onSelectMarker={(coords) => handleMapClick(coords)}
                        puntosHidratacion={[]}
                        zonasFrescas={[]}
                    />
                </div>

                {/* Vista previa de coordenadas */}
                {ubicacion && (
                    <div className="coords-preview">
                        Ubicación: {ubicacion.lat.toFixed(5)}, {ubicacion.lng.toFixed(5)}
                    </div>
                )}

                {/* Mensaje de estado */}
                {mensaje && <p className="msg">{mensaje}</p>}

                {/* Botón de envío */}
                <button type="submit" disabled={enviando}>
                    {enviando ? "Enviando..." : "Enviar reporte"}
                </button>
            </form>
        </div>
    );
}

// Fin ReportForm.jsx
