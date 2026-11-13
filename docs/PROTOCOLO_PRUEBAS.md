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
## Entrega 3 — Pruebas ejecutadas

| ID E3 | Acción | Resultado esperado | Resultado |
| --- | --- | --- | --- |
| P05 | Agregar canciones a la playlist hasta superar el tope | La sexta canción no se agrega y se muestra `La playlist esta llena` | PASA |
| P06 | Sacar una reproducción con el historial vacío | Se muestra que la pila está vacía y el programa continúa | PASA |
| P07   | Desencolar una cola de reproducción vacía | Se produce `ColaVaciaError`, se muestra `La cola esta vacia` y el programa continúa | PASA |
| P08 | Listar la playlist | Las canciones aparecen en el mismo orden en que fueron agregadas | PASA |

## Entrega 4 — Pruebas ejecutadas

| ID E4 | Acción | Datos de entrada | Resultado esperado | Resultado |
| --- | --- | --- | --- | --- |
| P09 | Búsqueda lineal de una canción existente | Buscar por título `La Balsa` | Se encuentra la canción y se muestran ID, título, artista, álbum y duración | PASA |
| P10 | Búsqueda lineal de una canción inexistente | Buscar `Cancion que no existe` | Se muestra `Canción no encontrada.` | PASA |
| P11 | Búsqueda binaria sobre el catálogo | Buscar por título `La Balsa` mediante búsqueda binaria | El catálogo se ordena previamente por título, se informa al usuario y se muestran ID, título, artista, álbum y duración | PASA |
| P12 | Ordenar el catálogo con distintos algoritmos y criterios | Elegir selección o inserción y ordenar por título, duración o artista | El catálogo se ordena según el algoritmo y criterio elegidos, mostrando título, artista y duración | PASA |
**Regresión adicional de E3:** se probaron versiones derivadas con ID 68, playlist, historial y reproducción con cola. Todas continuaron funcionando correctamente.

## Entrega 5 — Pruebas ejecutadas

| ID E5 | Acción | Datos de entrada | Resultado esperado | Resultado |
| --- | --- | --- | --- | --- |
| P13 | Guardar y recargar texto | Guardar el catálogo en `.txt`, salir del programa y volver a entrar | Las canciones y las relaciones de versiones se mantienen correctamente | PASA |
| P14 | Actualización binaria | Guardar el catálogo en binario, modificar una canción por ID y volver a cargar desde binario | La modificación queda almacenada y aparece al recargar | PASA |
| P15 | Archivo inválido | Intentar cargar archivos con magia incorrecta, binario truncado y texto con cantidad incorrecta de campos | Se muestra `ArchivoInvalidoError` con mensaje claro y sin traceback | PASA |