from peewee import Model, PostgresqlDatabase, CharField, DateField, ForeignKeyField, BooleanField
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

# Configura la conexión a la base de datos PostgreSQL
database = PostgresqlDatabase('dbdi', user='dbdi_user', password='hfB3VFoAb5Q2GVW1jQgPYiA6xuqALu8f',
                              host='dpg-cl6165c72pts73fqdbug-a.oregon-postgres.render.com', port=5432)




class User(UserMixin, Model):
    nombre_usuario = CharField()
    correo_electronico = CharField(unique=True)
    contrasena = CharField()
    fecha_registro = DateField()

    class Meta:
        database = database
        db_table = 'usuarios'  # Nombre de la tabla en la base de datos


# Define un modelo para perfiles de seguridad
class PerfilSeguridad(Model):
    nombre_perfil = CharField()
    descripcion = CharField()

    class Meta:
        database = database


# Define un modelo para asignación de perfiles a usuarios
class AsignacionPerfilUsuario(Model):
    usuario = ForeignKeyField(User, backref='perfiles')
    perfil = ForeignKeyField(PerfilSeguridad, backref='usuarios')

    class Meta:
        database = database
