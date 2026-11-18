# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical

- Por qué lo eligieron (5–8 líneas):

Elegimos Biblioteca Musical porque nos pareció lo más sencillo de entender. Si bien la cátedra aclara que los tres temas son la misma consigna con distinta piel, las entidades de este tema, canciones, artistas, géneros y playlists, nos resultan más familiares que las de Pokémon o las recetas. Al comparar las relaciones propuestas para cada dominio, nos resultó más fácil visualizar canciones y sus versiones que relaciones de sub-recetas o cadenas de evolución.

## 2. Modelo

Los ítems del catálogo son las canciones.

En la Entrega 1 cada canción estaba representada mediante un diccionario.

En la Entrega 2 se incorporaron clases para representar los principales conceptos del dominio de la biblioteca musical.

### Cancion

La clase `Cancion` representa una canción del catálogo.

Cada objeto `Cancion` contiene los atributos:

`id`, `titulo`, `artista`, `album`, `genero`, `anio`, `duracion_seg`, `version_de` y `tipo_version`.

El atributo `version_de` permite relacionar una canción con otra de la cual deriva.

Si `version_de = None`, la canción no está definida como versión de otra canción.

El atributo `tipo_version` indica el tipo de relación con la canción original, por ejemplo `cover`, `live` o `remix`.

### Biblioteca

La clase `Biblioteca` representa el catálogo general de canciones.

Contiene una lista de objetos `Cancion` en el atributo `canciones`.

Actualmente posee los métodos:

- `listar_catalogo()`: muestra las canciones de la biblioteca.
- `listar_catalogo_dos_columnas()`: muestra el catálogo en dos columnas y distingue los títulos repetidos.
- `buscar_por_id(id_cancion)`: busca una canción por su identificador y devuelve el objeto encontrado o `None`.
- `versiones_directas(id_cancion)`: devuelve una lista con los ids de las canciones que derivan directamente de la canción indicada.

La opción 1 del menú utiliza `listar_catalogo_dos_columnas()` para mostrar el catálogo mediante el recorrido de la colección.

De esta manera, la clase `Biblioteca` se encarga de encontrar las versiones directas y la función `versiones_de()` se encarga de recorrer recursivamente las versiones de esas versiones.

### Playlist

La clase `Playlist` representa una selección de canciones.

Cada objeto `Playlist` tiene un nombre, una colección de canciones y un máximo permitido.

En la Entrega 3, las canciones de la playlist se almacenan en una `ListaEnlazada`.

Actualmente posee los métodos:

- `agregar_cancion(cancion)`: agrega una canción a la playlist si no se alcanzó el máximo.
- `duracion_total()`: calcula la duración total de las canciones agregadas.
- `listar()`: muestra las canciones de la playlist.
- `eliminar_cancion(cancion)`: elimina una canción de la playlist.
- `mover_al_inicio(cancion)`: mueve una canción existente al comienzo de la playlist.
- `mover_al_final(cancion)`: mueve una canción existente al final de la playlist.

Los métodos de cambio de orden permiten modificar la posición de las canciones dentro de la playlist sin alterar los datos de las canciones del catálogo. De esta manera se puede cambiar el orden en que serán reproducidas.

Si se intenta superar el máximo de cinco canciones, se lanza `ColeccionLlenaError`.

### Estructuras utilizadas

En la Entrega 3 se reemplazó el uso de listas de Python en la colección principal por una `ListaEnlazada` propia.

También se implementaron una `Pila` para el historial de reproducción y una `Cola` para las canciones pendientes de reproducción.

## 3. Recursión (E2)

- Función: `versiones_de(biblioteca, id_cancion)`

- Objetivo:

Buscar todas las versiones que derivan de una canción y también las versiones que derivan de esas versiones.

La función recursiva no recorre directamente el catálogo para buscar las versiones. Esa tarea se delega al método `Biblioteca.versiones_directas(id_cancion)`.

Primero le pide a la clase `Biblioteca` las versiones directas de una canción mediante:

`biblioteca.versiones_directas(id_cancion)`

Ese método devuelve una lista con los ids de las canciones que derivan directamente de la canción indicada.

- Caso base:

Si `biblioteca.versiones_directas(id_cancion)` devuelve una lista vacía, significa que la canción no tiene versiones derivadas.

En ese caso:

`directas = []`

y la función devuelve:

`[]`

- Caso recursivo:

Si existen versiones directas, la función recorre esos ids uno por uno.

Cada id se agrega a `resultado`.

