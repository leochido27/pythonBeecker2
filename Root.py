from Users import User
#seccion de variables
list_usuarios = []
obj = User()

while True:
    print("Plataforma de usuarios ")
    print("1.- Agregar usuario ")
    print("2.- Eliminar Usuarios ")
    print("3.- Actualizar Usuarios ")
    print("4.- salir")

    opciones_menu=int(input("introduce una opcion: "))

    if opciones_menu == 1:
        print("Agregar Usuarios")
        ValorUsuario= input("Introduce el nombre: ")
        list_usuarios.append(obj.get_name(in_name=ValorUsuario))
        print(list_usuarios)
    elif opciones_menu == 1:
        print("Eliminar Usuarios")

    elif opciones_menu == 1:
        print("Actualizar Usuarios")

    else:
        print("Saliendo..")
        break

