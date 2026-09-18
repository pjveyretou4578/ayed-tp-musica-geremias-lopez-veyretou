class Cancion:

    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg, version_de):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg
        self.version_de = version_de


catalogo = [

    Cancion(1, "De Musica Ligera", "Soda Stereo",
            "Cancion Animal", "Rock", 1990, 213, None),

    Cancion(2, "Persiana Americana", "Soda Stereo",
            "Signos", "Rock", 1986, 263, None),

    Cancion(3, "En la Ciudad de la Furia", "Soda Stereo",
            "Doble Vida", "Rock", 1988, 351, None),

    Cancion(4, "Crimen", "Gustavo Cerati",
            "Ahi Vamos", "Rock", 2006, 239, None),

    Cancion(5, "Adios", "Gustavo Cerati",
            "Fuerza Natural", "Rock", 2009, 233, None),

    Cancion(6, "Muchacha ojos de papel", "Luis Alberto Spinetta",
            "Almendra", "Rock", 1969, 203, None),

    Cancion(7, "Cantata de Puentes Amarillos", "Luis Alberto Spinetta",
            "Artaud", "Rock", 1973, 557, None),

    Cancion(8, "Rasguna las Piedras", "Sui Generis",
            "Confesiones de Invierno", "Rock", 1973, 196, None),

    Cancion(9, "Seminare", "Seru Giran",
            "La Grasa de las Capitales", "Rock", 1979, 241, None),

    Cancion(10, "Los Dinosaurios", "Charly Garcia",
            "Clics Modernos", "Rock", 1983, 241, None),

    Cancion(11, "Demoliendo Hoteles", "Charly Garcia",
            "Piano Bar", "Rock", 1984, 151, None),

    Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota",
            "Un Baion para el Ojo Idiota", "Rock", 1988, 316, None),

    Cancion(13, "Ji Ji Ji", "Patricio Rey y sus Redonditos de Ricota",
            "En Directo", "Rock", 1992, 318, 12),

    Cancion(14, "La Bestia Pop", "Patricio Rey y sus Redonditos de Ricota",
            "Octubre", "Rock", 1986, 240, None),

    Cancion(15, "Alfonsina y el mar", "Mercedes Sosa",
            "Mujeres Argentinas", "Folklore", 1969, 298, None),

    Cancion(16, "Gracias a la Vida", "Mercedes Sosa",
            "Hasta la Victoria", "Folklore", 1971, 271, 61),

    Cancion(17, "La Balsa", "Los Gatos",
            "Los Gatos", "Rock", 1967, 187, None),

    Cancion(18, "El Extrano de Pelo Largo", "Almendra",
            "Almendra", "Rock", 1969, 198, None),

    Cancion(19, "Flaca", "Andres Calamaro",
            "Honestidad Brutal", "Rock", 1999, 263, None),

    Cancion(20, "Lamento Boliviano", "Los Enanitos Verdes",
            "Big Bang", "Rock", 1994, 223, None),

    Cancion(21, "La Guitarra", "Los Autenticos Decadentes",
            "Mi enfermedad", "Cumbia", 1997, 201, None),

    Cancion(22, "Waka Waka", "Shakira",
            "Sale el Sol", "Pop", 2010, 202, None),

    Cancion(23, "Bzrp Music Sessions Vol. 52", "Bizarrap",
            "Sessions", "Urbano", 2022, 201, None),

    Cancion(24, "Bzrp Music Sessions Vol. 53", "Bizarrap",
            "Sessions", "Urbano", 2023, 194, None),

    Cancion(25, "Natacha", "Wos",
            "Oscuro Extasis", "Urbano", 2019, 183, None),

    Cancion(26, "Canguro", "Wos",
            "Tres Puntos Suspensivos", "Urbano", 2021, 176, None),

    Cancion(27, "Buenos Aires", "Nathy Peluso",
            "Calambre", "Urbano", 2020, 198, None),

    Cancion(28, "Despecha", "Rosalia",
            "Motomami", "Pop", 2022, 157, None),

    Cancion(29, "Titi Me Pregunto", "Bad Bunny",
            "Un Verano Sin Ti", "Urbano", 2022, 243, None),

    Cancion(30, "Anti-Hero", "Taylor Swift",
            "Midnights", "Pop", 2022, 201, None),

    Cancion(31, "Blank Space", "Taylor Swift",
            "1989", "Pop", 2014, 231, None),

    Cancion(32, "Bohemian Rhapsody", "Queen",
            "A Night at the Opera", "Rock", 1975, 354, None),

    Cancion(33, "Bohemian Rhapsody (Live Aid)", "Queen",
            "Live Aid", "Rock", 1985, 362, 32),

    Cancion(34, "Don't Stop Me Now", "Queen",
            "Jazz", "Rock", 1978, 209, None),

    Cancion(35, "Come Together", "The Beatles",
            "Abbey Road", "Rock", 1969, 259, None),

    Cancion(36, "Here Comes the Sun", "The Beatles",
            "Abbey Road", "Rock", 1969, 185, None),

    Cancion(37, "Get Lucky", "Daft Punk",
            "Random Access Memories", "Electronica", 2013, 248, None),

    Cancion(38, "One More Time", "Daft Punk",
            "Discovery", "Electronica", 2000, 320, None),

    Cancion(39, "Rolling in the Deep", "Adele",
            "21", "Pop", 2010, 228, None),

    Cancion(40, "Someone Like You", "Adele",
            "21", "Pop", 2011, 285, None),

    Cancion(41, "Do I Wanna Know?", "Arctic Monkeys",
            "AM", "Rock", 2013, 272, None),

    Cancion(42, "505", "Arctic Monkeys",
            "Favourite Worst Nightmare", "Rock", 2007, 214, None),

    Cancion(43, "Blinding Lights", "The Weeknd",
            "After Hours", "Pop", 2019, 200, None),

    Cancion(44, "Levitating", "Dua Lipa",
            "Future Nostalgia", "Pop", 2020, 203, None),

    Cancion(45, "As It Was", "Harry Styles",
            "Harry's House", "Pop", 2022, 167, None),

    Cancion(46, "Smells Like Teen Spirit", "Nirvana",
            "Nevermind", "Rock", 1991, 301, None),

    Cancion(47, "Wonderwall", "Oasis",
            "What's the Story Morning Glory", "Rock", 1995, 258, None),

    Cancion(48, "Wonderwall (Live)", "Oasis",
            "Familiar to Millions", "Rock", 2000, 265, 47),

    Cancion(49, "Take On Me", "a-ha",
            "Hunting High and Low", "Pop", 1985, 225, None),

    Cancion(50, "Africa", "Toto",
            "Toto IV", "Pop", 1982, 296, None),

    Cancion(51, "Billie Jean", "Michael Jackson",
            "Thriller", "Pop", 1982, 294, None),

    Cancion(52, "Billie Jean (Remix)", "Michael Jackson",
            "Thriller 40", "Pop", 2022, 292, 51),

    Cancion(53, "Clocks", "Coldplay",
            "A Rush of Blood to the Head", "Rock", 2002, 307, None),

    Cancion(54, "Yellow", "Coldplay",
            "Parachutes", "Rock", 2000, 269, None),

    Cancion(55, "Creep", "Radiohead",
            "Pablo Honey", "Rock", 1992, 238, None),

    Cancion(56, "Karma Police", "Radiohead",
            "OK Computer", "Rock", 1997, 261, None),

    Cancion(57, "Vasos Vacios", "Los Abuelos de la Nada",
            "Vasos y Besos", "Rock", 1983, 214, None),

    Cancion(58, "Lunes Por La Madrugada", "Los Abuelos de la Nada",
            "Los Abuelos de la Nada", "Rock", 1982, 241, None),

    Cancion(59, "El Aguante", "Divididos",
            "Gol de Mujer", "Rock", 1998, 245, None),

    Cancion(60, "Que Ves", "Divididos",
            "Acariciando lo Aspero", "Rock", 1991, 232, None),

    Cancion(61, "Gracias a la Vida", "Violeta Parra",
            "Las Ultimas Composiciones", "Folklore", 1966, 258, None),

    Cancion(62, "De Musica Ligera (Unplugged)", "Soda Stereo",
            "Comfort y Musica Para Volar", "Rock", 1996, 221, 1),

    Cancion(63, "Flaca (Live)", "Andres Calamaro",
            "Vivo", "Rock", 2000, 270, 19),

    Cancion(64, "Creep (Live)", "Radiohead",
            "The Astoria London", "Rock", 1994, 245, 55),

    Cancion(65, "Yellow (Live)", "Coldplay",
            "Live 2003", "Rock", 2003, 280, 54),

    Cancion(66, "Blank Space (Acoustic)", "Taylor Swift",
            "1989", "Pop", 2014, 228, 31),

    Cancion(67, "Get Lucky (Remix)", "Daft Punk",
            "Random Access Memories", "Electronica", 2013, 248, 37),

    # Canciones agregadas por el grupo para disponer
    # de un ejemplo con ramificaciones y versiones de versiones.

    Cancion(68, "Hallelujah", "Leonard Cohen",
            "Various Positions", "Folk Rock", 1984, 279, None),

    Cancion(69, "Hallelujah", "John Cale",
            "I'm Your Fan", "Rock", 1991, 246, 68),

    Cancion(70, "Hallelujah", "Jeff Buckley",
            "Grace", "Alternative Rock", 1994, 413, 69),

    Cancion(71, "Hallelujah", "Pentatonix",
            "A Pentatonix Christmas", "A cappella", 2016, 268, 68)
]

