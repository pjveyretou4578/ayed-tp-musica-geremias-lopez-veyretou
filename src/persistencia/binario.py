"""Persistencia binaria del catálogo musical."""

import struct

from src.excepciones import ArchivoInvalidoError


# Registro de canción:
# id(4) + titulo(32) + artista(45) + album(35) +
# genero(20) + anio(2) + duracion(2) = 140 bytes
FORMATO = struct.Struct("<I 32s 45s 35s 20s 2H")

# Header:
# magia AYED(4) + tema(1) + cantidad(4) = 9 bytes
HEADER = struct.Struct("<4s 1s I")

# Tema M = Música
TEMA = b"M"


def _a_bytes(texto, ancho):
    datos = texto.encode("utf-8")

    if len(datos) > ancho:
        raise ArchivoInvalidoError(
            f"El texto '{texto}' supera el máximo de {ancho} bytes."
        )

    return datos.ljust(ancho, b"\x00")


def _a_texto(datos):
    return datos.rstrip(b"\x00").decode("utf-8")


def _item_a_tupla(cancion):
    return (
        cancion.id,
        _a_bytes(cancion.titulo, 32),
        _a_bytes(cancion.artista, 45),
        _a_bytes(cancion.album, 35),
        _a_bytes(cancion.genero, 20),
        cancion.anio,
        cancion.duracion_seg
    )


def _tupla_a_item(datos):
    from src.dominio.cancion import Cancion

    return Cancion(
        datos[0],
        _a_texto(datos[1]),
        _a_texto(datos[2]),
        _a_texto(datos[3]),
        _a_texto(datos[4]),
        datos[5],
        datos[6],
        None,
        None
    )


def guardar_binario(ruta, items):
    registros = []

    for cancion in items:
        datos = FORMATO.pack(*_item_a_tupla(cancion))
        registros.append(datos)

    with open(ruta, "wb") as archivo:
        archivo.write(
            HEADER.pack(b"AYED", TEMA, len(items))
        )

        for datos in registros:
            archivo.write(datos)


def cargar_binario(ruta):

    canciones = []

    with open(ruta, "rb") as archivo:

        cabecera = archivo.read(HEADER.size)

        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError(
                "Binario truncado: el header está incompleto."
            )

        magia, tema, cantidad = HEADER.unpack(cabecera)

        if magia != b"AYED":
            raise ArchivoInvalidoError(
                "Magia incorrecta: el archivo no pertenece a este TP."
            )

        if tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo binario no corresponde al tema Música."
            )

        for _ in range(cantidad):

            datos = archivo.read(FORMATO.size)

            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError(
                    "Binario truncado: faltan registros."
                )

            tupla = FORMATO.unpack(datos)
            cancion = _tupla_a_item(tupla)

            canciones.append(cancion)

    return canciones


def actualizar_registro(ruta, posicion, item):
    """Pisa un registro por posición. La posición comienza en 0."""

    if posicion < 0:
        raise ArchivoInvalidoError("La posición no puede ser negativa.")

    datos = FORMATO.pack(*_item_a_tupla(item))

    with open(ruta, "r+b") as archivo:

        encabezado = archivo.read(HEADER.size)

        if len(encabezado) != HEADER.size:
            raise ArchivoInvalidoError("Binario truncado: header incompleto.")

        magia, tema, cantidad = HEADER.unpack(encabezado)

        if magia != b"AYED":
            raise ArchivoInvalidoError("Magia incorrecta: el archivo no pertenece a este TP.")

        if tema != TEMA:
            raise ArchivoInvalidoError("Tema incorrecto en el archivo binario.")

        if posicion >= cantidad:
            raise ArchivoInvalidoError("La posición indicada no existe en el archivo binario.")

        posicion_byte = HEADER.size + posicion * FORMATO.size

        archivo.seek(0, 2)
        tamanio_archivo = archivo.tell()

        if posicion_byte + FORMATO.size > tamanio_archivo:
            raise ArchivoInvalidoError("Binario truncado: falta el registro indicado.")

        archivo.seek(posicion_byte)
        archivo.write(datos)