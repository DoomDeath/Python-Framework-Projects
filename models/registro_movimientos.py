class RegistroDTO:
    def __init__(self, registro_id, usuario_id, nombre_usuario, accion, fecha_hora, descripcion):
        self.registro_id = registro_id
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.accion = accion
        self.fecha_hora = fecha_hora
        self.descripcion = descripcion
