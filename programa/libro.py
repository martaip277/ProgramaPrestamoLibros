class Libro:
    def __init__(self, id_libro: str, titulo: str, autor: str, ejemplares: str):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

    def mostrar_info(self):
        return f"{self.id_libro} - {self.titulo} ({self.autor}) | Ejemplares: {self.ejemplares}"

    def convertir_a_linea(self):
        return f"{self.id_libro}|{self.titulo}|{self.autor}|{self.ejemplares}"

    @staticmethod
    def crear_desde_linea(linea: str):
        id_libro, titulo, autor, ejemplares = linea.strip().split("|")
        return Libro(id_libro, titulo, autor, ejemplares)

    @staticmethod
    def cargar_libros(ruta="../datos/libros.txt"):
        libros = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    libros.append(Libro.crear_desde_linea(linea))
        except FileNotFoundError:
            print("No existe el archivo de libros.")
        return libros
