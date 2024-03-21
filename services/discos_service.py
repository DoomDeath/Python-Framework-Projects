from models.usuario import Disco, Categorizacion


class DiscoService:
    @staticmethod
    def guardar_disco(nombre_disco, artista, anio_lanzamiento, genero, formato, categoria, url_imagen):
        nuevo_disco = Disco.create(
            nombre_disco=nombre_disco,
            artista=artista,
            anio_lanzamiento=anio_lanzamiento,
            genero=genero,
            formato=formato,
            url_imagen=url_imagen
        )
        nueva_categorizacion = Categorizacion.create(
            disco=nuevo_disco,
            categoria=categoria
        )

        return nuevo_disco
