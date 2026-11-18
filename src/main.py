from src.config import TEMA
from src.persistencia.texto import cargar_canciones, cargar_versiones, guardar_catalogo
from src.persistencia.binario import guardar_binario, cargar_binario, actualizar_registro
from src.dominio.versiones import mostrar_cadena_versiones
from src.dominio.biblioteca import Biblioteca
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError, ArchivoInvalidoError
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.dominio.cancion import Cancion
from pathlib import Path
from datetime import datetime

error_inicio = None

try:
    catalogo = cargar_canciones("data/canciones.txt")
    cargar_versiones("data/versiones.txt", catalogo)

except ArchivoInvalidoError as error:
    error_inicio = error
    catalogo = []

biblioteca = Biblioteca(catalogo)

playlist = Playlist("Mi playlist", 5)
historial = Pila()
cola_reproduccion = Cola()
cancion_actual = None

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def obtener_titulo(cancion):
    return cancion.titulo.casefold()


def obtener_artista(cancion):
    return cancion.artista.casefold()


def obtener_duracion(cancion):
    return cancion.duracion_seg


def ver_detalle():

    print()
    print("--- Detalle de canción ---")

    entrada = input("Ingrese ID de la canción: ").strip()

    if not entrada.isdigit():
        print("El ID debe ser numérico.")
        return

    id_cancion = int(entrada)

    cancion = biblioteca.buscar_por_id(id_cancion)

    if cancion is None:
        print("Canción no encontrada.")
        return

    print()
    print("ID:", cancion.id)
    print("Título:", cancion.titulo)
    print("Artista:", cancion.artista)
    print("Álbum:", cancion.album)
    print("Género:", cancion.genero)
    print("Año:", cancion.anio)
    print("Duración:", cancion.duracion_seg, "segundos")
    print("Versión de:", cancion.version_de)
    print("Tipo de versión:", cancion.tipo_version)

def mostrar_menu():

    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Mostrar versiones derivadas")
    print("6. Playlist")
    print("7. Historial (pila)")
    print("8. Reproducción")
    print("9. Guardar / cargar / gestionar datos")
    print("0. Salir")


def menu_playlist():

    while True:

        print("--- Playlist ---")
        print("1. Agregar cancion")
        print("2. Eliminar cancion")
        print("3. Cambiar orden")
        print("4. Listar playlist")
        print("0. Volver")

        print()
        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":

            print()
            biblioteca.listar_catalogo_dos_columnas()

            while True:

                print()

                entrada = input(
                    "Ingrese ID de la cancion (0 para terminar): "
                ).strip()

                if entrada == "0":
                    break

                if not entrada.isdigit():
                    print("Debe ingresar un numero.")
                    continue

                id_cancion = int(entrada)

                cancion = biblioteca.buscar_por_id(id_cancion)

                if cancion is None:
                    print("Cancion no encontrada.")

                else:
                    try:
                        playlist.agregar_cancion(cancion)
                        print("Cancion agregada.")

                    except ColeccionLlenaError as e:
                        print(e)
                        break

        elif opcion == "2":

            print()
            playlist.listar()

            print()
            entrada = input(
                "Ingrese ID de la cancion a eliminar: "
            ).strip()

            if not entrada.isdigit():
                print("Debe ingresar un numero.")
                continue

            id_cancion = int(entrada)

            cancion = biblioteca.buscar_por_id(id_cancion)

            if cancion is None:
                print("Cancion no encontrada.")

            else:
                playlist.eliminar_cancion(cancion)
                print("Cancion eliminada.")

        elif opcion == "3":

            while True:

                print()
                print("--- Cambiar orden de la playlist ---")
                playlist.listar()

                print()
                print("1. Mover canción al inicio")
                print("2. Mover canción al final")
                print("0. Volver")

                print()
                opcion_orden = input("Ingrese una opcion: ").strip()

                if opcion_orden == "0":
                    break

                if opcion_orden != "1" and opcion_orden != "2":
                    print("Opcion invalida.")
                    continue

                entrada = input("Ingrese ID de la canción: ").strip()

                if not entrada.isdigit():
                    print("El ID debe ser numérico.")
                    continue

                id_cancion = int(entrada)

                cancion_en_playlist = None

                for cancion in playlist:
                    if cancion.id == id_cancion:
                        cancion_en_playlist = cancion
                        break

                if cancion_en_playlist is None:
                    print("La canción no está en la playlist.")
                    continue

                if opcion_orden == "1":
                    playlist.mover_al_inicio(cancion_en_playlist)
                    print("Canción movida al inicio.")

                else:
                    playlist.mover_al_final(cancion_en_playlist)
                    print("Canción movida al final.")

                print()
                print("Playlist actualizada:")
                playlist.listar()

        elif opcion == "4":

            print()
            playlist.listar()

        else:
            print("Opcion invalida.")


