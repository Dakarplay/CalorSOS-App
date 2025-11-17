import React, { useEffect, useRef } from "react";
import {
    MapContainer,
    TileLayer,
    Marker,
    Popup,
    useMap,
} from "react-leaflet";

import L from "leaflet";
import "./MapView.css";

// Fix de íconos por defecto (marcador azul)
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
    iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
});

// --- FORZAR RESIZE EN MODAL ---
function ForceResize() {
    const map = useMap();
    useEffect(() => {
        setTimeout(() => map.invalidateSize(), 200);
    }, [map]);
    return null;
}

// --- CENTRAR EN SELECCIÓN ---
function CenterOnSelection({ seleccion }) {
    const map = useMap();

    useEffect(() => {
        if (seleccion) {
            map.setView([seleccion.latitud, seleccion.longitud], 16, {
                animate: true,
            });
        }
    }, [seleccion]);

    return null;
}

// --- NUEVO: RESET GENERAL DE VISTA ---
function ResetView({ trigger, zonasFrescas, puntosHidratacion }) {
    const map = useMap();

    useEffect(() => {
        if (trigger === 0) return;

        const coords = [];

        zonasFrescas?.forEach(z => coords.push([z.latitud, z.longitud]));
        puntosHidratacion?.forEach(p => coords.push([p.latitud, p.longitud]));

        if (coords.length === 0) return;

        const bounds = L.latLngBounds(coords);

        map.fitBounds(bounds, {
            padding: [50, 50],
            animate: true,
            maxZoom: 14
        });
    }, [trigger, zonasFrescas]);

    // Escuchar evento de reset
    useEffect(() => {
        const handleReset = () => {
            const coords = [];
            zonasFrescas?.forEach(z => coords.push([z.latitud, z.longitud]));
            puntosHidratacion?.forEach(p => coords.push([p.latitud, p.longitud]));

            if (coords.length === 0) return;

            const bounds = L.latLngBounds(coords);
            map.fitBounds(bounds, {
                padding: [50, 50],
                animate: true,
                maxZoom: 14
            });
        };

        window.addEventListener('resetMapView', handleReset);
        return () => window.removeEventListener('resetMapView', handleReset);
    }, [map, zonasFrescas, puntosHidratacion]);

    return null;
}

// ICONO VERDE PARA ZONAS FRESCAS
const greenDivIcon = new L.DivIcon({
    html: `<span class="zf-div-marker"></span>`,
    className: "custom-div-icon-wrapper",
    iconSize: [24, 24],
    iconAnchor: [12, 24],
    popupAnchor: [0, -20],
});

// ICONO AZUL PARA PUNTOS DE HIDRATACIÓN
const blueDivIcon = new L.DivIcon({
    html: `<span class="ph-div-marker"></span>`,
    className: "custom-div-icon-wrapper",
    iconSize: [24, 24],
    iconAnchor: [12, 24],
    popupAnchor: [0, -20],
});

// ICONO ROJO PARA REPORTES
const redDivIcon = new L.DivIcon({
    html: `<span class="report-div-marker"></span>`,
    className: "custom-div-icon-wrapper",
    iconSize: [24, 24],
    iconAnchor: [12, 24],
    popupAnchor: [0, -20],
});

