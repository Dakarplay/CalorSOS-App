// Inicio LoaderPremium.jsx

// frontend/src/components/common/LoaderPremium.jsx

// Componente de loader premium con opción mini

// Componente funcional para mostrar loader
export default function LoaderPremium({ mini = false }) {
    return (
        <div className={`thermal-loader ${mini ? "btn-mini" : ""}`}></div>
    );
}

// Fin LoaderPremium.jsx