def menu_historial():

    while True:

        print()
        print("1. Sacar ultima reproduccion")
        print("2. Ver ultima reproduccion")
        print("3. Ver historial completo")
        print("0. Volver")
        print()
        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "0":
            break


        elif opcion == "1":

            try:
                cancion = historial.desapilar()

                print(
                    "Se quito del historial:",
                    cancion.titulo,
                    "-",
                    cancion.artista
                )

            except PilaVaciaError as e:
                print(e)

        elif opcion == "2":

            try:
                cancion = historial.ver_tope()

                print(
                    "Ultima reproduccion:",
                    cancion.titulo,
                    "-",
                    cancion.artista
                )

            except PilaVaciaError as e:
                print(e)

        

            print()
            print("Historial de reproduccion:")

            for cancion in historial:
                print(
                    cancion.titulo,
                    "-",
                    cancion.artista
                )
        else:
            print("Opcion invalida.")


def menu_reproduccion():

    global cancion_actual

    while True:

        print()
        print("--- Reproduccion ---")
        print("1. Reproducir playlist")
        print("2. Siguiente cancion (Next)")
        print("3. Ver cancion actual")
        print("4. Ver canciones pendientes")
        print("0. Volver")

        print()
        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":

            if cancion_actual is not None:

                print(
                    "Ya hay una cancion en reproduccion:",
                    cancion_actual.titulo,
                    "-",
                    cancion_actual.artista
                )

            else:

                # Si la cola esta vacia, cargamos la playlist
                if cola_reproduccion.esta_vacia():

                    for cancion in playlist:
                        cola_reproduccion.encolar(cancion)

                # Si sigue vacia, la playlist no tenia canciones
                if cola_reproduccion.esta_vacia():

                    print("La playlist esta vacia.")

                else:

                    cancion_actual = cola_reproduccion.desencolar()

                    print(
                        "Reproduccion iniciada:",
                        cancion_actual.titulo,
                        "-",
                        cancion_actual.artista
                    )

        elif opcion == "2":

            if cancion_actual is None:

                print("No hay una cancion en reproduccion.")

            else:

                # La cancion que estaba sonando pasa al historial
                historial.apilar(cancion_actual)

                try:
                    cancion_actual = cola_reproduccion.desencolar()

                    print(
                        "Reproduciendo:",
                        cancion_actual.titulo,
                        "-",
                        cancion_actual.artista
                    )

                except ColaVaciaError as e:
                    cancion_actual = None
                    print(e)

        elif opcion == "3":

            if cancion_actual is None:

                print("No hay una cancion en reproduccion.")

            else:

                print(
                    "Cancion actual:",
                    cancion_actual.titulo,
                    "-",
                    cancion_actual.artista
                )

        elif opcion == "4":

            print()
            print("Canciones pendientes:")

            if cola_reproduccion.esta_vacia():

                print("No hay canciones pendientes.")

            else:

                for cancion in cola_reproduccion:

                    print(
                        cancion.titulo,
                        "-",
                        cancion.artista
                    )

        else:

            print("Opcion invalida.")


