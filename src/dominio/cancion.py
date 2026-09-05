CATALOGO = [
    {
        "id": 1,
        "titulo": "De Musica Ligera",
        "artista": "Soda Stereo",
        "album": "Cancion Animal",
        "genero": "Rock",
        "anio": 1990,
        "duracion_seg": 213
    },
    {
        "id": 62,
        "titulo": "De Musica Ligera (Unplugged)",
        "artista": "Soda Stereo",
        "album": "Comfort y Musica Para Volar",
        "genero": "Rock",
        "anio": 1996,
        "duracion_seg": 221
    },
    {
        "id": 32,
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "album": "A Night at the Opera",
        "genero": "Rock",
        "anio": 1975,
        "duracion_seg": 354
    },
    {
        "id": 33,
        "titulo": "Bohemian Rhapsody (Live Aid)",
        "artista": "Queen",
        "album": "Live Aid",
        "genero": "Rock",
        "anio": 1985,
        "duracion_seg": 362
    },
    {
        "id": 47,
        "titulo": "Wonderwall",
        "artista": "Oasis",
        "album": "What's the Story Morning Glory",
        "genero": "Rock",
        "anio": 1995,
        "duracion_seg": 258
    },
    {
        "id": 48,
        "titulo": "Wonderwall (Live)",
        "artista": "Oasis",
        "album": "Familiar to Millions",
        "genero": "Rock",
        "anio": 2000,
        "duracion_seg": 265
    },
    {
        "id": 51,
        "titulo": "Billie Jean",
        "artista": "Michael Jackson",
        "album": "Thriller",
        "genero": "Pop",
        "anio": 1982,
        "duracion_seg": 294
    },
    {
        "id": 52,
        "titulo": "Billie Jean (Remix)",
        "artista": "Michael Jackson",
        "album": "Thriller 40",
        "genero": "Pop",
        "anio": 2022,
        "duracion_seg": 292
    },
    {
        "id": 55,
        "titulo": "Creep",
        "artista": "Radiohead",
        "album": "Pablo Honey",
        "genero": "Rock",
        "anio": 1992,
        "duracion_seg": 238
    },
    {
        "id": 64,
        "titulo": "Creep (Live)",
        "artista": "Radiohead",
        "album": "The Astoria London",
        "genero": "Rock",
        "anio": 1994,
        "duracion_seg": 245
    },
]

def listar_catalogo():
    for  cancion in CATALOGO:
        print(cancion["id"],"-", cancion["titulo"],"-", cancion["artista"])

    