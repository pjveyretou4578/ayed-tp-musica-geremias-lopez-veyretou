from pathlib import Path
from datetime import datetime
from src.excepciones import ArchivoInvalidoError
from src.dominio.cancion import Cancion

def cargar_txt(ruta):
    """Carga un archivo de texto separado por comas y devuelve una lista de diccionarios."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    filas = []

    with ruta.open("r", encoding="utf-8") as archivo:

        encabezados = archivo.readline().strip().split(",")

        for linea in archivo:

            linea = linea.strip()

            if not linea:
                continue

            valores = linea.split(",")

            if len(valores) != len(encabezados):
                raise ArchivoInvalidoError(
                    f"Línea con {len(valores)} campos; "
                    f"se esperaban {len(encabezados)}."
                )

            fila = dict(zip(encabezados, valores))
            filas.append(fila)

    return filas

def cargar_canciones(ruta):
    filas = cargar_txt(ruta)

    canciones = []
    ids_usados = []
    anio_actual = datetime.now().year

    for fila in filas:
        try:
            id_cancion = int(fila["id"])
            anio = int(fila["anio"])
            duracion = int(fila["duracion_seg"])
        except ValueError:
            raise ArchivoInvalidoError(
                "ID, año y duración deben contener valores numéricos."
            )

        if id_cancion in ids_usados:
            raise ArchivoInvalidoError(
                f"ID duplicado en canciones.txt: {id_cancion}"
            )



        if anio < 1 or anio > anio_actual:
            raise ArchivoInvalidoError(
                f"Año fuera de rango en canciones.txt: {anio}"
            )

        if duracion < 1 or duracion > 65535:
            raise ArchivoInvalidoError(
                f"Duración fuera de rango en canciones.txt: {duracion}"
            )

        ids_usados.append(id_cancion)

        cancion = Cancion(
            id_cancion,
            fila["titulo"],
            fila["artista"],
            fila["album"],
            fila["genero"],
            anio,
            duracion,
            None
        )

        canciones.append(cancion)

    return canciones

def cargar_versiones(ruta, canciones):
    filas = cargar_txt(ruta)

    for fila in filas:
        cancion_id = int(fila["cancion_id"])
        version_de_id = int(fila["version_de_id"])

        for cancion in canciones:
            if cancion.id == cancion_id:
                cancion.version_de = version_de_id
                cancion.tipo_version = fila["tipo"]
                break

    return canciones

def canciones_a_filas(canciones):
    filas = []

    for cancion in canciones:
        fila = {
            "id": cancion.id,
            "titulo": cancion.titulo,
            "artista": cancion.artista,
            "album": cancion.album,
            "genero": cancion.genero,
            "anio": cancion.anio,
            "duracion_seg": cancion.duracion_seg
        }

        filas.append(fila)

    return filas

def versiones_a_filas(canciones):
    filas = []

    for cancion in canciones:
        if cancion.version_de is not None:
            fila = {
                "cancion_id": cancion.id,
                "version_de_id": cancion.version_de,
                "tipo": cancion.tipo_version
            }

            filas.append(fila)

    return filas

def guardar_txt(ruta, filas, encabezados):
    ruta = Path(ruta)

    with ruta.open("w", encoding="utf-8") as archivo:
        archivo.write(",".join(encabezados) + "\n")

        for fila in filas:
            valores = []

            for encabezado in encabezados:
                valores.append(str(fila[encabezado]))

            archivo.write(",".join(valores) + "\n")

def guardar_catalogo(canciones):

    if not canciones:
        raise ArchivoInvalidoError("No se puede guardar un catálogo vacío.")

    encabezados_canciones = [
        "id",
        "titulo",
        "artista",
        "album",
        "genero",
        "anio",
        "duracion_seg"
    ]

    encabezados_versiones = [
        "cancion_id",
        "version_de_id",
        "tipo"
    ]

    filas_canciones = canciones_a_filas(canciones)
    filas_versiones = versiones_a_filas(canciones)

    guardar_txt(
        "data/canciones.txt",
        filas_canciones,
        encabezados_canciones
    )

    guardar_txt(
        "data/versiones.txt",
        filas_versiones,
        encabezados_versiones
)