Después, para cada versión encontrada, la función vuelve a llamarse para buscar si esa versión también tiene otras versiones derivadas.

El resultado de esa llamada se guarda en `resultado_hijo` y luego se suma al resultado de la llamada actual.

La parte principal de la función es:

```python
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
```

### Ejemplo del catálogo

Se utiliza la canción con id `68`:

`68 - Hallelujah - Leonard Cohen`

Las relaciones son:

- `69` deriva de `68`.
- `70` deriva de `69`.
- `71` deriva de `68`.

Por lo tanto, la estructura es:

```text
68 - Hallelujah - Leonard Cohen
    69 - Hallelujah - John Cale
        70 - Hallelujah - Jeff Buckley
    71 - Hallelujah - Pentatonix
```

### Traza

1. Se llama:

   `versiones_de(biblioteca, 68)`

   `biblioteca.versiones_directas(68)` devuelve:

   `[69, 71]`

   Entonces:

   `directas = [69, 71]`

   Se crea:

   `resultado = []`

2. El `for` toma primero:

   `version_id = 69`

   Se ejecuta:

   `resultado.append(69)`

   y queda:

   `resultado = [69]`

   Después se llama:

   `versiones_de(biblioteca, 69)`

   La llamada correspondiente a `68` queda pausada.

3. En `versiones_de(biblioteca, 69)`:

   `biblioteca.versiones_directas(69)` devuelve:

   `[70]`

   Entonces:

   `directas = [70]`

   Se crea un nuevo:

   `resultado = []`

   Se agrega `70`:

   `resultado = [70]`

   y se llama:

   `versiones_de(biblioteca, 70)`

4. En `versiones_de(biblioteca, 70)`:

   `biblioteca.versiones_directas(70)` devuelve:

   `[]`

   Se llega al caso base:

   `return []`

5. Se reactiva la llamada correspondiente a `69`.

   La llamada de `70` devolvió:

   `[]`

   Entonces:

   `resultado_hijo = []`

   y:

   `resultado = [70] + []`

   queda:

   `resultado = [70]`

   La función devuelve:

   `[70]`

6. Se reactiva la llamada correspondiente a `68`.

   Antes tenía:

   `resultado = [69]`

   La llamada de `69` devolvió:

   `[70]`

   Entonces:

   `resultado_hijo = [70]`

   y:

   `resultado = [69] + [70]`

   queda:

   `resultado = [69, 70]`

7. El `for` continúa con:

   `version_id = 71`

   Se ejecuta:

   `resultado.append(71)`

   y queda:

   `resultado = [69, 70, 71]`

   Después se llama:

   `versiones_de(biblioteca, 71)`

8. En `versiones_de(biblioteca, 71)`:

   no se encuentran versiones directas.

   Entonces:

   `directas = []`

   y se llega al caso base:

   `return []`

9. Se reactiva nuevamente la llamada correspondiente a `68`.

   La llamada de `71` devolvió:

   `[]`

   Entonces:

   `resultado = [69, 70, 71] + []`

   y queda:

   `resultado = [69, 70, 71]`

10. Como ya no quedan elementos en `directas = [69, 71]`, termina el `for` y se ejecuta:

    `return resultado`

Resultado final:

`[69, 70, 71]`

La salida mostrada por el programa es:

```text
68 - Hallelujah - Leonard Cohen
    69 - Hallelujah - John Cale
        70 - Hallelujah - Jeff Buckley
    71 - Hallelujah - Pentatonix
```

## 4. TADs (E3)

En la Entrega 3 se implementaron los TAD lineales requeridos por la cátedra utilizando nodos propios.

La `ListaEnlazada` no utiliza una lista de Python como estructura interna. La `Pila` y la `Cola` se construyen utilizando `ListaEnlazada`.

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar al inicio, insertar al final, insertar ordenado, eliminar, buscar, obtener tamaño, comprobar si está vacía, recorrer mediante `__iter__` | `_cabeza` apunta al primer nodo o es `None` si la lista está vacía. `_tamanio` coincide con la cantidad de nodos de la lista. Cada nodo apunta al siguiente o a `None` si es el último. |
| Pila | `apilar`, `desapilar`, `ver_tope`, `esta_vacia`, recorrer con iterador | Se respeta el criterio LIFO: el último elemento apilado es el primero que se desapila. El tope corresponde al primer nodo de la lista enlazada interna. |
| Cola | `encolar`, `desencolar`, `ver_frente`, `esta_vacia`, recorrer con iterador | Se respeta el criterio FIFO: el primer elemento encolado es el primero que se desencola. Los nuevos elementos se agregan al final y se retiran desde el frente. |

