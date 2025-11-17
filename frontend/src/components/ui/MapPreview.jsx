// Inicio MapPreview.jsx

// frontend/src/components/ui/MapPreview.jsx

// Componente de vista previa del mapa con opción para ver mapa completo

// Importación de estilos
import "../../assets/styles/MapPreview.css";

// Importación del componente MapView
import MapView from "../maps/MapView.jsx";

// Componente funcional principal
export default function MapPreview() {
    return (
        <div className="mt-tile">
            <div className="mt-header">
                <div className="mt-title">Mapa — vista previa</div>
                <div className="mt-actions">
                    <button className="mt-btn">Ver mapa completo</button>
                </div>
            </div>

            <div className="mt-body">
                <div style={{ height: "200px", width: "100%", borderRadius: "12px", overflow: "hidden" }}>
                    <MapView mini />
                </div>
            </div>

            <div className="mt-footer">
                <span className="mt-note">Haz clic en "Ver mapa completo" para ampliar y ver todos los puntos.</span>
            </div>
        </div>
    );
}

// Fin MapPreview.jsx
