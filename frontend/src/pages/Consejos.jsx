// Inicio Consejos.jsx

// frontend/src/pages/Consejos.jsx

// Página para mostrar consejos de prevención contra el calor

// Importaciones de React y hooks
import React, { useState } from "react";

// Estilos
import "../assets/styles/Consejos.css";

// Componentes
import Navbar from "../components/ui/NavbarSmart.jsx";

// Datos
import { consejosData } from "../data/consejosData.js";


// ===================================
// COMPONENTE PRINCIPAL
// ===================================
export default function Consejos() {

    // -----------------------------------
    // CATEGORÍAS DISPONIBLES
    // -----------------------------------
    const categoriasUnicas = [
        "Hidratación",
        "Exposición al sol",
        "Protección personal",
        "Actividad física",
        "Hogar",
        "Control corporal",
        "Alimentación",
        "Comunidad",
        "Emergencias",
    ];

    // -----------------------------------
    // ESTADO: Filtros seleccionados
    // -----------------------------------
    const [filtros, setFiltros] = useState([]);

    // -----------------------------------
    // FUNCIÓN: Activar o desactivar filtro
    // -----------------------------------
    const toggleFiltro = (categoria) => {
        if (filtros.includes(categoria)) {
            setFiltros(filtros.filter((f) => f !== categoria));
        } else {
            setFiltros([...filtros, categoria]);
        }
    };

    // -----------------------------------
    // FUNCIÓN: Limpiar todos los filtros
    // -----------------------------------
    const limpiarFiltros = () => setFiltros([]);

    // -----------------------------------
    // CONTEO: Consejos por categoría
    // -----------------------------------
    const cuentaPorCategoria = categoriasUnicas.reduce((acc, categoria) => {
        acc[categoria] = consejosData.filter(
            c => c.categoria === categoria
        ).length;
        return acc;
    }, {});

    const totalConsejos = consejosData.length;
    const totalCategorias = categoriasUnicas.length;

    // -----------------------------------
    // FILTRO: Aplicar filtros activos
    // -----------------------------------
    const consejosFiltrados =
        filtros.length === 0
            ? consejosData
            : consejosData.filter(c => filtros.includes(c.categoria));


    // ===================================
    // RENDER
    // ===================================
    return (
        <div className="consejos-container">
            {/* Navbar */}
            <Navbar />

            <div className="consejos-layout">

                {/* SIDEBAR DE FILTROS */}
                <aside className="consejos-sidebar">
                    <h2 className="sidebar-title">Filtrar por categoría</h2>

                    <p className="sidebar-subtitle-categorias">
                        Categorías: {totalCategorias}
                    </p>

                    <p className="sidebar-subtitle-consejos">
                        Consejos: {totalConsejos}
                    </p>

                    <button className="sidebar-clear" onClick={limpiarFiltros}>
                        Ver todos
                    </button>

                    {/* Checklist de categorías */}
                    <div className="sidebar-checklist">
                        {categoriasUnicas.map((cat) => (
                            <label key={cat} className="sidebar-item">
                                <input
                                    type="checkbox"
                                    checked={filtros.includes(cat)}
                                    onChange={() => toggleFiltro(cat)}
                                />
                                {cat} ({cuentaPorCategoria[cat]})
                            </label>
                        ))}
                    </div>
                </aside>

                {/* CONTENIDO PRINCIPAL */}
                <main className="consejos-content">
                    <h1 className="consejos-title">
                        CONSEJOS PARA PREVENIR RIESGOS POR CALOR
                    </h1>

                    {/* Grid de tarjetas */}
                    <div className="consejos-grid">
                        {consejosFiltrados.map((consejo, idx) => (
                            <div className="consejo-card" key={idx}>
                                <div className="consejo-header">
                                    <h3>{consejo.titulo}</h3>
                                </div>

                                <p className="consejo-desc">
                                    {consejo.descripcion}
                                </p>

                                <span
                                    className="consejo-tag"
                                    data-categoria={consejo.categoria}
                                >
                                    {consejo.categoria}
                                </span>
                            </div>
                        ))}
                    </div>
                </main>
            </div>
        </div>
    );
}

// Fin Consejos.jsx