### Uso de los TAD en el dominio

La `Playlist` es la colección principal del dominio y utiliza una `ListaEnlazada` para almacenar canciones. Se estableció un máximo de cinco canciones. Si se intenta superar ese límite se lanza la excepción `ColeccionLlenaError`.

El historial de reproducción utiliza una `Pila`. Cuando una canción deja de ser la canción actual y se avanza a la siguiente, la canción anterior se apila en el historial. Esto permite consultar o eliminar primero la reproducción más reciente.

La reproducción pendiente utiliza una `Cola`. Al iniciar la reproducción de una playlist, sus canciones se encolan en el mismo orden en que aparecen en la playlist. La primera canción pendiente es la primera que se reproduce.

El recorrido de las estructuras se realiza mediante el iterador definido con `__iter__` y `yield`.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo en dos columnas | O(n²) | O(1) | Para cada canción se vuelve a recorrer el catálogo para detectar títulos repetidos. |
| Buscar canción por ID | O(n) peor caso | O(1) | Se recorren las canciones una por una hasta encontrar el ID o llegar al final. |
| Búsqueda lineal por título | O(n) peor / O(1) mejor | O(1) | Puede encontrar la canción en la primera comparación o recorrer todo el catálogo. |
| Búsqueda binaria por título | O(log n) | O(1) | En cada comparación se descarta aproximadamente la mitad del rango de búsqueda. |
| Ordenamiento por selección | O(n²) | O(n) | Para cada posición se recorre el resto de la colección para buscar el menor. Además se crea una copia de la colección. |
| Ordenamiento por inserción | O(n) mejor / O(n²) peor | O(n) | Si ya está ordenado casi no desplaza elementos; en el peor caso desplaza muchos. Además se crea una copia de la colección. |
| Recorrer versiones derivadas | O(n²) peor caso | O(n) | Por cada canción visitada por la recursión se vuelve a recorrer el catálogo para buscar versiones directas. |
| Listar playlist | O(p) | O(1) | Se recorre una vez la lista enlazada de la playlist. |
| Ver tope de pila | O(1) | O(1) | Se accede directamente al primer nodo. |
| Apilar | O(1) | O(1) | Se inserta al inicio de la lista enlazada. |
| Desapilar | O(1) | O(1) | Se elimina el primer nodo de la lista enlazada. |
| Desencolar | O(1) | O(1) | Se elimina el primer nodo de la cola. |
| Encolar | O(n) | O(1) | La implementación actual recorre la lista enlazada hasta llegar al último nodo para insertar. |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal | 71 | 0.0000148 |
| Búsqueda lineal | 710 | 0.000117 |
| Búsqueda binaria | 71 | 0.00000402 |
| Búsqueda binaria | 710 | 0.00000794 |
| Ordenamiento por selección | 71 | 0.000926 |
| Ordenamiento por selección | 710 | 0.09416 |
| Ordenamiento por inserción | 71 | 0.001657 |
| Ordenamiento por inserción | 710 | 0.06430 |

Para reducir la variación de mediciones muy pequeñas, cada búsqueda se ejecutó 1000 veces y cada ordenamiento 100 veces. En la tabla se informa el tiempo promedio por ejecución.

Los tiempos corresponden a una corrida de medición realizada con `time.perf_counter()`. Pueden variar entre ejecuciones según la carga del sistema, por lo que se utiliza principalmente la tendencia de crecimiento para comparar con la complejidad teórica.

En la búsqueda binaria se midió únicamente la función de búsqueda sobre una colección previamente ordenada por título. El tiempo necesario para ordenar la colección no se incluyó en la medición, ya que se buscó observar específicamente el comportamiento O(log n) de la búsqueda binaria.

### Comparación con la complejidad teórica

| Operación | Aumento de n | Aumento observado | Comportamiento teórico |
| --- | --- | --- | --- |
| Búsqueda lineal | 10 veces | 7.9 veces | O(n): se esperaba un aumento cercano a 10 veces. |
| Búsqueda binaria | 10 veces | 2.0 veces | O(log n): el tiempo aumenta poco al crecer n. |
| Ordenamiento por selección | 10 veces | 101.7 veces | O(n²): se esperaba un aumento cercano a 100 veces. |
| Ordenamiento por inserción | 10 veces | 38.8 veces | O(n²) en el peor caso; depende del orden inicial de los datos. |

