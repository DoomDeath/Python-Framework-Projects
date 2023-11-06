import datetime

from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)

app.secret_key = '12345678'  # Cambia esto a una clave secreta segura

# Configura el LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


# Modelo de usuario de ejemplo
class User(UserMixin):
    def __init__(self, id):
        self.id = id


@app.context_processor
def utility_processor():
    fecha_actual = datetime.date.today()
    return {'fecha_actual': fecha_actual}


# Simulación de una base de datos de usuarios
usuarios2 = {"1": {"id": "1", "username": "Gustavo Burgos", "password": "contrasena6"}}


# Función para cargar un usuario por ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Ruta para el inicio de sesión
@app.route("/login", methods=["GET", "POST"])
#login_required
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        user_final = None
        for user in usuarios2.values():
            if user["username"] == username and user["password"] == password:
                user_final = user
                break

        if user_final:
            user_obj = User(user_final["id"])
            print(user_final["id"])
            isLogged = login_user(user_obj)

            return render_template('panel.html', isLogged=isLogged, user_final=user_final)

    return render_template("index.html")


# Ruta para cerrar sesión
@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/table_user')
def table_user():
    return render_template('tabla_usuarios.html', base_template='base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acerca')
def acerca():
    current_page = 'acerca'
    return render_template('acerca.html', current_page=current_page)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


# @app.route('/panel')
@login_required
def panel():
    panel_title = "Dashboard de Usuario"
    panel_content = ("Bienvenido al panel de control. Aquí encontrarás información y opciones para administrar tu "
                     "cuenta de usuario.")
    return render_template('panel.html', panel_title=panel_title, panel_content=panel_content)


# @app.context_processor
# def inject_data():
# data = {
# 'username': 'UsuarioEjemplo',  # Puedes obtener este valor de donde desees
# 'notifications': 3  # Puedes obtener este valor de donde desees
# }
# return data


if __name__ == '__main__':
    app.run()
