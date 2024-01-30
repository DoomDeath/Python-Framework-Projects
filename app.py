# noinspection PyInterpreter
import base64
import datetime
from flask import Flask, flash, render_template, redirect, url_for, request, session, jsonify, make_response
from flask_login import LoginManager, login_user, logout_user, login_required
from psycopg2 import IntegrityError
import requests

import utils.utils
from config import GITHUB_USERNAME, GITHUB_REPO, GITHUB_TOKEN
from models.usuario import Acceso, Usuario, Roles, Disco, Categorizacion, Categoria
from services.discos_service import DiscoService
from services.git_hub_service import GitHubService
from services.imgbb_service import subir_imagen
from utils.bd_utils import probar_connecion
from utils.utils import RegistroActividades, ValidadorUsuario
from utils.utils import RestriccionUsuarios

app = Flask(__name__)

# Establecer el atributo SameSite para las cookies de sesión
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True  # Asegúrate de utilizar HTTPS

# Configura el LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Crear una instancia del servicio de GitHub
github_service = GitHubService(GITHUB_USERNAME, GITHUB_REPO, GITHUB_TOKEN)
restriccion_usuarios = RestriccionUsuarios()

app.config.from_pyfile('config.py')


# # Middleware para verificar la página abierta
# @app.before_request
# def verificar_pagina_abierta():
#     ruta_actual = request.endpoint
#     if ruta_actual and ruta_actual != 'static':
#         if ruta_actual in session:
#             # El usuario ya tiene abierta la página, redirigir a la página actual
#             return redirect("ACCESS DENIED", code=200)
#         # Marcar la página actual como abierta en la sesión
#         session[ruta_actual] = True


@app.context_processor
def utility_processor():
    print(utils.utils.RegistroActividades.saludar("Gustavo"))
    fecha_actual = datetime.date.today()
    return {'fecha_actual': fecha_actual}


@app.route('/upload', methods=['POST'])
def upload():
    nombre_disco = request.form["nombre_disco"]
    artista = request.form["artista"]
    anio_lanzamiento = request.form["anio_lanzamiento"]
    genero = request.form["genero"]
    formato = request.form["formato"]
    categoria = request.form["categorias"]

    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo.')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No se seleccionó ningún archivo.')
        return redirect(request.url)
    # se uriliza api imgbb
    image_url = subir_imagen(file)

    if image_url:
        nuevo_disco = DiscoService.guardar_disco(nombre_disco, artista, anio_lanzamiento, genero, formato, categoria,
                                                 image_url)
        flash(f'Imagen subida exitosamente. URL: {image_url}')
        flash(f'Se agrega disco exitosamente')

    return redirect(url_for('ingreso_disco'))


@app.route('/ingreso_disco')
@login_required
def ingreso_disco():
    categorias = Categoria.select()
    return render_template('disc/ingreso_disco.html', categorias=categorias)


@app.route('/tabla_discos')
@login_required
def tabla_discos():
    discos = Disco.select()
    for disco in discos:
        print(disco.nombre_disco)
        print(disco.url_imagen)
    return render_template('disc/tabla_discos.html', discos=discos)


@app.route('/table_user')
@login_required
@restriccion_usuarios.admin_required
def tabla_usuarios():
    usuarios = Usuario.select()
    roles = Roles.select()
    for role in roles:
        print(role.nombre_rol)
    return render_template('tabla_usuarios.html', usuarios=usuarios, roles=roles)


@app.route('/movimietos_usuario')
@login_required
@restriccion_usuarios.admin_required
def movimientos_usuarios():
    return render_template('registro_movimientos.html')

    # REVISAR SI QUEDA COMO ENDPOINT


