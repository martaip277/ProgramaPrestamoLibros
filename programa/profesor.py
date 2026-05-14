from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre:str, apellido:str, dni: str, especialidad: str):
        super().__init__(nombre, apellido, dni)
        self.especialidad = especialidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Especialidad: {self.especialidad}"

    def convertir_a_linea(self):
        return f"{self.nombre}|{self.apellido}|{self.dni}|{self.especialidad}"

    @staticmethod
    def crear_desde_linea(linea):
        nombre, apellido, dni, especialidad = linea.strip().split("|")
        return Profesor(nombre, apellido, dni, especialidad)

    @staticmethod
    def cargar_profesores(ruta="../datos/profesores.txt"):
        profesores = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    profesores.append(Profesor.crear_desde_linea(linea))
        except FileNotFoundError:
            print("No existe el archivo de profesores. Se creará cuando guardes uno.")
        return profesores

    def guardar_en_archivo(self, ruta="../datos/profesores.txt"):
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(self.convertir_a_linea() + "\n")
