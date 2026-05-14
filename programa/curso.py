class Curso:
    def __init__(self, id_curso: str, nombre: str, tutor: str):
        self.id_curso = id_curso
        self.nombre = nombre
        self.tutor = tutor

    def mostrar_info(self):
        return f"{self.id_curso} - {self.nombre} | Tutor: {self.tutor}"

    def convertir_a_linea(self):
        return f"{self.id_curso}|{self.nombre}|{self.tutor}"

    @staticmethod
    def crear_desde_linea(linea: str):
        id_curso, nombre, tutor = linea.strip().split("|")
        return Curso(id_curso, nombre, tutor)

    @staticmethod
    def cargar_cursos(ruta="../datos/cursos.txt"):
        cursos = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    cursos.append(Curso.crear_desde_linea(linea))
        except FileNotFoundError:
            print("No existe el archivo de cursos.")
        return cursos
