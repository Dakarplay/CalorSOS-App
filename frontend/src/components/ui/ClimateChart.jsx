// src/components/ui/ClimateChart.jsx
import React from "react";
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
    CartesianGrid,
} from "recharts";

export default function ClimateChart({ feelsLike }) {

    // Generamos datos suaves alrededor del valor real
    const base = feelsLike || 30;

    const data = Array.from({ length: 12 }).map((_, i) => ({
        hora: `${i + 6}:00`,
        sensacion: Number((base + Math.sin(i / 2) * 2).toFixed(3)),  // 3 decimales
    }));

    return (
        <div className="chart-container">
            <h3>Tendencia de Sensación Térmica (estimada)</h3>

            <ResponsiveContainer width="100%" height={250}>
                <LineChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" opacity={0.2} />
                    <XAxis dataKey="hora" stroke="#aaa" />
                    <YAxis stroke="#aaa" domain={[20, 50]} />
                    <Tooltip />
                    <Line
                        type="monotone"
                        dataKey="sensacion"
                        stroke="#ff7300"
                        strokeWidth={3}
                        dot={false}
                        activeDot={{ r: 6 }}
                    />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
}
