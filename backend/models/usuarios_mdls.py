# Inicio usuarios_mdls.py

# backend/models/usuarios_mdls.py

# Importaciones necesarias para el modelo de usuarios
from backend.app.security.hashing import verify_password
from backend.app.security.jwt_handler import crear_token
from backend.database.supabase_config import supabase
from fastapi import HTTPException
from typing import Optional

# Clase principal para manejar usuarios
class UsuarioModel:
    """
    Modelo de acceso a datos para la tabla 'usuarios' en Supabase.
    Gestiona operaciones CRUD de usuarios y autenticación.
    """

    @staticmethod
    def crear_usuario(nombre: str, correo: str, password: str, telefono: Optional[str] = None, rol: str = "usuario"):
        """
        Crea un nuevo usuario en la base de datos.
        Almacena la contraseña cifrada y otros datos del usuario.
        """
        try:
            # Preparar datos para inserción
            data = {
                "nombre": nombre,
                "correo": correo,
                "telefono": telefono,
                "rol": rol,
                "password": password  # Se almacena el hash, no el texto plano
            }
            # Ejecutar inserción en Supabase
            response = supabase.table("usuarios").insert(data).execute()
            if not response.data:
                raise HTTPException(status_code=400, detail="No se pudo crear el usuario")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la creación
            raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")

    @staticmethod
    def obtener_usuario_por_id(id_usuario: str):
        """
        Obtiene un usuario específico por su ID.
        Busca en la base de datos y retorna el usuario si existe.
        """
        try:
            # Consultar usuario por ID
            response = supabase.table("usuarios").select("*").eq("id_usuario", id_usuario).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener usuario: {str(e)}")

    @staticmethod
    def obtener_usuario_por_correo(correo: str):
        """
        Busca un usuario por su correo electrónico.
        Útil para procesos de login y verificación de existencia.
        """
        try:
            # Consultar usuario por correo
            response = supabase.table("usuarios").select("*").eq("correo", correo).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al obtener usuario por correo: {str(e)}")

    @staticmethod
    def listar_usuarios():
        """
        Lista todos los usuarios registrados en la base de datos.
        Retorna una lista completa de usuarios.
        """
        try:
            # Consultar todos los usuarios
            response = supabase.table("usuarios").select("*").execute()
            return response.data
        except Exception as e:
            # Manejar errores en la consulta
            raise HTTPException(status_code=500, detail=f"Error al listar usuarios: {str(e)}")

    @staticmethod
    def actualizar_usuario(id_usuario: str, data: dict):
        """
        Actualiza la información de un usuario existente.
        Modifica los campos especificados en el diccionario data.
        """
        try:
            # Ejecutar actualización
            response = supabase.table("usuarios").update(data).eq("id_usuario", id_usuario).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Usuario no encontrado para actualizar")
            return response.data[0]
        except Exception as e:
            # Manejar errores en la actualización
            raise HTTPException(status_code=500, detail=f"Error al actualizar usuario: {str(e)}")

    @staticmethod
    def eliminar_usuario(id_usuario: str):
        """
        Elimina un usuario por su ID.
        Remueve el registro de la base de datos.
        """
        try:
            # Ejecutar eliminación
            response = supabase.table("usuarios").delete().eq("id_usuario", id_usuario).execute()
            if not response.data:
                return {"message": "No se encontró el usuario"}
            return {"message": "Usuario eliminado correctamente"}
        except Exception as e:
            # Manejar errores en la eliminación
            raise HTTPException(status_code=500, detail=f"Error al eliminar usuario: {str(e)}")

    @staticmethod
    def autenticar_usuario(correo: str, password: str):
        """
        Verifica las credenciales del usuario y genera un token JWT si son válidas.
        Compara la contraseña proporcionada con el hash almacenado.
        """
        try:
            # Buscar usuario por correo
            response = supabase.table("usuarios").select("*").eq("correo", correo).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            usuario = response.data[0]
            hashed_password = usuario.get("password")

            # Verificar contraseña
            if not verify_password(password, hashed_password):
                raise HTTPException(status_code=401, detail="Contraseña incorrecta")

            # Generar token JWT
            token = crear_token({"id_usuario": usuario["id_usuario"], "correo": usuario["correo"], "rol": usuario["rol"]})

            # Retornar token y datos del usuario
            return {"access_token": token, "token_type": "bearer", "usuario": usuario}

        except Exception as e:
            # Manejar errores en la autenticación
            raise HTTPException(status_code=500, detail=f"Error en autenticación: {str(e)}")

# Fin usuarios_mdls.py
