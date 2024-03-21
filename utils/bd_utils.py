from models.usuario import db


def probar_connecion():
    try:
        # Intenta conectar a la base de datos
        db.connect()
        resultado = "Conexión exitosa a la base de datos PostgreSQL."
    except Exception as e:
        resultado = f"Error al conectar a la base de datos: {str(e)}"
    finally:
        # Asegúrate de cerrar la conexión
        if not db.is_closed():
            db.close()

    return resultado
