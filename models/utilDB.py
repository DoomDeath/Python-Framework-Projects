from models.usuarios import database


def probar_connecion():
    try:
        # Intenta conectar a la base de datos
        database.connect()
        resultado = "Conexión exitosa a la base de datos PostgreSQL."
    except Exception as e:
        resultado = f"Error al conectar a la base de datos: {str(e)}"
    finally:
        # Asegúrate de cerrar la conexión
        if not database.is_closed():
            database.close()
    
    return resultado