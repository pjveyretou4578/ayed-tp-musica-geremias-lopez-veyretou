def versiones_de(biblioteca, id_cancion):

    directas = biblioteca.versiones_directas(id_cancion)

    # CASO BASE
    if len(directas) == 0:
        return []

    resultado = []

    # CASO RECURSIVO
    for version_id in directas:

        resultado.append(version_id)

        resultado_hijo = versiones_de(
            biblioteca,
            version_id
        )

        resultado = resultado + resultado_hijo

    return resultado


def mostrar_arbol_versiones(biblioteca, id_cancion, nivel=0):

    directas = biblioteca.versiones_directas(id_cancion)

    for version_id in directas:

        cancion = biblioteca.buscar_por_id(version_id)

        print(
            "    " * nivel,
            cancion.id,
            "-",
            cancion.titulo,
            "-",
            cancion.artista
        )

        mostrar_arbol_versiones(
            biblioteca,
            version_id,
            nivel + 1
        )


def mostrar_cadena_versiones(biblioteca):

    entrada = input("Ingrese el id de la cancion: ").strip()

    try:
        id_ingresado = int(entrada)
    except ValueError:
        print("El ID debe ser un numero.")
        return

    cancion_encontrada = biblioteca.buscar_por_id(id_ingresado)

    if cancion_encontrada is None:
        print("Cancion no encontrada")
        return

    print(
        cancion_encontrada.id,
        "-",
        cancion_encontrada.titulo,
        "-",
        cancion_encontrada.artista
    )

    cadena = versiones_de(
        biblioteca,
        id_ingresado
    )

    if len(cadena) == 0:
        print("La cancion no tiene versiones derivadas")
        return

    mostrar_arbol_versiones(
        biblioteca,
        id_ingresado,
        1
    )