export default function MapView({
    mini = false,
    onExpand,
    zonasFrescas = [],
    puntosHidratacion = [],
    zonaSeleccionada = null,
    puntoSeleccionado = null,
    onSelectMarker = () => {},
    resetView = false,   // 👈 NUEVO
    reportes = [], // Nueva prop para reportes
    selectedMarker = null, // Para controlar el zoom en marcador seleccionado
}) {

    const markerRefs = useRef({});

    // abrir popup automático
    useEffect(() => {
        if (zonaSeleccionada && markerRefs.current[zonaSeleccionada.id_zona]) {
            try {
                markerRefs.current[zonaSeleccionada.id_zona].openPopup();
            } catch {}
        }
        if (puntoSeleccionado && markerRefs.current[puntoSeleccionado.id_punto]) {
            try {
                markerRefs.current[puntoSeleccionado.id_punto].openPopup();
            } catch {}
        }
    }, [zonaSeleccionada, puntoSeleccionado]);

    return (
        <div className={mini ? "mv-container mini" : "mv-container full"}>

            <MapContainer
                center={[10.391, -75.479]}
                zoom={13}
                className="mv-map"
                maxBounds={[
                    [10.30, -75.60],
                    [10.50, -75.35]
                ]}
                maxBoundsViscosity={1.0}
                minZoom={12}
                maxZoom={18}
                dragging={true}
                scrollWheelZoom={true}
                doubleClickZoom={!mini}
                zoomControl={false}
                touchZoom={!mini}
                boxZoom={!mini}
                keyboard={!mini}
                attributionControl={false}
            >
                <ForceResize />

                {/* reset general cuando trigger cambia */}
                <ResetView
                    trigger={resetView}
                    zonasFrescas={zonasFrescas}
                    puntosHidratacion={puntosHidratacion}
                />

                {/* centrado por selección */}
                <CenterOnSelection seleccion={zonaSeleccionada || puntoSeleccionado || (reportes.length > 0 ? reportes[0] : null)} />

                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution="&copy; OpenStreetMap"
                />

                {/* Marcadores verdes (Zonas Frescas) */}
                {Array.isArray(zonasFrescas) && zonasFrescas.map((z) => (
                    <Marker
                        key={z.id_zona}
                        position={[z.latitud, z.longitud]}
                        icon={greenDivIcon}
                        ref={(ref) => (markerRefs.current[z.id_zona] = ref)}
                        eventHandlers={{ click: () => onSelectMarker(z) }}
                    >
                        <Popup>
                            <strong>{z.nombre}</strong><br />
                            {z.descripcion}
                        </Popup>
                    </Marker>
                ))}

                {/* Marcadores azules (Puntos de hidratación) */}
                {Array.isArray(puntosHidratacion) && puntosHidratacion.map((p) => (
                    <Marker
                        key={p.id_punto}
                        position={[p.latitud, p.longitud]}
                        icon={blueDivIcon}
                        ref={(ref) => (markerRefs.current[p.id_punto] = ref)}
                        eventHandlers={{ click: () => onSelectMarker(p) }}
                    >
                        <Popup>
                            <strong>{p.nombre}</strong><br />
                            {p.descripcion}
                        </Popup>

                    </Marker>
                ))}

                {/* Marcadores rojos (Reportes) */}
                {Array.isArray(reportes) && reportes.map((r) => (
                    <Marker
                        key={r.id_reporte}
                        position={[r.latitud, r.longitud]}
                        icon={redDivIcon}
                        ref={(ref) => (markerRefs.current[r.id_reporte] = ref)}
                    >
                        <Popup>
                            <strong>Reporte: {r.nombre || "Sin nombre"}</strong><br />
                            <strong>Tipo:</strong> {r.tipo}<br />
                            <strong>Estado:</strong> {r.estado}<br />
                            {r.descripcion && <><strong>Descripción:</strong> {r.descripcion}<br /></>}
                            {r.fecha_reporte && <><strong>Fecha:</strong> {new Date(r.fecha_reporte).toLocaleString()}</>}
                        </Popup>
                    </Marker>
                ))}

            </MapContainer>

            {/* botón ver completo si es mini */}
            {mini && (
                <button className="mv-expand-btn" onClick={onExpand}>
                    Ver mapa completo
                </button>
            )}

            {/* botón reset vista si no es mini */}
            {!mini && (
                <button className="mv-reset-btn" onClick={() => {
                    // Trigger reset view
                    const event = new CustomEvent('resetMapView');
                    window.dispatchEvent(event);
                }}>
                    Restablecer vista
                </button>
            )}
        </div>
    );
}
