# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical
- Por qué lo eligieron (5–8 líneas): 
Elegimos Biblioteca Musical porque nos parecio lo mas sencillo de entender. Si bien la catedra aclara que los tres temas son la misma consigna con distinta piel, las entidades de este tema, canciones, artistas, géneros y playlists, nos resultan mas familiares que las de pokemon o las recetas. Al comparar las relaciones propuestas para cada dominio, nos resultó más facil visualizar canciones y sus versiones que relaciones de sub-recetas o cadenas de evolución.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Los ítems del catálogo son las canciones.
Cada canción se representa mediante un diccionario con los campos:
id, título, artista, álbum, género, año y duración en segundos.
El catálogo se representa mediante una lista que contiene los diccionarios de las canciones.
La lista es mutable porque se pueden agregar, eliminar o reemplazar canciones.
Cada diccionario también es mutable porque se pueden modificar los valores asociados a sus claves.
Los valores de tipo `str` e `int` son inmutables: cuando se cambia uno de esos valores, en realidad se reemplaza por otro valor nuevo.
En esta entrega todavía no se implementan la colección principal, la pila ni la cola.
Esas relaciones se incorporarán en entregas posteriores.


## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

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
