// Inicio Alertas.jsx

// frontend/src/pages/Alertas.jsx

// Página para mostrar alertas de calor y notificaciones al usuario

// Importación de componentes
import NavbarSmart from '../components/ui/NavbarSmart';

// Importación de estilos
import "../assets/styles/Alertas.css";

export default function Alertas() {
    return (
        <div className="page-container">
            <NavbarSmart />
            <div className="page-content">
                <h1 className="page-title">Alertas</h1>
                {/* Aquí puedes agregar tus tarjetas, mapas, listas, etc. */}
            </div>
        </div>
    );
}

// Fin Alertas.jsx
