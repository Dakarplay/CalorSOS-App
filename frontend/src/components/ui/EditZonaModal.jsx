// Inicio EditZonaModal.jsx

// frontend/src/components/ui/EditZonaModal.jsx

// Componente modal para editar zonas frescas en el panel de administración

// Importaciones de React
import React from "react";

// Importación de estilos
import "../../assets/styles/Admin.css";

// Componente funcional principal
export default function EditZonaModal({ open, onClose, zona, onSave }) {
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
                    <h2 className="rm-title">Editar Zona Fresca</h2>
                    <form
                        className="rm-form"
                        onSubmit={async (e) => {
                            e.preventDefault();
                            const formData = new FormData(e.target);
                            const updates = {
                                nombre: formData.get("nombre"),
                                descripcion: formData.get("descripcion"),
                                tipo: formData.get("tipo")
                            };

                            try {
                                await onSave(updates);
                                onClose();
                            } catch (error) {
                                alert("Error al actualizar zona");
                            }
                        }}
                    >
                        <div>
                            <label className="rm-label" htmlFor="nombre">Nombre:</label>
                            <input
                                className="rm-input"
                                type="text"
                                id="nombre"
                                name="nombre"
                                defaultValue={zona?.nombre || ""}
                                required
                            />
                        </div>

                        <div>
                            <label className="rm-label" htmlFor="descripcion">Descripción:</label>
                            <textarea
                                className="rm-textarea"
                                id="descripcion"
                                name="descripcion"
                                defaultValue={zona?.descripcion || ""}
                            />
                        </div>

                        <div>
                            <label className="rm-label" htmlFor="tipo">Tipo:</label>
                            <select
                                className="rm-input"
                                id="tipo"
                                name="tipo"
                                defaultValue={zona?.tipo || "urbana"}
                                required
                            >
                                <option value="urbana">Urbana</option>
                                <option value="natural">Natural</option>
                                <option value="artificial">Artificial</option>
                            </select>
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
                                Actualizar Zona
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

// Fin EditZonaModal.jsx
