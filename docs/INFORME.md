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

`id`, `titulo`, `artista`, `album`, `genero`, `anio`, `duracion_seg` y `version_de`.

El atributo `version_de` permite relacionar una canción con otra de la cual deriva.

Si `version_de = None`, la canción no está definida como versión de otra canción.

### Biblioteca

La clase `Biblioteca` representa el catálogo general de canciones.

Contiene una lista de objetos `Cancion` en el atributo `canciones`.

Actualmente posee los métodos:

- `listar_catalogo()`: muestra las canciones de la biblioteca.
- `buscar_por_id(id_cancion)`: busca una canción por su identificador y devuelve el objeto encontrado o `None`.
- `versiones_directas(id_cancion)`: devuelve una lista con los ids de las canciones que derivan directamente de la canción indicada.

La opción 1 del menú utiliza un objeto `Biblioteca` para listar el catálogo.

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
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |