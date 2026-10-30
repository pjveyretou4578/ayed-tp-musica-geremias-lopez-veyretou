from src.config import TEMA
from src.dominio.cancion import catalogo
from src.dominio.versiones import mostrar_cadena_versiones
from src.dominio.biblioteca import Biblioteca
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

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


def pendiente():
    print()
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


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
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def menu_playlist():

    while True:

        print()
        print("--- Playlist ---")
        print("1. Agregar cancion")
        print("2. Eliminar cancion")
        print("3. Listar playlist")
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

        elif opcion == "3":

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



def main():

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

        elif opcion in {"2", "9"}:
            pendiente()

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