def menu_ordenar():

    print()
    print("--- Ordenar catálogo ---")
    print("1. Selección")
    print("2. Inserción")
    print("0. Volver")

    print()
    opcion_algoritmo = input("Ingrese una opcion: ").strip()

    if opcion_algoritmo == "0":
        return

    print()
    print("--- Criterio de ordenamiento ---")
    print("1. Título")
    print("2. Duración")
    print("3. Artista")
    print("0. Volver")

    print()
    opcion_criterio = input("Ingrese una opcion: ").strip()

    if opcion_criterio == "0":
        return

    if opcion_criterio == "1":
        criterio = obtener_titulo
        nombre_criterio = "título"

    elif opcion_criterio == "2":
        criterio = obtener_duracion
        nombre_criterio = "duración"

    elif opcion_criterio == "3":
        criterio = obtener_artista
        nombre_criterio = "artista"

    else:
        print("Opcion invalida.")
        return

    if opcion_algoritmo == "1":
        resultado = ordenar_seleccion(catalogo, criterio)
        nombre_algoritmo = "selección"

    elif opcion_algoritmo == "2":
        resultado = ordenar_insercion(catalogo, criterio)
        nombre_algoritmo = "inserción"

    else:
        print("Opcion invalida.")
        return

    print()
    print(
        "Catálogo ordenado por",
        nombre_criterio,
        "con",
        nombre_algoritmo
    )

    for cancion in resultado:

        if nombre_criterio == "título":
            print(
                cancion.titulo,
                "-",
                cancion.artista,
                "-",
                cancion.duracion_seg,
                "segundos"
            )

        elif nombre_criterio == "duración":
            print(
                cancion.duracion_seg,
                "segundos",
                "-",
                cancion.titulo,
                "-",
                cancion.artista
            )

        elif nombre_criterio == "artista":
            print(
                cancion.artista,
                "-",
                cancion.titulo,
                "-",

                cancion.duracion_seg,
                "segundos"
            )

def menu_buscar():

    print()
    print("--- Buscar canción ---")
    print("1. Por título - búsqueda lineal")
    print("2. Por título - búsqueda binaria")
    print("0. Volver")

    print()
    opcion = input("Ingrese una opcion: ").strip()

    if opcion == "0":
        return

    elif opcion == "1":

        titulo = input("Ingrese el título: ").strip().casefold()

        resultado = busqueda_lineal(
            catalogo,
            titulo,
            obtener_titulo
        )

        if resultado is None:
            print("Canción no encontrada.")
        else:
            print("ID:", resultado.id)
            print("Título:", resultado.titulo)
            print("Artista:", resultado.artista)
            print("Álbum:", resultado.album)
            print("Duración:", resultado.duracion_seg, "segundos")

    elif opcion == "2":


        titulo = input("Ingrese el título: ").strip().casefold()

        catalogo_ordenado = ordenar_seleccion(
            catalogo,
            obtener_titulo
        )

        print("Catálogo ordenado por título para usar búsqueda binaria.")

        resultado = busqueda_binaria(
            catalogo_ordenado,
            titulo,
            obtener_titulo
        )

        if resultado is None:
            print("Canción no encontrada.")
        else:
            print("ID:", resultado.id)
            print("Título:", resultado.titulo)
            print("Artista:", resultado.artista)
            print("Álbum:", resultado.album)
            print("Duración:", resultado.duracion_seg, "segundos")

    else:
        print("Opcion invalida.")

