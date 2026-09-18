class Playlist:

    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):

        total = 0

        for cancion in self.canciones:
            total = total + cancion.duracion_seg

        return total