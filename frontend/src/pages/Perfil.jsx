import { useContext } from "react";
import { UserContext } from "../context/UserContext.jsx";

export default function Perfil() {
  const { user, logout } = useContext(UserContext);

  return (
    <div>
      <h1>Perfil</h1>
      <p>Usuario: {user?.nombre}</p>

      <button onClick={logout}>Cerrar sesión</button>
    </div>
  );
}
