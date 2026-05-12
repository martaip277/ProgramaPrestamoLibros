from login import login
from alumnos import mostrar_alumnos

def menu_principal():
    while True:
        print("\n-MENÚ PRINCIPAL-")
        print("1. Gestión de alumnos")
        print("2. Gestión de libros")
        print("3. Gestión de préstamos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Has elegido gestión de alumnos")
        elif opcion == "2":
            print("Has elegido gestión de libros")
        elif opcion == "3":
            print("Has elegido gestión de préstamos")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    if login():
        menu_principal()


