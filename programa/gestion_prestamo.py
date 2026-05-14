from prestamo import Prestamo

def menu_prestamos():
    while True:
        print("\n--- GESTIÓN DE PRÉSTAMOS ---")
        print("1. Mostrar préstamos")
        print("2. Registrar préstamo")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_prestamos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

def mostrar_prestamos():
    prestamos = Prestamo.cargar_prestamos()
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        print("\n--- PRÉSTAMOS REGISTRADOS ---")
        for p in prestamos:
            print(p.mostrar_info())

def registrar_prestamo():
    print("\n--- REGISTRAR PRÉSTAMO ---")
    dni = input("Inserte DNI del alumno: ")
    id_libro = input("Inserte ID del libro: ")
    fecha_prestamo = input("Fecha de préstamo (dd/mm/aaaa): ")
    fecha_devolucion = input("Fecha de devolución (dd/mm/aaaa): ")

    nuevo = Prestamo(dni, id_libro, fecha_prestamo, fecha_devolucion)
    nuevo.guardar_en_archivo()
    print("Préstamo registrado correctamente.")
