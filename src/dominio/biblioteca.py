class Biblioteca:

    def __init__(self, canciones):
        self.canciones = canciones


    def listar_catalogo(self):

        for cancion in self.canciones:
            print(
                cancion.id,
                "-",
                cancion.titulo,
                "-",
                cancion.artista
            )


    def buscar_por_id(self, id_cancion):

        for cancion in self.canciones:

            if cancion.id == id_cancion:
                return cancion

        return None


    def versiones_directas(self, id_cancion):

        resultado = []

        for cancion in self.canciones:

            if cancion.version_de == id_cancion:
                resultado.append(cancion.id)

        return resultado