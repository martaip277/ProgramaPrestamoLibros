from persona import Persona


class Alumno(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, curso):
        super().__init__(nombre, apellido, dni)
        self.curso = curso

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Curso: {self.curso}"

    def convertir_a_linea(self):
        return f"{self.nombre}|{self.apellido}|{self.dni}|{self.curso}"

    @staticmethod
    def crear_desde_linea(linea):
        nombre, apellido, dni, curso = linea.strip().split("|")
        return Alumno(nombre, apellido, dni, curso)

    @staticmethod
    def cargar_alumnos(ruta="../datos/alumnos.txt"):
        alumnos = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    alumnos.append(Alumno.crear_desde_linea(linea))
        except FileNotFoundError:
            print("No existe el archivo de alumnos. Se creará cuando guardes uno.")
        return alumnos

    def guardar_en_archivo(self, ruta="../datos/alumnos.txt"):
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(self.convertir_a_linea() + "\n")
