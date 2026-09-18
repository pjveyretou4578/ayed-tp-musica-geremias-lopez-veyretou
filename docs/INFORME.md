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

Cada objeto `Playlist` tiene un nombre y una lista de canciones.

Actualmente posee los métodos:

- `agregar_cancion(cancion)`: agrega una canción a la playlist.
- `duracion_total()`: calcula la duración total de las canciones agregadas.

En esta entrega la clase queda definida como parte del modelo del dominio. La funcionalidad completa de la colección principal y los TAD correspondientes se desarrollará en las entregas posteriores.

### Estructuras utilizadas

En esta entrega se utilizan listas de Python dentro de las clases.

Los TAD obligatorios de lista enlazada, pila y cola todavía no se implementan, ya que corresponden a la Entrega 3.

Se conservaron los datos utilizados en la Entrega 1 y se amplió el catálogo para poder representar un caso con varias versiones derivadas y una versión de una versión.

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

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

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