Los resultados son coherentes con las complejidades teóricas. La búsqueda lineal aumentó aproximadamente en proporción al tamaño del catálogo, mientras que la búsqueda binaria aumentó mucho menos. El ordenamiento por selección mostró un crecimiento prácticamente cuadrático. En el ordenamiento por inserción el aumento fue menor que el peor caso teórico porque la cantidad de desplazamientos depende del orden inicial de los elementos.

## 6. Persistencia (E5)

En la Entrega 5 se implementó persistencia en dos formatos: texto simple y binario.

### 6.1 Persistencia en texto

El catálogo se guarda en dos archivos de texto:

- `data/canciones.txt`: contiene los datos principales de cada canción.
- `data/versiones.txt`: contiene las relaciones entre canciones originales y sus versiones.

Los archivos tienen un encabezado en la primera línea y los campos están separados por comas.

Al iniciar el programa, las canciones se cargan desde `canciones.txt` y luego se aplican las relaciones almacenadas en `versiones.txt`.

Las funciones principales utilizadas son `cargar_txt()`, `cargar_canciones()`, `cargar_versiones()` y `guardar_txt()`.

### 6.2 Persistencia binaria

Para el archivo binario se utilizó el módulo `struct` de Python y registros de longitud fija.

El header se define como:

`struct.Struct("<4s 1s I")`

Su tamaño es de 9 bytes:

- magia `AYED`: 4 bytes;
- tema `M`: 1 byte, correspondiente a Biblioteca Musical;
- cantidad de registros: entero sin signo de 4 bytes.

Cada canción se almacena con el formato:

`struct.Struct("<I 32s 45s 35s 20s 2H")`

Cada registro ocupa 140 bytes:

- `id`: 4 bytes;
- `titulo`: 32 bytes;
- `artista`: 45 bytes;
- `album`: 35 bytes;
- `genero`: 20 bytes;
- `anio`: 2 bytes;
- `duracion_seg`: 2 bytes.

Las cadenas se codifican en UTF-8 y se completan con bytes nulos (`\x00`) hasta alcanzar el ancho fijo definido para cada campo. Si un texto supera el ancho disponible, se genera `ArchivoInvalidoError` en lugar de recortarlo silenciosamente.

Las relaciones entre versiones no se guardan dentro del registro binario. Se mantienen en `versiones.txt`, lo que permite conservar un registro binario de longitud fija simple.

### 6.3 Actualización directa con `seek`

Para modificar una canción ya almacenada en el archivo binario se busca primero su posición dentro del archivo y luego se calcula el byte donde comienza el registro:

`HEADER.size + posicion * FORMATO.size`

En este proyecto:

`9 + posicion * 140`

Luego se utiliza `seek()` para mover el cursor directamente hasta esa posición y sobrescribir únicamente ese registro.

De esta forma, una modificación no requiere reescribir todo el archivo binario.

En cambio, al realizar un alta o una baja se vuelve a generar el archivo binario completo para mantener correctamente la cantidad de registros del header y las posiciones consecutivas de los registros.

### 6.4 Validación de archivos

Se implementó la excepción propia `ArchivoInvalidoError` para detectar errores de persistencia.

Entre los casos controlados se encuentran:

- archivo binario truncado;
- magia incorrecta en el header;
- tema incorrecto en el archivo binario;
- archivo de texto con una cantidad incorrecta de campos;
- IDs duplicados en `canciones.txt`;
- posiciones inválidas al realizar una actualización directa.

Además, antes de sobrescribir el archivo binario completo, los registros se convierten al formato binario para comprobar que pueden almacenarse correctamente. De esta manera, un registro inválido no comienza a sobrescribir un archivo binario existente.

Los errores de persistencia son manejados por el programa mediante `ArchivoInvalidoError`, mostrando un mensaje claro en lugar de finalizar con un traceback.



## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
| Pablo Veyretou | Desarrollo e integración de las funcionalidades del programa, revisión del menú final, pruebas, correcciones, persistencia, documentación y cierre de la Entrega 6. | Funcionamiento general del programa, modelo de dominio, recursión, TADs, búsqueda y ordenamiento, persistencia y protocolo de pruebas. |
| Ariadna Geremias | Realizó aportes en distintas entregas del proyecto, entre ellos el desarrollo de relaciones y versiones de canciones que luego fueron integradas al programa. | A definir con la integrante según las partes del proyecto que pueda defender. |
| Lucas López | No se registraron aportes concretos en las tareas desarrolladas y documentadas del proyecto. | No se asigna una parte específica para la defensa. |