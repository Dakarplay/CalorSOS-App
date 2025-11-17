// Inicio Configuracion.jsx

// frontend/src/pages/Configuracion.jsx

// Página para configuración de usuario y aplicación

// Importación de componentes
import NavbarSmart from '../components/ui/NavbarSmart';

// Importación de estilos
import "../assets/styles/Configuracion.css";

export default function Configuracion() {
    return (

        <div className="page-container">
            <NavbarSmart />
            <div className="page-content">
                <h1 className="page-title">Configuración</h1>
                {/* Contenido de la página de configuración */}
            </div>
        </div>
    );
}

// Fin Configuracion.jsx
