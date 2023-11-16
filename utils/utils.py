from models.registro_movimientos import RegistroDTO
from models.usuario import RegistroDeActividades, db


class RegistroActividades():

    def registrar_actividades(id, accion, descripcion):
        RegistroActividades.create(
            usuario=int(id),
            accion=accion,
            descripcion=descripcion
        )

    def buscar_registros(termino, columna_busqueda):
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
