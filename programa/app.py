from profesor import Profesor
from alumno import Alumno

a = Alumno("Ana", "García", "12345678A", "1A")
a.guardar_en_archivo()

print("Alumnos guardados:")
lista = Alumno.cargar_alumnos()
for alu in lista:
    print(alu.mostrar_info())


# Guardar un profesor
p = Profesor("Luis", "Martínez", "11223344B", "Matemáticas")
p.guardar_en_archivo()

# Leer todos los profesores
print("Profesores guardados:")
lista = Profesor.cargar_profesores()
for prof in lista:
    print(prof.mostrar_info())

