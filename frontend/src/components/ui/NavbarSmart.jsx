// Inicio NavbarSmart.jsx

// frontend/src/components/ui/NavbarSmart.jsx

// Componente de navegación inteligente con menú desplegable

// Importaciones de React y hooks
import React, { useContext, useState, useRef, useEffect } from "react";

// Importaciones de React Router
import { NavLink, useNavigate } from "react-router-dom";

// Importación del contexto de usuario
import { UserContext } from "../../context/UserContext";

// Importación del logo y estilos
import logo from "../../assets/images/logo.svg";
import "../../assets/styles/NavbarSmart.css";

// Componente funcional principal
export default function NavbarSmart() {
    // Estado del componente
    const { user, logout } = useContext(UserContext);
    const [openMenu, setOpenMenu] = useState(false);
    const navigate = useNavigate();
    const menuRef = useRef(null);

    // Debug del contexto de usuario
    useEffect(() => {
        console.log("User context en Navbar:", user);
    }, [user]);

    // Función para manejar el logout
    const handleLogout = () => {
        logout();
        navigate("/login");
    };

    // Cerrar menú al hacer clic fuera
    useEffect(() => {
        const handler = (e) => {
            if (menuRef.current && !menuRef.current.contains(e.target)) {
                setOpenMenu(false);
            }
        };
        document.addEventListener("mousedown", handler);
        return () => document.removeEventListener("mousedown", handler);
    }, []);

    // Función para obtener el nombre del usuario
    const getUserName = () => {
        if (!user) return "Usuario";

        // Usar el nombre real si existe, sino fallback al email
        if (user.nombre) {
            return user.nombre;
        }

        // Intentar diferentes propiedades comunes
        return user.name || user.username || user.displayName || user.fullName || "Usuario";
    };

    // Obtener la primera letra del nombre para el avatar
    const getUserInitial = () => {
        const name = getUserName();
        return name !== "Usuario" ? name[0].toUpperCase() : "U";
    };

    // Obtener email si existe
    const getUserEmail = () => {
        return user?.email || user?.correo || "";
    };

    return (
        <header className="ns-header">
            {/* Lado izquierdo del header */}
            <div className="ns-left">
                <div className="ns-brand">
                    <img src={logo} alt="CalorSOS Logo" className="ns-logo-img" />
                    <span className="ns-brand__title">CalorSOS</span>
                </div>

                <nav className="ns-nav">
                    <NavLink to="/" className={({ isActive }) =>
                        `ns-link ${isActive ? "active" : ""}`
                    }>
                        Inicio
                    </NavLink>
                    <NavLink to="/zonas-frescas" className={({ isActive }) =>
                        `ns-link ${isActive ? "active" : ""}`
                    }>
                        Zonas Frescas
                    </NavLink>
                    <NavLink to="/puntos-hidratacion" className={({ isActive }) =>
                        `ns-link ${isActive ? "active" : ""}`
                    }>
                        Puntos de Hidratación
                    </NavLink>
                    <NavLink to="/alertas" className={({ isActive }) =>
                        `ns-link ${isActive ? "active" : ""}`
                    }>
                        Alertas
                    </NavLink>
                    <NavLink to="/consejos" className={({ isActive }) =>
                        `ns-link ${isActive ? "active" : ""}`
                    }>
                        Consejos
                    </NavLink>
                </nav>
            </div>

            {/* Lado derecho del header */}
            <div className="ns-right" ref={menuRef}>
                {/* Mensaje de bienvenida */}
                <div className="ns-welcome-message">
                    Hola <span className="ns-username">{getUserName()}</span>
                </div>

                {/* Avatar como botón */}
                <div
                    className="ns-avatar-btn"
                    onClick={() => setOpenMenu(!openMenu)}
                    role="button"
                    tabIndex={0}
                    onKeyDown={(e) => {
                        if (e.key === 'Enter' || e.key === ' ') {
                            setOpenMenu(!openMenu);
                        }
                    }}
                >
                    <div className="ns-avatar">
                        {getUserInitial()}
                    </div>
                </div>

                {openMenu && (
                    <div className="ns-profile-menu">
                        <div className="ns-profile-header">
                            <div className="ns-profile-name">{getUserName()}</div>
                            {getUserEmail() && (
                                <div style={{ fontSize: '12px', color: '#666' }}>
                                    {getUserEmail()}
                                </div>
                            )}
                        </div>

                        <button
                            className="ns-profile-item"
                            onClick={() => {
                                setOpenMenu(false);
                                setTimeout(() => navigate("/perfil"), 150);
                            }}
                        >
                            Ver perfil
                        </button>
                        <button
                            className="ns-profile-item"
                            onClick={() => {
                                setOpenMenu(false);
                                navigate("/configuracion");
                            }}
                        >
                            Configuración
                        </button>
                        {user && user.rol === "admin" && (
                            <button
                                className="ns-profile-item admin-link"
                                onClick={() => {
                                    setOpenMenu(false);
                                    navigate("/admin");
                                }}
                            >
                                Panel de Administración
                            </button>
                        )}

                        <hr />

                        <button
                            className="ns-profile-item logout"
                            onClick={handleLogout}
                        >
                            Cerrar sesión
                        </button>
                    </div>
                )}
            </div>
        </header>
    );
}

// Fin NavbarSmart.jsx
