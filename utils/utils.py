from models.registro_movimientos import RegistroDTO
from models.usuario import RegistroDeActividades, db


class RegistroActividades():

    def registrar_actividades(id, accion, descripcion):

        RegistroDeActividades.create(
            usuario=int(id),
            accion=accion,
            descripcion=descripcion


        )

    def buscar_registros(termino, columna_busqueda):

        query = f"SELECT * FROM buscar_registros('{termino}', '{columna_busqueda}')"

        # Ejecutar la consulta y obtener los resultados
        resultados = list(db.execute_sql(query))
        print(resultados)

        registros_peewee = [RegistroDTO(
            registro_id=resultado[0],
            usuario_id=resultado[1],
            nombre_usuario=resultado[2],
            accion=resultado[3],
            fecha_hora=resultado[4],
            descripcion=resultado[5]
        ) for resultado in resultados]

        return registros_peewee


# # Función para buscar registros
#     def buscar_registros(termino, columna_busqueda):
#         # Uso de Peewee para ejecutar la consulta
#         query = (RegistroDeActividades
#                 .select()
#                 .where(getattr(RegistroDeActividades, columna_busqueda).contains(termino)))
#
#         # Ejecutar la consulta y obtener los resultados
#         resultados = list(query.execute())
#
#         return resultados
#
#     def buscar_nombre_usuario(id):




