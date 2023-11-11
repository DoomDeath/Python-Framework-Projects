from models.usuario import RegistroDeActividades


class RegistroActividades():

    def registrar_actividades(id, accion, descripcion):

        RegistroDeActividades.create(
            usuario=int(id),
            accion=accion,
            descripcion=descripcion


        )
