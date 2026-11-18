# TP integrador — AyED C2 2026

Repositorio del grupo. Partir de este esqueleto. No borrar la estructura de `src/` ni de `docs/`.

## Integrantes

**Grupo:** 2

| Nombre | Mail | GitHub |
| --- | --- | --- |
|Ariadna Geremias|ageremias11@gmail.com|Ariadna1491|
|Lucas López |lucas77lopez@gmail.com|LucasL8505|
|Pablo Veyretou|pjveyretou@gmail.com|pjveyretou4578|


**Tema elegido:** Biblioteca musical 

## Cómo ejecutar

Desde la raíz del repo, con Python 3.10 o superior:

```text
python -m src.main
```

En Windows, si `python` no anda: `py -3 -m src.main`.

Solo biblioteca estándar. No hay `requirements.txt` a propósito.

## Qué hace

El programa permite:

- listar el catálogo de canciones;
- ver el detalle de una canción;
- buscar mediante búsqueda lineal y binaria;
- ordenar mediante selección e inserción;
- recorrer recursivamente versiones derivadas;
- administrar una playlist con un máximo de cinco canciones;
- utilizar una pila para el historial de reproducción;
- utilizar una cola para la reproducción pendiente;
- guardar y cargar el catálogo en texto y binario;
- actualizar registros binarios por posición.

## Limitaciones conocidas

- La playlist admite como máximo cinco canciones.
- Las relaciones entre versiones se almacenan en `versiones.txt` y no dentro del archivo binario.
- La recursión supone que las relaciones entre versiones no contienen ciclos.
- El programa funciona mediante consola y no posee interfaz gráfica.

## Entregas

Cada vencimiento se marca con un tag. Ver `GIT.md`.

| Tag | Vence |
| --- | --- |
| `preentrega` (opcional, solo repo) | domingo 30-ago-2026 23:59 |
| `entrega-1` | viernes 11-sep-2026 23:59 |
| `entrega-2` | domingo 20-sep-2026 23:59 |
| `entrega-3` | domingo 04-oct-2026 23:59 |
| `entrega-4` | domingo 01-nov-2026 23:59 |
| `entrega-5` | domingo 15-nov-2026 23:59 |
| `entrega-6` | domingo 22-nov-2026 23:59 |

Defensa oral (reemplaza el 2do parcial): 25 y 27-nov-2026.

La cátedra corrige el **tag**, no el último commit suelto de `main`.

El grupo se avisa por mail a diego.ambrossio@unab.edu.ar **y** angel.bianco@unab.edu.ar. Ver `GIT.md`.
