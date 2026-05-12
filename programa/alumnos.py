def mostrar_alumnos():
    print("\n LISTA DE ALUMNOS")

    try:
        with open("datos/alumnos.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if not lineas:
            print("No hay alumnos registrados.")
            return

        for linea in lineas:
            print("-", linea.strip())

    except FileNotFoundError:
        print("El archivo alumnos.txt no existe.")
