from datetime import datetime

from peewee import Model, PostgresqlDatabase, CharField, DateField, ForeignKeyField, BooleanField, IntegerField, \
    DateTimeField, Column, PrimaryKeyField
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

# Configura la conexión a la base de datos PostgreSQL
db = PostgresqlDatabase('dbdi', user='dbdi_user', password='hfB3VFoAb5Q2GVW1jQgPYiA6xuqALu8f',
                        host='dpg-cl6165c72pts73fqdbug-a.oregon-postgres.render.com', port=5432)


# Define el modelo de Usuario
class Usuarios(UserMixin, Model):
    id = PrimaryKeyField()
    nombre_usuario = CharField()
    correo_electronico = CharField()
    contrasena = CharField()
    fecha_registro = DateField()
    fecha_actualizacion = DateField()

    class Meta:
        database = db
        db_table = 'usuarios'  # Nombre de la tabla en la base de datos


# Define el modelo de Disco
class Disco(Model):
    nombre_disco = CharField()
    artista = CharField()
    anio_lanzamiento = IntegerField()
    genero = CharField()

    # Agrega otros campos relacionados con la información del disco aquí

    class Meta:
        database = db


# Define el modelo de Categoría
class Categoria(Model):
    nombre_categoria = CharField()
    descripcion_categoria = CharField()

    # Agrega otros campos relacionados con la información de la categoría aquí

    class Meta:
        database = db


# Define el modelo de Categorización (relación entre Discos y Categorías)
class Categorizacion(Model):
    disco = ForeignKeyField(Disco)
    categoria = ForeignKeyField(Categoria)

    class Meta:
        database = db


# Define el modelo de Acceso
class Acceso(Model):
    usuario = ForeignKeyField(Usuarios)
    permisos = CharField()  # Puedes definir otros tipos de campos para gestionar permisos

    class Meta:
        database = db


# Define el modelo de Registro de Actividades
class RegistroActividad(Model):
    usuario = ForeignKeyField(Usuarios)
    accion = CharField()
    fecha_hora = DateTimeField()
    descripcion = CharField()

    # Puedes personalizar los campos según tus necesidades

    class Meta:
        database = db
