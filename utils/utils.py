
from functools import wraps
from flask import app, flash, redirect, render_template, session, url_for
from models.registro_movimientos import RegistroDTO
from models.usuario import RegistroDeActividades, db


class RestriccionUsuarios():
    # Función decoradora para verificar si el usuario es un administrador
    @staticmethod
    def admin_required(view_func):
        @wraps(view_func)
        def decorated_view(*args, **kwargs):
            if 'tipo' in session and session['tipo'] == 'Admin':
                return view_func(*args, **kwargs)
            else:
                return render_template("acceso_restringido.html") # Redirige al usuario a la página de inicio de sesión
        return decorated_view
    
    



class RegistroActividades():

    def registrar_actividades(id, accion, descripcion):
        RegistroActividades.create(
            usuario=int(id),
            accion=accion,
            descripcion=descripcion
        )

    def buscar_registros(termino, columna_busqueda):
        termino = termino or ''
        columna_busqueda = columna_busqueda or ''
        query = "SELECT * FROM buscar_registros()"
        # Agregar condiciones solo si los parámetros no están vacíos
        if termino or columna_busqueda:
            query += f" WHERE LOWER({columna_busqueda}) ILIKE '%{termino}%'"
            query = f"SELECT * FROM buscar_registros('{termino}', '{columna_busqueda}')"

        # Ejecutar la consulta y obtener los resultados
        resultados = list(db.execute_sql(query))

        registros_peewee = [RegistroDTO(
            registro_id=resultado[0],
            usuario_id=resultado[1],
            nombre_usuario=resultado[2],
            accion=resultado[3],
            fecha_hora=RegistroActividades.fomatear_fecha(resultado[4]),  # Aquí se llama la función
            descripcion=resultado[5]
        ) for resultado in resultados]

        return registros_peewee

    @staticmethod
    def fomatear_fecha(timestamp):
        timestamp_str = str(timestamp)
        parts = timestamp_str.split(".")
        timestamp_without_fraction = parts[0]
        return timestamp_without_fraction


class ValidadorUsuario():
    def validar_usuario(usuario):
        longitud_minima = 3
        longitud_maxima = 20

        if longitud_minima <= len(usuario) <= longitud_maxima:
            # Verificar si el usuario contiene solo caracteres alfanuméricos y no permite espacios
            if usuario.isalnum() and ' ' not in usuario:
                return True
        return False
    
    def validar_contrasena(contrasena):
        longitud_minima = 8
        contiene_mayuscula = any(c.isupper() for c in contrasena)
        contiene_minuscula = any(c.islower() for c in contrasena)
        contiene_numero = any(c.isdigit() for c in contrasena)

        if (
            longitud_minima <= len(contrasena) and
            contiene_mayuscula and
            contiene_minuscula and
            contiene_numero
        ):
            return True
        else:
            mensaje_error = "La contraseña debe cumplir con los siguientes criterios:"
            if len(contrasena) < longitud_minima:
                mensaje_error += f"\n- Tener al menos {longitud_minima} caracteres."
            if not contiene_mayuscula:
                mensaje_error += "\n- Contener al menos una letra mayúscula."
            if not contiene_minuscula:
                mensaje_error += "\n- Contener al menos una letra minúscula."
            if not contiene_numero:
                mensaje_error += "\n- Contener al menos un número."

            flash(mensaje_error, 'error')
            return False