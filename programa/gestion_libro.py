from libro import Libro


def menu_libros():
    while True:
        print("\n--- GESTIÓN DE LIBROS ---")
        print("1. Mostrar libros")
        print("2. Añadir libro")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_libros()
        elif opcion == "2":
            anadir_libro()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")


def mostrar_libros():
    libros = Libro.cargar_libros()
    if not libros:
        print("No hay libros registrados.")
    else:
        print("\n--- LIBROS REGISTRADOS ---")
        for l in libros:
            print(l.mostrar_info())


def anadir_libro():
    print("\n--- AÑADIR LIBRO ---")
    id_libro = input("ID del libro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ejemplares = input("Número de ejemplares: ")

    nuevo = Libro(id_libro, titulo, autor, ejemplares)
    nuevo.guardar_en_archivo()
    print("Libro guardado correctamente.")
