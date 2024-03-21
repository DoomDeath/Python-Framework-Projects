import base64
from flask import flash
import requests

from config import IMG_API_KEY


def subir_imagen(imagen):
    try:
        # Configura la URL de la API de ImgBB
        url = "https://api.imgbb.com/1/upload"

        # Configura los datos del formulario
        payload = {
            'key': IMG_API_KEY,
            'image': base64.b64encode(imagen.read()).decode('utf-8')
        }

        # Realiza la solicitud POST a la API de ImgBB
        response = requests.post(url, data=payload)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            # Retorna la URL de la imagen cargada desde la respuesta JSON
            return response.json()['data']['url']
        else:
            flash(f'Error al subir la imagen. Respuesta de GitHub: {response.text}')
            response.raise_for_status()
    except Exception as e:
        flash(f'Error al subir la imagen. Excepción: {str(e)}')

    return None
