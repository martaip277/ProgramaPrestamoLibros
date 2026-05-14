from profesor import Profesor

def menu_profesores():
    while True:
        print("\n--- GESTIÓN DE PROFESORES ---")
        print("1. Mostrar profesores")
        print("2. Añadir profesor")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_profesores()
        elif opcion == "2":
            anadir_profesor()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

def mostrar_profesores():
    profesores = Profesor.cargar_profesores()
    if not profesores:
        print("No hay profesores registrados.")
    else:
        print("\n--- PROFESORES REGISTRADOS ---")
        for p in profesores:
            print(p.mostrar_info())

def anadir_profesor():
    print("\n--- AÑADIR PROFESOR ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    departamento = input("Departamento: ")

    nuevo = Profesor(nombre, apellido, dni, departamento)
    nuevo.guardar_en_archivo()
    print("Profesor guardado correctamente.")
