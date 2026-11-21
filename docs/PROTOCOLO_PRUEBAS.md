# Protocolo de pruebas

Este documento registra los casos de prueba ejecutados para verificar el funcionamiento final del programa.

| ID | Entrega | Acción | Datos de entrada | Resultado esperado | Resultado |
| --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar el catálogo | Ejecutar `python -m src.main` y elegir opción `1` | El programa inicia sin traceback y se muestran las canciones del catálogo | PASA |
| P02 | E1 | Consultar un ítem inexistente | Opción `2`, ID inexistente | Se muestra `Canción no encontrada.` y el programa vuelve al menú | PASA |
| P03 | E2 | Recursión sobre una canción con cadena de versiones | Opción `5`, ID `68` | Se muestran 68, 69, 70 y 71 respetando la relación de versiones derivadas | PASA |
| P04 | E2 | Recursión sobre una canción sin versiones derivadas | Opción `5`, ID `70` | Se muestra la canción y el mensaje `La cancion no tiene versiones derivadas` | PASA |
| P05 | E3 | Agregar canciones a la playlist hasta superar el tope | Agregar seis canciones | La sexta canción no se agrega y se muestra `La playlist esta llena` | PASA |
| P06 | E3 | Desapilar con el historial vacío | Opción `7`, sacar última reproducción sin historial | Se captura `PilaVaciaError`, se muestra un mensaje y el programa continúa | PASA |
| P07 | E3 | Desencolar una cola vacía | Intentar avanzar la reproducción sin canciones pendientes | Se captura `ColaVaciaError`, se muestra un mensaje y el programa continúa | PASA |
| P08 | E3 | Listar la colección utilizando el iterador | Agregar canciones a la playlist y listarlas | Las canciones aparecen en el mismo orden en que fueron agregadas | PASA |
| P09 | E4 | Búsqueda lineal de una canción existente | Buscar por título `La Balsa` | Se encuentra la canción y se muestran sus datos | PASA |
| P10 | E4 | Búsqueda lineal de una canción inexistente | Buscar `Cancion que no existe` | Se muestra `Canción no encontrada.` y el programa continúa | PASA |
| P11 | E4 | Búsqueda binaria con catálogo inicialmente desordenado | Buscar `La Balsa` mediante búsqueda binaria | El catálogo se ordena previamente, se informa al usuario y la búsqueda funciona correctamente | PASA |
| P12 | E4 | Ordenar por distintos criterios | Ordenar primero por un criterio y luego por otro | El orden cambia correctamente de acuerdo con el criterio elegido | PASA |
| P13 | E5 | Guardar y recargar texto | Guardar el catálogo en `.txt`, salir y volver a entrar | Las canciones y relaciones de versiones se mantienen correctamente | PASA |
| P14 | E5 | Actualización binaria por posición | Guardar binario, modificar una canción por ID y recargar | La modificación queda almacenada y aparece al recargar | PASA |
| P15 | E5 | Archivo inválido | Probar magia incorrecta, binario truncado y texto con cantidad incorrecta de campos | Se captura `ArchivoInvalidoError`, se muestra un mensaje claro y no aparece traceback | PASA |

## Regresión final de E6

Además de los casos P01–P15, se verificaron nuevamente las diez operaciones del menú final:

- listado del catálogo mediante iterador;
- consulta de detalle por ID;
- búsqueda lineal y binaria;
- ordenamiento por distintos criterios;
- versiones derivadas mediante recursión;
- gestión de playlist con alta, baja y cambio de orden;
- historial mediante pila;
- reproducción mediante cola;
- persistencia en texto y binario;
- salida normal del programa.

Las operaciones continúan funcionando sin traceback.


## Verificaciones complementarias realizadas en E6

Durante la revisión final también se realizaron comprobaciones complementarias, sin agregarlas como nuevos casos al protocolo P01–P15:

- agregar y eliminar canciones de la playlist;
- reproducir canciones en orden FIFO y consultar el historial;
- realizar búsqueda binaria con ordenamiento previo del catálogo por título;
- ordenar mediante selección por duración e inserción por artista;
- desencolar una cola vacía y comprobar `ColaVaciaError`;
- validar archivos binarios con encabezado incompleto, magia incorrecta, tema incorrecto y registros faltantes, además de archivos de texto con cantidad incorrecta de campos.

### Observaciones de las pruebas

- Se corrigieron errores en el menú de historial y en la eliminación de canciones de la playlist.
- La búsqueda binaria informó que ordenó el catálogo por título antes de buscar.
- Las pruebas directas confirmaron que se lanzan correctamente `ColaVaciaError` y `ArchivoInvalidoError`; desde el menú estas excepciones son capturadas y se muestran mensajes controlados, sin traceback.
- Las pruebas de archivos inválidos se realizaron con archivos temporales, sin modificar los datos originales.
- Se verificó desde el menú que los archivos inválidos generan mensajes controlados mediante `ArchivoInvalidoError`, sin traceback, y que el programa continúa funcionando.