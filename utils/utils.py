from functools import wraps
from math import ceil

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
                return render_template("acceso_restringido.html")  # Redirige al usuario a la página de inicio de sesión

        return decorated_view


class RegistroActividades():

    def registrar_actividades(id, accion, descripcion):
        RegistroDeActividades.create(
            usuario=int(id),
            accion=accion,
            descripcion=descripcion
        )

    # def buscar_registros(termino, columna_busqueda):
    #     termino = termino or ''
    #     columna_busqueda = columna_busqueda or ''
    #     query = "SELECT * FROM buscar_registros()"
    #     # Agregar condiciones solo si los parámetros no están vacíos
    #     if termino or columna_busqueda:
    #         query += f" WHERE LOWER({columna_busqueda}) ILIKE '%{termino}%'"
    #         query = f"SELECT * FROM buscar_registros('{termino}', '{columna_busqueda}')"
    #
    #     # Ejecutar la consulta y obtener los resultados
    #     resultados = list(db.execute_sql(query))
    #
    #     registros_peewee = [RegistroDTO(
    #         registro_id=resultado[0],
    #         usuario_id=resultado[1],
    #         nombre_usuario=resultado[2],
    #         accion=resultado[3],
    #         fecha_hora=RegistroActividades.fomatear_fecha(resultado[4]),  # Aquí se llama la función
    #         descripcion=resultado[5]
    #     ) for resultado in resultados]
    #
    #     return registros_peewee

    def buscar_registros(termino, columna_busqueda, page, per_page):
        termino = termino or ''
        columna_busqueda = columna_busqueda or ''

        # Consulta para obtener el número total de registros con condiciones de búsqueda
        count_query = "SELECT COUNT(*) FROM buscar_registros()"
        if termino or columna_busqueda:
            count_query += f" WHERE LOWER({columna_busqueda}) ILIKE %s"
            parametros_count = (f"%{termino}%",)
        else:
            parametros_count = ()
        count_result = db.execute_sql(count_query, parametros_count).fetchone()
        total_registros = count_result[0]

        # Consulta para obtener registros con condiciones de búsqueda y aplicar paginación en la base de datos
        query = "SELECT * FROM buscar_registros()"

        # Agregar condiciones solo si los parámetros no están vacíos
        if termino or columna_busqueda:
            query += f" WHERE LOWER({columna_busqueda}) ILIKE %s"
            parametros = (f"%{termino}%",)
        else:
            parametros = ()

        # Calcular el índice de inicio para la paginación
        start = (page - 1) * per_page

        # Agregar la cláusula LIMIT y OFFSET para paginar directamente en la base de datos
        query += f" LIMIT {per_page} OFFSET {start}"

        # Ejecutar la consulta y obtener los resultados
        resultados = list(db.execute_sql(query, parametros))

        # Calcular el número total de páginas
        total_paginas = ceil(total_registros / per_page)

        registros_peewee = [RegistroDTO(
            registro_id=resultado[0],
            usuario_id=resultado[1],
            nombre_usuario=resultado[2],
            accion=resultado[3],
            fecha_hora=RegistroActividades.fomatear_fecha(resultado[4]),  # Aquí se llama la función
            descripcion=resultado[5]
        ) for resultado in resultados]

        # Devolver los resultados junto con la información de paginación
        return {
            'registros': registros_peewee,
            'total_registros': total_registros,
            'total_paginas': total_paginas,
            'pagina_actual': page
        }

    @staticmethod
    def fomatear_fecha(timestamp):
        timestamp_str = str(timestamp)
        parts = timestamp_str.split(".")
        timestamp_without_fraction = parts[0]
        return timestamp_without_fraction

    @staticmethod
    def saludar(nombre):
        print(nombre)
        return "Salud :" + nombre


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
