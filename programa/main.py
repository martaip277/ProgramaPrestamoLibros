from login import login
from gestion_alumno import menu_alumnos
from gestion_libro import menu_libros
from gestion_prestamo import menu_prestamos


def menu_principal():
    while True:
        print("\n-MENÚ PRINCIPAL-")
        print("1. Gestión de alumnos")
        print("2. Gestión de libros")
        print("3. Gestión de préstamos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_alumnos()

        elif opcion == "2":
            menu_libros()


        elif opcion == "3":
            menu_prestamos()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    if login():
        menu_principal()