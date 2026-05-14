def cargar_usuarios():
    usuarios = {}
    with open("../datos/usuarios.txt", "r", encoding="utf-8") as f:
        for linea in f:
            nombre, password = linea.strip().split("|")
            usuarios[nombre] = password
    return usuarios


def login():
    print("Inicio de sesión")
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    usuarios = cargar_usuarios()

    if usuario in usuarios and usuarios[usuario] == password:
        print("Acceso permitido")
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False