def menu_persistencia():

    while True:

        print()
        print("--- Guardar / cargar / gestionar datos ---")
        print("1. Agregar canción")
        print("2. Modificar canción")
        print("3. Eliminar canción")
        print("4. Guardar catálogo en texto")
        print("5. Cargar catálogo desde texto")
        print("6. Guardar catálogo en binario")
        print("7. Cargar catálogo desde binario")
        print("0. Volver")

        print()
        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":

            print()
            print("--- Alta de canción ---")

            nuevo_id = 1

            for cancion in catalogo:
                if cancion.id >= nuevo_id:
                    nuevo_id = cancion.id + 1

            print("ID asignado:", nuevo_id)

            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            album = input("Álbum: ").strip()
            genero = input("Género: ").strip()

            entrada_anio = input("Año: ").strip()
            entrada_duracion = input("Duración en segundos: ").strip()

            if not entrada_anio.isdigit() or not entrada_duracion.isdigit():
                print("Año y duración deben ser numéricos.")
                continue

            anio = int(entrada_anio)
            duracion = int(entrada_duracion)

            anio_actual = datetime.now().year

            if anio < 1 or anio > anio_actual:
                print(f"El año debe estar entre 1 y {anio_actual}.")
                continue

            if duracion < 1 or duracion > 65535:
                print("La duración debe estar entre 1 y 65535 segundos.")
                continue

            nueva = Cancion(
                nuevo_id,
                titulo,
                artista,
                album,
                genero,
                anio,
                duracion,
                None,
                None
            )

            catalogo.append(nueva)

            guardar_catalogo(catalogo)
            guardar_binario("data/canciones.bin", catalogo)

            print("Canción agregada y cambios guardados.")

        elif opcion == "2":

            print()
            print("--- Modificar canción ---")

            entrada_id = input("ID de la canción a modificar: ").strip()

            if not entrada_id.isdigit():
                print("El ID debe ser numérico.")
                continue

            id_cancion = int(entrada_id)

            cancion = biblioteca.buscar_por_id(id_cancion)

            if cancion is None:
                print("Canción no encontrada.")
                continue

            print("Título actual:", cancion.titulo)
            titulo = input("Nuevo título (Enter para mantener): ").strip()

            print("Artista actual:", cancion.artista)
            artista = input("Nuevo artista (Enter para mantener): ").strip()

            print("Álbum actual:", cancion.album)
            album = input("Nuevo álbum (Enter para mantener): ").strip()

            print("Género actual:", cancion.genero)
            genero = input("Nuevo género (Enter para mantener): ").strip()

            print("Año actual:", cancion.anio)
            entrada_anio = input("Nuevo año (Enter para mantener): ").strip()

            print("Duración actual:", cancion.duracion_seg)
            entrada_duracion = input(
                "Nueva duración en segundos (Enter para mantener): "
            ).strip()

            if entrada_anio and not entrada_anio.isdigit():
                print("El año debe ser numérico.")
                continue

            if entrada_duracion and not entrada_duracion.isdigit():
                print("La duración debe ser numérica.")
                continue

            if entrada_anio:
                nuevo_anio = int(entrada_anio)

                anio_actual = datetime.now().year

                if nuevo_anio < 1 or nuevo_anio > anio_actual:
                    print(f"El año debe estar entre 1 y {anio_actual}.")
                    continue

            if entrada_duracion:
                nueva_duracion = int(entrada_duracion)

                if nueva_duracion < 1 or nueva_duracion > 65535:
                    print("La duración debe estar entre 1 y 65535 segundos.")
                    continue

            if titulo:
                cancion.titulo = titulo

            if artista:
                cancion.artista = artista

            if album:
                cancion.album = album

            if genero:
                cancion.genero = genero

            if entrada_anio:
                cancion.anio = nuevo_anio

            if entrada_duracion:
                cancion.duracion_seg = nueva_duracion

            while True:
                entrada_version = input(
                    "Nuevo ID de origen, None para independiente "
                    "o Enter para mantener: "
                ).strip()

                if entrada_version == "":
                    break

                if entrada_version.lower() == "none":
                    cancion.version_de = None
                    cancion.tipo_version = None
                    break

                if entrada_version.isdigit():
                    nuevo_origen = int(entrada_version)

                    if biblioteca.buscar_por_id(nuevo_origen) is None:
                        print("Ese ID no existe.")
                        continue

                    if nuevo_origen == cancion.id:
                        print("Una canción no puede derivar de sí misma.")
                        continue

                    cancion.version_de = nuevo_origen

                    while True:
                        tipo = input(
                            "Tipo de versión (cover/live/remix): "
                        ).strip().lower()

                        if tipo == "cover" or tipo == "live" or tipo == "remix":
                            cancion.tipo_version = tipo
                            break

                        print("Debe ingresar cover, live o remix.")

                    break

                print("Debe ingresar un ID numérico, None o Enter.")

            guardar_catalogo(catalogo)

            ruta_binario = Path("data/canciones.bin")

            if ruta_binario.exists():
                canciones_binario = cargar_binario(ruta_binario)
                posicion = None

                for i in range(len(canciones_binario)):
                    if canciones_binario[i].id == cancion.id:
                        posicion = i
                        break

                if posicion is not None:
                    actualizar_registro(ruta_binario, posicion, cancion)

            print("Canción modificada y guardada.")

        elif opcion == "3":

            print()
            print("--- Eliminar canción ---")

            entrada_id = input("ID de la canción a eliminar: ").strip()

            if not entrada_id.isdigit():
                print("El ID debe ser numérico.")
                continue

            id_cancion = int(entrada_id)

            cancion = biblioteca.buscar_por_id(id_cancion)

            if cancion is None:
                print("Canción no encontrada.")
                continue

            tiene_derivadas = False

            for otra_cancion in catalogo:
                if otra_cancion.version_de == id_cancion:
                    tiene_derivadas = True
                    break

            if tiene_derivadas:
                print("No se puede eliminar: hay canciones que derivan de ella.")
                continue

            catalogo.remove(cancion)

            guardar_catalogo(catalogo)
            guardar_binario("data/canciones.bin", catalogo)

            print("Canción eliminada y cambios guardados.")

        elif opcion == "4":
            guardar_catalogo(catalogo)
            print("Catálogo guardado en archivos de texto.")

        elif opcion == "5":

            try:
                nuevo_catalogo = cargar_canciones("data/canciones.txt")
                cargar_versiones("data/versiones.txt", nuevo_catalogo)

                catalogo.clear()
                catalogo.extend(nuevo_catalogo)

                print("Catálogo cargado desde archivos de texto.")

            except ArchivoInvalidoError as error:
                print("Archivo inválido:", error)


        elif opcion == "6":
            guardar_binario("data/canciones.bin", catalogo)
            print("Catálogo guardado en archivo binario.")

        elif opcion == "7":

            try:
                nuevo_catalogo = cargar_binario("data/canciones.bin")
                cargar_versiones("data/versiones.txt", nuevo_catalogo)

                catalogo.clear()
                catalogo.extend(nuevo_catalogo)

                print("Catálogo cargado desde archivo binario.")

            except ArchivoInvalidoError as error:
                print("Archivo inválido:", error)

        else:
            print("Opción inválida.")


def main():

    if error_inicio is not None:
        print("")
        print("No se puede iniciar el programa.")
        print("Archivo inválido:", error_inicio)
        print("")
        return

    if TEMA not in TEMAS:
        print(
            "Seteá TEMA en src/config.py: "
            "'pokedex', 'recetario' o 'musica'."

        )

        return

    opcion = None

    while opcion != "0":

        mostrar_menu()

        print()
        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "0":

            print()
            print("Chau.")

        elif opcion == "2":
            ver_detalle()

        elif opcion == "9":
            menu_persistencia()

        elif opcion == "3":

            menu_buscar()

        elif opcion == "4":

            menu_ordenar()

        elif opcion == "8":

            menu_reproduccion()

        elif opcion == "7":

            menu_historial()

        elif opcion == "1":

            print()
            biblioteca.listar_catalogo_dos_columnas()

        elif opcion == "5":
            print()
            mostrar_cadena_versiones(biblioteca)

        elif opcion == "6":

            menu_playlist()

if __name__ == "__main__":
    main()