@app.route('/movimientos_usuario_busqueda', methods=["GET", "POST"])
@login_required
@restriccion_usuarios.admin_required
def movimientos_usuarios_busqueda():
    # Obtener la página y per_page de los parámetros de la solicitud
    page = 1
    if request.method == 'POST':
        busqueda = request.form["busqueda"]
        criterio = request.form.get("criterio", '')

    else:
        print(request.args)
        busqueda = request.cookies.get('busqueda')
        criterio = request.cookies.get('criterio')
        page = max(int(request.args.get('pagina_actual', 1)), 1)

    movimientos = RegistroActividades.buscar_registros(busqueda, criterio, page, 10)

    # Desempaquetar la respuesta para pasarla al render_template
    registros = movimientos['registros']
    total_registros = movimientos['total_registros']
    total_paginas = movimientos['total_paginas']
    pagina_actual = movimientos['pagina_actual']

    # Calcular si hay una página siguiente
    has_next = pagina_actual < total_paginas
    response = make_response(
        render_template('registro_movimientos.html', movimientos=registros, total_registros=total_registros,
                        total_paginas=total_paginas, pagina_actual=pagina_actual, has_next=has_next))
    response.set_cookie('busqueda', busqueda)
    response.set_cookie('criterio', criterio)
    return response


# Función para cargar un usuario por ID
@login_manager.user_loader
def load_user(user_id):
    try:
        return Usuario.get(Usuario.id == user_id)
    except Usuario.DoesNotExist:
        return None


# Ruta para el inicio de sesión


@app.route("/login", methods=["GET", "POST"])
def login():
    current_page = 'index'

    try:
        print(probar_connecion())  # Supongo que 'probar_connecion()' maneja la conexión a la base de datos

        if request.method == "POST":
            username = request.form["username"].strip()
            password = request.form["password"].strip()

            user = Usuario.get_or_none(
                (Usuario.nombre_usuario == username) & (Usuario.contrasena == password))

            if user:
                login_user(user)
                session['id'] = user.id
                session['logged'] = True
                session['user'] = username
                session['tipo'] = user.tipo_usuario
                current_page = ''
                return render_template('panel.html', current_page=current_page)

        flash("Error al iniciar sesión. Verifica tus credenciales e inténtalo de nuevo.", "error")
    except Exception as e:
        flash(f"Error de conexión a la base de datos: {str(e)}", "error")

    return render_template("index.html", current_page=current_page)


# Ruta para cerrar sesión
@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/usuario_cliente", methods=['POST'])
def registrar_usuario_cliente():
    try:
        nombre = request.form["nombre"]
        if not ValidadorUsuario.validar_usuario(nombre):
            flash(
                'El nombre de usuario no es válido. Debe tener entre 3 y 20 caracteres y contener solo letras y '
                'números (sin espacios).',
                'error')
            return redirect(url_for('index'))
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]
        if not ValidadorUsuario.validar_contrasena(contrasena):
            # Si la contraseña no cumple con los criterios, el mensaje de error ya fue flash y ahora rediriges a la
            # página principal
            return redirect(url_for('index'))
        tipo_usuario = 'User'

        if not Usuario.select().where(
                (Usuario.nombre_usuario == nombre) | (Usuario.correo_electronico == correo)).exists():
            # Crear un nuevo usuario y acceso en la base de datos
            nuevo_usuario = Usuario.create(
                nombre_usuario=nombre,
                correo_electronico=correo,
                contrasena=contrasena,
                tipo_usuario=tipo_usuario
            )

            rol_id = Roles.select(Roles.rol_id).where(
                Roles.nombre_rol == tipo_usuario).scalar()

            nuevo_acceso = Acceso.create(
                usuario_id=nuevo_usuario,
                rol_id=int(rol_id)
            )

            flash('Registro exitoso', 'success')  # Flash success message
        else:
            # Flash error message for duplicate entry
            flash('Usuario o correo ya existen', 'error')
    except IntegrityError as e:
        flash('Error al registrar el usuario: {}'.format(str(e)),
              'error')  # Flash error message for integrity error

    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html', current_page='/')


@app.route('/panel')
@login_required
def panel():
    panel_title = "Dashboard de Usuario"
    panel_content = ("Bienvenido al panel de control. Aquí encontrarás información y opciones para administrar tu "
                     "cuenta de usuario.")
    return render_template('panel.html', panel_title=panel_title, panel_content=panel_content)


# Ruta para eliminar un elemento por su índice


