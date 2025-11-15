// src/components/ui/StatCard.jsx
import React from "react";
import "../../assets/styles/StatCard.css";

export default function StatCard({ title, value, unit }) {
  return (
    <div className="sc-card" role="group" aria-labelledby={`sc-${title}`}>
      <div className="sc-title" id={`sc-${title}`}>{title}</div>
      <div className="sc-value" aria-hidden="false">
        <span className="sc-number">{value}</span>
        <span className="sc-unit">{unit}</span>
      </div>
      <div className="sc-foot">Última actualización: —</div>
    </div>
  );
}
