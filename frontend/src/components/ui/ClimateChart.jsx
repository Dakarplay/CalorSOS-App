import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";
import { getClimaHistoricoTempHumedad } from "../../services/climaService";
import LoaderPremium from "../../components/common/LoaderPremium";
import "../../assets/styles/ClimateChart.css";

export default function TempHumedadChart() {
    const [historico, setHistorico] = useState([]);
    const [dias, setDias] = useState(1);
    const [loading, setLoading] = useState(true);

    const botonesDias = [1, 2, 3, 4, 5, 6, 7];

    useEffect(() => {
        async function fetchHistorico() {
            setLoading(true);
            const data = await getClimaHistoricoTempHumedad(dias);
            setHistorico(data);
            setLoading(false);
        }
        fetchHistorico();
    }, [dias]);

    // Tooltip personalizado
    const CustomTooltip = ({ active, payload, label }) => {
        if (active && payload && payload.length) {
            const date = new Date(label);
            return (
                <div className="custom-tooltip" style={{
                    backgroundColor: "#1f2a33",
                    border: "1px solid rgba(255,255,255,0.1)",
                    borderRadius: "8px",
                    padding: "8px",
                    color: "#fff",
                    fontSize: "13px"
                }}>
                    <p>{dias === 1 
                        ? `Hora: ${date.getHours()}:${("0"+date.getMinutes()).slice(-2)}` 
                        : `Fecha: ${date.getMonth()+1}-${date.getDate()} ${date.getHours()}:${("0"+date.getMinutes()).slice(-2)}`}</p>
                    {payload.map((p) => (
                        <p key={p.dataKey} style={{ color: p.stroke, margin: 0 }}>
                            {p.dataKey === "temperatura" ? "Temp" : "Humedad"}: {p.value}{p.dataKey === "temperatura" ? "°C" : "%"}
                        </p>
                    ))}
                </div>
            );
        }
        return null;
    };

    return (
        <div className="chart-container">
            <h3>Gráfico de Temperatura y Humedad</h3>

            <div className="chart-buttons">
                {botonesDias.map((d) => (
                    <button
                        key={d}
                        className={dias === d ? "active" : ""}
                        onClick={() => setDias(d)}
                    >
                        {d} Día{d > 1 ? "s" : ""}
                    </button>
                ))}
            </div>

            {loading && (
                <div className="chart-loader">
                    <LoaderPremium />
                </div>
            )}

            <ResponsiveContainer width="100%" height={350}>
                <LineChart
                    data={historico}
                    margin={{ top: 20, right: 40, left: 0, bottom: 5 }}
                    isAnimationActive={false}
                >
                    <CartesianGrid strokeDasharray="3 3" opacity={0.2} />
                    <XAxis
                        dataKey="timestamp"
                        stroke="#cfd9e5"
                        tick={false}
                        interval={0} // todos los puntos seleccionables
                        tickFormatter={(value) => {
                            const date = new Date(value);
                            if (dias === 1) {
                                return `${date.getHours()}:${("0"+date.getMinutes()).slice(-2)}`; // HH:MM
                            }
                            return ""; // no mostrar ticks para >1 día
                        }}
                    />
                    <YAxis yAxisId="left" stroke="#ff7300" tick={{ fontSize: 12 }} />
                    <YAxis yAxisId="right" orientation="right" stroke="#0074d9" tick={{ fontSize: 12 }} />
                    <Tooltip
                        content={<CustomTooltip />}
                        cursor={{ stroke: "#aaa", strokeWidth: 1, strokeDasharray: "3 3" }}
                    />
                    <Line
                        yAxisId="left"
                        type="monotone"
                        dataKey="temperatura"
                        stroke="#ff7300"
                        strokeWidth={2.5}
                        dot={false}
                        activeDot={{ r: 6 }}
                        connectNulls
                    />
                    <Line
                        yAxisId="right"
                        type="monotone"
                        dataKey="humedad"
                        stroke="#0074d9"
                        strokeWidth={2.5}
                        dot={false}
                        activeDot={{ r: 6 }}
                        connectNulls
                    />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
}
