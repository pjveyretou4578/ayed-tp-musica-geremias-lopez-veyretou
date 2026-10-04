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


    def listar_catalogo_paginado(self):
    # Se usa en la opcion 6 para elegir canciones para la playlist

        contador = 0

        for cancion in self.canciones:
            print(
                cancion.id,
                "-",
                cancion.titulo,
                "-",
                cancion.artista
            )

            contador += 1

            if contador % 10 == 0:
                opcion = input(
                    "Enter para ver mas canciones o q para elegir: "
                ).strip().lower()

                if opcion == "q":
                    return


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

    def listar_catalogo_dos_columnas(self):

        contador = 0

        for cancion in self.canciones:

            repetido = False

            for otra in self.canciones:
                if otra.id != cancion.id and otra.titulo == cancion.titulo:
                    repetido = True

            if repetido:
                texto = f"{cancion.id} - {cancion.titulo} - {cancion.artista}"
            else:
                texto = f"{cancion.id} - {cancion.titulo}"

            if len(texto) > 36:
                texto = texto[:33] + "..."

            print(f"{texto:<40}", end="")

            contador += 1

            if contador % 2 == 0:
                print()

        if contador % 2 != 0:
            print()