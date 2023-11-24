import base64

import requests
from flask import flash


class GitHubService:
    def __init__(self, username, repo, token):
        self.username = username
        self.repo = repo
        self.token = token

    def upload_image(self, file):
        try:
            # Configura los parámetros para subir la imagen a GitHub
            url = f'https://api.github.com/repos/{self.username}/{self.repo}/contents/{file.filename}'
            headers = {'Authorization': f'token {self.token}'}
            data = {
                'message': 'Añadir imagen',
                'content': base64.b64encode(file.read()).decode('utf-8')
            }
            response = requests.put(url, headers=headers, json=data)

            if response.status_code == 201:
                # Obtiene la URL de la imagen subida
                image_url = response.json()['content']['html_url']
                return image_url
            else:
                flash(f'Error al subir la imagen. Respuesta de GitHub: {response.text}')
        except Exception as e:
            flash(f'Error al subir la imagen. Excepción: {str(e)}')

        return None
