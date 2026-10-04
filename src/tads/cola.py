from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError


class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")

        dato = self._items._cabeza.dato

        self._items._cabeza = self._items._cabeza.siguiente
        self._items._tamanio -= 1

        return dato

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")

        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()

    def __iter__(self):
        for dato in self._items:
            yield dato