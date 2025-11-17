// Inicio EditPuntoModal.jsx

// frontend/src/components/ui/EditPuntoModal.jsx

// Componente modal para editar puntos de hidratación en el panel de administración

// Importaciones de React
import React from "react";

// Importación de estilos
import "../../assets/styles/Admin.css";

// Componente funcional principal
export default function EditPuntoModal({ open, onClose, punto, onSave }) {
    // No renderizar si el modal no está abierto
    if (!open) return null;

    return (
        <div className="rm-backdrop">
            <div className="rm-window">
                {/* Botón para cerrar el modal */}
                <button className="rm-close-btn" onClick={onClose}>
                    ✕
                </button>

                {/* Contenido del modal */}
                <div className="rm-content">
                    <h2 className="rm-title">Editar Punto de Hidratación</h2>
                    <form
                        className="rm-form"
                        onSubmit={async (e) => {
                            e.preventDefault();
                            const formData = new FormData(e.target);
                            const updates = {
                                nombre: formData.get("nombre"),
                                descripcion: formData.get("descripcion")
                            };

                            try {
                                await onSave(updates);
                                onClose();
                            } catch (error) {
                                alert("Error al actualizar punto");
                            }
                        }}
                    >
                        <div>
                            <label className="rm-label" htmlFor="nombre_punto">Nombre:</label>
                            <input
                                className="rm-input"
                                type="text"
                                id="nombre_punto"
                                name="nombre"
                                defaultValue={punto?.nombre || ""}
                                required
                            />
                        </div>

                        <div>
                            <label className="rm-label" htmlFor="descripcion_punto">Descripción:</label>
                            <textarea
                                className="rm-textarea"
                                id="descripcion_punto"
                                name="descripcion"
                                defaultValue={punto?.descripcion || ""}
                            />
                        </div>

                        <div className="rm-actions">
                            <button
                                type="button"
                                className="rm-btn-cancel"
                                onClick={onClose}
                            >
                                Cancelar
                            </button>
                            <button type="submit" className="rm-btn-send">
                                Actualizar Punto
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

// Fin EditPuntoModal.jsx
