// src/pages/Home.jsx
import React, { useState, useEffect } from "react";

// UI components
import IndicatorsPanel from "../components/ui/IndicatorsPanel.jsx";
import Navbar from "../components/ui/NavbarSmart.jsx";
import ReportCallToAction from "../components/ui/ReportCTA.jsx";
import StatCard from "../components/ui/StatCard.jsx";
import ClimateChart from "../components/ui/ClimateChart.jsx";

// Map components
import MapView from "../components/maps/MapView.jsx";
import MapFullscreenModal from "../components/maps/MapFullscreenModal.jsx";

// Services
import { getClima } from "../services/climaService.js";

// Styles
import "../assets/styles/Home.css";

export default function Home() {

    const [openMap, setOpenMap] = useState(false);
    const [weather, setWeather] = useState(null);
    const [loadingWeather, setLoadingWeather] = useState(true);
    const [lastUpdate, setLastUpdate] = useState("—");

    useEffect(() => {
        const fetchWeather = async () => {
            try {
                const data = await getClima();
                setWeather(data);

                // Timestamp
                const hora = new Date().toLocaleTimeString("es-CO", {
                    hour: "2-digit",
                    minute: "2-digit",
                });

                setLastUpdate(hora);

            } catch (error) {
                console.error("Error cargando clima:", error);
            } finally {
                setLoadingWeather(false);
            }
        };

        fetchWeather();
    }, []);

    const stats = weather
        ? [
            {
                id: "heat-level",
                title: "Nivel de Calor",
                value: weather.heat_level,
                unit: "/100",
                updated: lastUpdate
            },
            {
                id: "temperature",
                title: "Temperatura",
                value: weather.temperatura.toFixed(1),
                unit: "°C",
                updated: lastUpdate
            },
            {
                id: "humidity",
                title: "Humedad",
                value: weather.humedad,
                unit: "%",
                updated: lastUpdate
            },
            {
                id: "hydration",
                title: "Nivel de Hidratación",
                value: weather.hydration_level,
                unit: "/10",
                updated: lastUpdate
            },
        ]
        : [
            { id: "heat-level", title: "Nivel de Calor", value: "—", unit: "/100" },
            { id: "temperature", title: "Temperatura", value: "—", unit: "°C" },
            { id: "humidity", title: "Humedad", value: "—", unit: "%" },
            { id: "hydration", title: "Nivel de Hidratación", value: "—", unit: "/10" },
        ];

    // Alertas inteligentes
    let alertaTexto = "No hay alertas activas en este momento.";

    if (weather?.thermal_risk >= 3) {
        alertaTexto = `⚠ Riesgo térmico elevado: ${weather.condicion}`;
    }

    if (weather?.uv_index >= 7) {
        alertaTexto = `⚠ Índice UV muy alto (${weather.uv_index})`;
    }

    if (weather?.sensacion_termica >= 40) {
        alertaTexto = `⚠ Sensación térmica muy alta (${weather.sensacion_termica}°C)`;
    }

    return (
        <div className="hr-container">
            <Navbar />

            <div className="hr-content">

                {/* ALERTAS DEL CLIMA */}
                <div className="hr-alerts" role="status" aria-live="polite">
                    <div className="hr-alerts__inner">
                        {loadingWeather ? "Cargando datos del clima…" : alertaTexto}
                    </div>
                </div>

                <div className="hr-grid">

                    {/* LEFT COLUMN */}
                    <section className="hr-left">

                        {/* Mini-mapa con header integrado */}
                        <div className="map-preview-card">
                            <div className="map-preview-header">
                                <div>
                                    <h3>🗺️ Cartagena</h3>
                                    <p className="map-location-desc">Zonas de calor y puntos de agua</p>
                                </div>
                            </div>
                            <MapView mini={true} onExpand={() => setOpenMap(true)} />
                        </div>

                        <ClimateChart feelsLike={weather?.sensacion_termica} />

                    </section>

                    {/* RIGHT COLUMN */}
                    <aside className="hr-right">

                        {/* STAT CARDS */}
                        <div className="hr-stats">
                            {stats.map((s) => (
                                <StatCard
                                    key={s.id}
                                    title={s.title}
                                    value={s.value}
                                    unit={s.unit}
                                    updated={s.updated}
                                />
                            ))}
                        </div>

                        {/* INDICADORES */}
                        <IndicatorsPanel
                            uv={weather?.uv_index || 0}
                            feelsLike={weather?.sensacion_termica || 0}
                            risk={weather?.thermal_risk || 0}
                            hydration={weather?.hydration_level || 0}
                        />
                    </aside>

                </div>

                <ReportCallToAction />
            </div>

            {/* Mapa grande */}
            <MapFullscreenModal open={openMap} onClose={() => setOpenMap(false)} />

        </div>
    );
}
