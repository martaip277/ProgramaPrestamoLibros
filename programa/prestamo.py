class Prestamo:
    def __init__(self, dni_alumno: str, id_libro: str, fecha_prestamo: str, fecha_devolucion: str):
        self.dni_alumno = dni_alumno
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return f"{self.dni_alumno} | Libro: {self.id_libro} | {self.fecha_prestamo} → {self.fecha_devolucion}"

    def convertir_a_linea(self):
        return f"{self.dni_alumno}|{self.id_libro}|{self.fecha_prestamo}|{self.fecha_devolucion}"

    @staticmethod
    def crear_desde_linea(linea: str):
        dni_alumno, id_libro, fecha_prestamo, fecha_devolucion = linea.strip().split("|")
        return Prestamo(dni_alumno, id_libro, fecha_prestamo, fecha_devolucion)

    @staticmethod
    def cargar_prestamos(ruta="../datos/prestamos.txt"):
        prestamos = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    prestamos.append(Prestamo.crear_desde_linea(linea))
        except FileNotFoundError:
            print("No existe el archivo de préstamos.")
        return prestamos

    def guardar_en_archivo(self, ruta="../datos/prestamos.txt"):
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(self.convertir_a_linea() + "\n")
