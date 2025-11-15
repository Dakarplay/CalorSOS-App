// src/components/maps/MapView.jsx
import React, { useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import L from "leaflet";

import "./MapView.css";

// Fix de íconos para Leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
    iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
    });

    // Forzar resize cuando se monta el modal
    function ForceResize() {
    const map = useMap();
    useEffect(() => {
        setTimeout(() => map.invalidateSize(), 200);
    }, [map]);
    return null;
    }

    export default function MapView({ mini = false, onExpand }) {
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
            maxBoundsViscosity={1.0}  // entre 0 y 1, rebote fuerte
            minZoom={12}
            maxZoom={18}
            // restricciones de interacción
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

            <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="&copy; OpenStreetMap"
            />

            <Marker position={[10.391, -75.479]}>
            <Popup>Centro de Cartagena</Popup>
            </Marker>
        </MapContainer>

        {mini && (
            <button className="mv-expand-btn" onClick={onExpand}>
            Ver mapa completo
            </button>
        )}
        </div>
    );
}
