from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError


class Playlist:

    def __init__(self, nombre, maximo):
        self.nombre = nombre
        self.canciones = ListaEnlazada()
        self.maximo = maximo

    def agregar_cancion(self, cancion):

        if self.canciones.tamanio() >= self.maximo:
            raise ColeccionLlenaError("La playlist esta llena")

        self.canciones.insertar_al_final(cancion)

    def duracion_total(self):

        total = 0

        for cancion in self.canciones:
            total = total + cancion.duracion_seg

        return total

    def listar(self):

        for cancion in self.canciones:
            print(
                cancion.id,
                "-",
                cancion.titulo,
                "-",
                cancion.artista
            )
    def eliminar_cancion(self, cancion):
        self.canciones.eliminar(cancion)

    def mover_al_inicio(self, cancion):
        self.canciones.eliminar(cancion)
        self.canciones.insertar_al_inicio(cancion)

    def mover_al_final(self, cancion):
        self.canciones.eliminar(cancion)
        self.canciones.insertar_al_final(cancion)

    def __iter__(self):
        for cancion in self.canciones:
            yield cancion