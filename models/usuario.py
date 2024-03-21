from flask_login import UserMixin
from peewee import Model, PostgresqlDatabase, CharField, DateField, ForeignKeyField, IntegerField, \
    DateTimeField, SQL, TextField

# Configura la conexión a la base de datos PostgreSQL
db = PostgresqlDatabase('dbdi', user='dbdi_user', password='hfB3VFoAb5Q2GVW1jQgPYiA6xuqALu8f',
                        host='dpg-cl6165c72pts73fqdbug-a.oregon-postgres.render.com', port=5432)


class Usuario(UserMixin, Model):
    id = IntegerField(primary_key=True, db_column='usuario_id')
    nombre_usuario = CharField(max_length=255)
    correo_electronico = CharField(max_length=255)
    contrasena = CharField(max_length=255)
    tipo_usuario = CharField(max_length=50)
    fecha_registro = DateField(constraints=[SQL('DEFAULT CURRENT_DATE')])
    fecha_actualizacion = DateField()

    class Meta:
        database = db
        db_table = 'usuarios'  # Nombre de la tabla en la base de datos


# Definición del modelo Disco
class Disco(Model):
    disco_id = IntegerField(primary_key=True)
    nombre_disco = CharField(max_length=255)
    artista = CharField(max_length=255, null=True)
    anio_lanzamiento = IntegerField(null=True)
    genero = CharField(max_length=100, null=True)
    formato = CharField(max_length=100, null=True)
    fecha_registro = DateField(constraints=[SQL('DEFAULT CURRENT_DATE')])
    fecha_actualizacion = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    url_imagen = CharField(max_length=255, null=True)  # Nueva columna

    class Meta:
        database = db
        db_table = 'discos'


# Definición del modelo Categoría
class Categoria(Model):
    categoria_id = IntegerField(primary_key=True)
    nombre_categoria = CharField(max_length=100)
    descripcion_categoria = TextField(null=True)

    class Meta:
        database = db
        db_table = 'categorias'


# Definición del modelo Categorización
class Categorizacion(Model):
    categorizacion_id = IntegerField(primary_key=True)
    disco = ForeignKeyField(Disco, backref='categorias')
    categoria = ForeignKeyField(Categoria, backref='discos')

    class Meta:
        database = db


# Definición del modelo Rol
class Roles(Model):
    rol_id = IntegerField(primary_key=True)
    nombre_rol = CharField(max_length=50)
    descripcion = CharField(max_length=100, null=True)

    class Meta:
        database = db


# Definición del modelo Acceso
class Acceso(Model):
    acceso_id = IntegerField(primary_key=True)
    usuario = ForeignKeyField(Usuario, backref='roles')
    rol = ForeignKeyField(Roles, backref='usuarios')

    class Meta:
        database = db
        db_table = 'accesos'


# Definición del modelo Registro_de_Actividades
class RegistroDeActividades(Model):
    registro_id = IntegerField(primary_key=True)
    usuario = IntegerField(Usuario, db_column='usuario_id')
    accion = CharField(max_length=255)
    fecha_hora = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    descripcion = TextField(null=True)

    class Meta:
        database = db
        db_table = 'registro_de_actividades'
