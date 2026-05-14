class Materia:
    def __init__(self, id_materia: str, nombre: str, horas: str):
        self.id_materia = id_materia
        self.nombre = nombre
        self.horas = horas

    def mostrar_info(self):
        return f"{self.id_materia} - {self.nombre} ({self.horas} horas)"

    def convertir_a_linea(self):
        return f"{self.id_materia}|{self.nombre}|{self.horas}"

    @staticmethod
    def crear_desde_linea(linea: str):
        id_materia, nombre, horas = linea.strip().split("|")
        return Materia(id_materia, nombre, horas)

    @staticmethod
    def cargar_materias(ruta="../datos/materias.txt"):
        materias = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    materias.append(Materia.crear_desde_linea(linea))
        except FileNotFoundError:
            print("No existe el archivo de materias.")
        return materias
