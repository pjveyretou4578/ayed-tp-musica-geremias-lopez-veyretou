# Protocolo de pruebas

Este documento registra los casos de prueba definidos para verificar el funcionamiento del programa.

En la Entrega 2 no es obligatorio ejecutar formalmente todos los casos. Por ese motivo, el campo `Resultado` se deja como `No corrido`.

| ID | Entrega | Acción | Datos de entrada | Resultado esperado | Resultado | Motivo / Qué comprueba |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E2 | Listar el catálogo | Opción `1` | Se muestran las canciones del catálogo sin producir errores. | No corrido | Comprueba que la clase `Biblioteca` contiene las canciones y que el método `listar_catalogo()` funciona. |
| P02 | E2 | Buscar versiones derivadas de una canción con dos ramas | Opción `5`, id `68` | Se muestra la canción 68 y las versiones 69, 70 y 71. La canción 70 debe aparecer como derivada de la 69. | No corrido | Comprueba la recursión con varias ramas y una versión de una versión. |
| P03 | E2 | Buscar versiones desde una canción intermedia | Opción `5`, id `69` | Se muestra la canción 69 y debajo la canción 70. | No corrido | Comprueba que la búsqueda recursiva puede comenzar desde una versión y encontrar sus propias versiones derivadas. |
| P04 | E2 | Buscar versiones de una canción sin versiones derivadas | Opción `5`, id `70` | Se muestra la canción 70 y el mensaje `La cancion no tiene versiones derivadas`. | No corrido | Comprueba el caso base de la función recursiva. |
| P05 | E2 | Buscar un id inexistente | Opción `5`, id `99` | Se muestra `Cancion no encontrada` y el programa vuelve al menú. | No corrido | Comprueba que el programa controla la búsqueda de un identificador que no existe. |
| P06 | E2 | Buscar una relación del dataset original | Opción `5`, id `51` | Se muestra la canción 51 y su versión derivada con id 52. | No corrido | Comprueba que la recursión funciona también con las relaciones originales del dataset. |
| P07 | E2 | Buscar otra relación del dataset original | Opción `5`, id `12` | Se muestra la canción 12 y su versión derivada con id 13. | No corrido | Comprueba el funcionamiento con otro par de canciones relacionadas. |
| P08 | E2 | Ingresar una opción de menú inválida | `9z` | Se muestra `Opción inválida.` y vuelve a aparecer el menú. | No corrido | Comprueba que una opción inexistente no finaliza el programa. |
| P09 | E2 | Presionar Enter sin ingresar una opción | Entrada vacía | Se muestra `Opción inválida.` y vuelve a aparecer el menú. | No corrido | Comprueba que una entrada vacía en el menú no produce un error. |
| P10 | E2 | Salir del programa | Opción `0` | Se muestra `Chau.` y finaliza el programa. | No corrido | Comprueba la salida normal del programa. |
| P11 | E2 | Ingresar un id no numérico | Opción `5`, id `abc` | Se muestra `El ID debe ser un numero.` y el programa vuelve al menú. | No corrido | Comprueba que una entrada no numérica no produce un error de ejecución. |