@app.route('/delete/<int:index>', methods=['POST'])
@login_required
@restriccion_usuarios.admin_required
def delete_element(index):
    if request.method == 'POST':
        try:
            # Recupera los accesos asociados al usuario
            accesos_a_eliminar = Acceso.select().where(Acceso.usuario_id == index)

            # Elimina los accesos asociados
            for acceso in accesos_a_eliminar:
                acceso.delete_instance()

            # Ahora puedes eliminar el usuario
            usuario_a_eliminar = Usuario.get(Usuario.id == index)
            usuario_a_eliminar.delete_instance()

            # Registrar accion
            RegistroActividades.registrar_actividades(
                str(session['id']), "ELIMINAR", "SE ELIMINA USUARIO DEL SISTEMA: " + usuario_a_eliminar.nombre_usuario)
            flash("Usuario eliminado exitosamente", "success")

        except IntegrityError as e:
            # Manejar la excepción de integridad referencial
            print(f"Error de integridad referencial: {e}")

    return redirect(url_for('tabla_usuarios'))


# Crea una ruta "insertar" para agregar un nuevo usuario a la lista


@app.route('/insertar', methods=['POST'])
@login_required
@restriccion_usuarios.admin_required
def insertar_usuario():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]
        rol = request.form["roles"]
        id_rol, nombre_rol = rol.split('|')

        try:
            # Verificar si el usuario ya existe en la base de datos
            if not Usuario.select().where(
                    (Usuario.nombre_usuario == nombre) | (Usuario.correo_electronico == correo)).exists():
                # Crear un nuevo usuario y acceso en la base de datos
                nuevo_usuario = Usuario.create(
                    nombre_usuario=nombre,
                    correo_electronico=correo,
                    contrasena=contrasena,
                    tipo_usuario=nombre_rol
                )
                nuevo_acceso = Acceso.create(
                    usuario_id=nuevo_usuario,
                    rol_id=int(id_rol)
                )

                # Registrar acción
                RegistroActividades.registrar_actividades(
                    str(session['id']), "REGISTRO",
                    f"SE REGISTRA POR USUARIO: {session['user']} - SE HA CREADO UN NUEVO USUARIO: {nombre}"
                )
                flash("Usuario creado exitosamente", "success")
            else:
                flash("El usuario o correo electronico ya existe en la base de datos.", "error")
        except Exception as e:
            # Manejar otras excepciones si es necesario
            flash(f"Error al crear el usuario: {str(e)}", "error")

    return redirect(url_for('tabla_usuarios'))


@app.route('/updateData', methods=['POST'])
@login_required
@restriccion_usuarios.admin_required
def editar_datos():
    # Obtener los datos del cuerpo de la solicitud en formato JSON
    data = request.get_json()

    # Verifica si el ID del usuario está presente en los datos recibidos
    if 'user_id' not in data:
        # Respuesta de error
        return jsonify({'mensaje': 'Falta el ID del usuario'}), 400

    try:
        # Obtiene el objeto de rol basado en el nombre de rol proporcionado
        rol = Roles.get(Roles.nombre_rol == data['TipoUsuario'])

        # Define los nuevos valores para el usuario
        nuevos_valores = {
            'nombre_usuario': data['nombre'],
            'correo_electronico': data['correo'],
            'contrasena': data['Contrasena'],
            'tipo_usuario': data['TipoUsuario'],
            'fecha_actualizacion': datetime.date.today()
        }

        # Actualiza el usuario en la base de datos
        Usuario.update(**nuevos_valores).where(Usuario.id ==
                                               data['user_id']).execute()

        # Actualiza el rol en la tabla de Acceso
        Acceso.update(rol_id=rol.rol_id).where(
            Acceso.usuario_id == data['user_id']).execute()

        # Registra la actividad
        RegistroActividades.registrar_actividades(
            str(session['id']), "ACTUALIZAR",
            f"SE ACTUALIZA POR USUARIO: {session['user']} - SE HA ACTUALIZADO USUARIO: {data['nombre']}"
        )

        # Indicar al cliente que debe recargar la página
        response_data = {'mensaje': 'Datos guardados exitosamente', 'reload_page': True}
        flash("Usuario actualizado exitosamente", "success")

        # Devuelve una respuesta JSON con la indicación de recargar la página
        return jsonify(response_data)
    except Roles.DoesNotExist:
        # Devuelve un mensaje de error si no se encuentra el rol
        return jsonify({'mensaje': 'Rol no encontrado'}), 404
    except Usuario.DoesNotExist:
        # Devuelve un mensaje de error si no se encuentra el usuario con el ID dado
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404


if __name__ == '__main__':
    app.run()
