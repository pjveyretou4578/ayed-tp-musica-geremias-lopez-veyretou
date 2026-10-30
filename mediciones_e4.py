from time import perf_counter

from src.main import catalogo, obtener_titulo
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion


def medir_busqueda_lineal(coleccion, repeticiones):

    inicio = perf_counter()

    for _ in range(repeticiones):
        busqueda_lineal(
            coleccion,
            "cancion que no existe",
            obtener_titulo
        )

    fin = perf_counter()

    return (fin - inicio) / repeticiones


def medir_busqueda_binaria(coleccion, repeticiones):

    coleccion_ordenada = ordenar_seleccion(
        coleccion,
        obtener_titulo
    )

    inicio = perf_counter()

    for _ in range(repeticiones):
        busqueda_binaria(
            coleccion_ordenada,
            "cancion que no existe",
            obtener_titulo
        )

    fin = perf_counter()

    return (fin - inicio) / repeticiones


def medir_seleccion(coleccion, repeticiones):

    inicio = perf_counter()

    for _ in range(repeticiones):
        ordenar_seleccion(
            coleccion,
            obtener_titulo
        )

    fin = perf_counter()

    return (fin - inicio) / repeticiones


def medir_insercion(coleccion, repeticiones):

    inicio = perf_counter()

    for _ in range(repeticiones):
        ordenar_insercion(
            coleccion,
            obtener_titulo
        )

    fin = perf_counter()

    return (fin - inicio) / repeticiones


def mostrar_mediciones(coleccion):

    print()
    print("Cantidad de canciones:", len(coleccion))

    print(
        "Búsqueda lineal:",
        medir_busqueda_lineal(coleccion, 1000)
    )

    print(
        "Búsqueda binaria:",
        medir_busqueda_binaria(coleccion, 1000)
    )

    print(
        "Ordenamiento por selección:",
        medir_seleccion(coleccion, 100)
    )

    print(
        "Ordenamiento por inserción:",
        medir_insercion(coleccion, 100)
    )


catalogo_grande = catalogo * 10

mostrar_mediciones(catalogo)
mostrar_mediciones(catalogo_grande)