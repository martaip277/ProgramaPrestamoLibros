from alumno import Alumno

def menu_alumnos():
    while True:
        print("\n--- GESTIÓN DE ALUMNOS ---")
        print("1. Mostrar alumnos")
        print("2. Añadir alumno")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_alumnos()
        elif opcion == "2":
            anadir_alumno()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")


def mostrar_alumnos():
    alumnos = Alumno.cargar_alumnos()
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        print("\n--- ALUMNOS REGISTRADOS ---")
        for a in alumnos:
            print(a.mostrar_info())

def anadir_alumno():
    print("\n--- AÑADIR ALUMNO ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    curso = input("Curso: ")

    nuevo = Alumno(nombre, apellido, dni, curso)
    nuevo.guardar_en_archivo()
    print("Alumno guardado correctamente.")
