# backend/app/routers/usuarios.py
from fastapi import APIRouter, HTTPException, Form, Depends, Body
from backend.models.usuarios_mdls import UsuarioModel
from backend.app.security.hashing import hash_password, verify_password
from backend.app.security.jwt_handler import crear_token, verificar_token, verificar_rol

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# ======================================================
# REGISTRO DE USUARIOS
# ======================================================
@router.post("/register")
def register(
    nombre: str = Form(...),
    correo: str = Form(...),
    password: str = Form(...),
    telefono: str = Form(None),
    rol: str = Form("usuario")
):
    try:
        existente = UsuarioModel.obtener_usuario_por_correo(correo)
        if existente:
            raise HTTPException(status_code=400, detail="El correo ya está registrado")

        hashed_pw = hash_password(password)
        usuario = UsuarioModel.crear_usuario(
            nombre=nombre,
            correo=correo,
            password=hashed_pw,
            telefono=telefono,
            rol=rol
        )

        return {
            "status": "success",
            "message": "Usuario registrado correctamente",
            "data": usuario
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ======================================================
# LOGIN DE USUARIOS
# ======================================================
@router.post("/login")
def login(correo: str = Form(...), password: str = Form(...)):
    usuario = UsuarioModel.obtener_usuario_por_correo(correo)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not verify_password(password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = crear_token({
        "id_usuario": usuario["id_usuario"],
        "correo": usuario["correo"],
        "rol": usuario["rol"]
    })

    return {
        "status": "success",
        "access_token": token,
        "token_type": "bearer"
    }


# ======================================================
# PERFIL (UNA SOLA RUTA, FUNCIONANDO)
# ======================================================
@router.get("/perfil")
def perfil(datos_usuario: dict = Depends(verificar_token)):
    """
    Devuelve el usuario actual basado en el token.
    """
    # Obtener el usuario completo desde la base de datos
    usuario_completo = UsuarioModel.obtener_usuario_por_id(datos_usuario["id_usuario"])

    # Filtrar la contraseña por seguridad
    usuario_filtrado = {
        "id_usuario": usuario_completo["id_usuario"],
        "nombre": usuario_completo["nombre"],
        "correo": usuario_completo["correo"],
        "telefono": usuario_completo.get("telefono"),
        "rol": usuario_completo["rol"]
    }

    return {
        "status": "success",
        "usuario_actual": usuario_filtrado
    }


# ======================================================
# ADMIN - OBTENER TODOS LOS USUARIOS
# ======================================================
@router.get("/")
def listar_todos_los_usuarios(datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    usuarios = UsuarioModel.listar_usuarios()
    return {
        "status": "success",
        "total": len(usuarios),
        "usuarios": usuarios
    }


# ======================================================
# OBTENER USUARIO POR ID
# ======================================================
@router.get("/{id_usuario}")
def obtener_usuario_por_id(id_usuario: str, datos_usuario: dict = Depends(verificar_token)):

    if datos_usuario["rol"] != "admin" and datos_usuario["id_usuario"] != id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este perfil")

    usuario = UsuarioModel.obtener_usuario_por_id(id_usuario)

    return {
        "status": "success",
        "usuario": usuario
    }


# ======================================================
# ACTUALIZAR
# ======================================================
@router.put("/{id_usuario}")
def actualizar_usuario(
    id_usuario: str,
    data: dict = Body(...),
    datos_usuario: dict = Depends(verificar_token)
):

    if datos_usuario["rol"] != "admin" and datos_usuario["id_usuario"] != id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permisos para modificar este perfil")

    usuario_actualizado = UsuarioModel.actualizar_usuario(id_usuario, data)

    return {
        "status": "success",
        "message": "Usuario actualizado correctamente",
        "usuario": usuario_actualizado
    }


# ======================================================
# ELIMINAR (ADMIN)
# ======================================================
@router.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: str, datos_usuario: dict = Depends(verificar_rol(["admin"]))):
    return UsuarioModel.eliminar_usuario(id_usuario)

# ======================================================
# CAMBIAR CONTRASEÑA
# ======================================================
@router.put("/{id_usuario}/cambiar-password")
def cambiar_password(
    id_usuario: str,
    data: dict = Body(...),
    datos_usuario: dict = Depends(verificar_token)
):
    """
    Endpoint específico para cambiar contraseña con verificación
    """
    if datos_usuario["rol"] != "admin" and datos_usuario["id_usuario"] != id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permisos para modificar este perfil")

    # Verificar contraseña actual
    usuario = UsuarioModel.obtener_usuario_por_id(id_usuario)
    if not verify_password(data["currentPassword"], usuario["password"]):
        raise HTTPException(status_code=401, detail="Contraseña actual incorrecta")

    # Hashear nueva contraseña
    nueva_password_hasheada = hash_password(data["newPassword"])

    # Actualizar en la base de datos
    usuario_actualizado = UsuarioModel.actualizar_usuario(id_usuario, {
        "password": nueva_password_hasheada
    })

    return {
        "status": "success",
        "message": "Contraseña cambiada correctamente"
    }