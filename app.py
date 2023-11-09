from flask import request, render_template, session, redirect, url_for
import datetime

from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

from models.usuarios import User, database
from models.utilDB import probar_connecion

app = Flask(__name__)

app.secret_key = '12345678'  # Cambia esto a una clave secreta segura

# Configura el LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@app.context_processor
def utility_processor():
    fecha_actual = datetime.date.today()
    return {'fecha_actual': fecha_actual}


# Simulación de una base de datos de usuarios
usuarios2 = {
    "1": {"id": "1", "username": "Gustavo", "password": "1234"}}

# Datos ficticios para la tabla de usuarios
usuarios = [
    {"id": 1, "nombre": "John Doe", "correo": "johndoe@example.com", "edad": 30},
    {"id": 2, "nombre": "Jane Smith", "correo": "janesmith@example.com", "edad": 25},
    {"id": 3, "nombre": "Robert Johnson",
     "correo": "robert@example.com", "edad": 35},
    {"id": 4, "nombre": "Jane Smith", "correo": "janesmith@example.com", "edad": 25},
    {"id": 5, "nombre": "Jane Smith", "correo": "janesmith@example.com", "edad": 25},
    {"id": 6, "nombre": "Jane Smith", "correo": "janesmith@example.com", "edad": 25},
    {"id": 7, "nombre": "Jane Smith", "correo": "janesmith@example.com", "edad": 25},
    {"id": 8, "nombre": "Jane Smith", "correo": "janesmith@example.com", "edad": 25}

]


@app.route('/table_user')
@login_required
def tabla_usuarios():
    return render_template('tabla_usuarios.html', usuarios=usuarios)


# Función para cargar un usuario por ID
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.get(User.id == user_id)
    except Usuario.DoesNotExist:
        return None


# Ruta para el inicio de sesión


@app.route("/login", methods=["GET", "POST"])
def login():
    current_page = 'index'

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        user = User.get_or_none(
            (User.nombre_usuario == username) & (User.contrasena == password))

        if user:
            login_user(user)
            session['logged'] = True
            session['user'] = username
            current_page = ''
            return render_template('panel.html', current_page=current_page)

    return render_template("index.html", current_page=current_page)


# Ruta para cerrar sesión
@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


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
def delete_element(index):
    if request.method == 'POST':
        try:
            # Eliminar el elemento por su índice
            del usuarios[index]
        except IndexError:
            pass  # Manejar el caso en el que el índice no existe

        return redirect(url_for('tabla_usuarios'))


# Crea una ruta "insertar" para agregar un nuevo usuario a la lista


@app.route('/insertar', methods=['POST'])
# Debes reemplazar esto con tu decorador de autenticación real
@login_required
def insertar_elemento():
    if request.method == 'POST':
        # Obtén los datos del nuevo usuario desde la solicitud
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        edad = request.form["edad"]
        # Crear un nuevo diccionario de usuario
        nuevo_usuario = {
            "id": len(usuarios) + 1,
            "nombre": nombre,
            "correo": correo,
            "edad": edad
        }

        if nuevo_usuario:
            # Agrega el nuevo usuario a la lista
            usuarios.append(nuevo_usuario)

    return redirect(url_for('tabla_usuarios'))


@app.route('/updateData', methods=['POST'])
@login_required
def editar_datos():
    # Obtener los datos del cuerpo de la solicitud en formato JSON
    data = request.get_json()

    # Verifica si el ID del usuario está presente en los datos recibidos
    if 'user_id' not in data:
        # Respuesta de error
        return jsonify({'mensaje': 'Falta el ID del usuario'}), 400

    user_id = data['user_id']

    # Busca el usuario por su ID en la lista de usuarios
    for usuario in usuarios:
        if usuario['id'] == int(user_id):
            # Actualiza los campos si están presentes en los datos
            if 'nombre' in data:
                usuario['nombre'] = data['nombre']
            if 'correo' in data:
                usuario['correo'] = data['correo']
            if 'edad' in data:
                usuario['edad'] = data['edad']

            return jsonify({'mensaje': 'Datos guardados exitosamente'})

    # Devuelve un mensaje de error si no se encuentra el usuario con el ID dado
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404


if __name__ == '__main__':
    app.run()
