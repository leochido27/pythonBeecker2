from Users import User
#seccion de variables
list_usuarios = []
try:
    
    obj = User()

except Exception as e :
    print("no se encontro la clase")

while True:
    print("Plataforma de usuarios ")
    print("1.- Agregar usuario ")
    print("2.- Eliminar Usuarios ")
    print("3.- Actualizar Usuarios ")
    print("4.- Mostrar datos ")
    print("5.- salir")

    opciones_menu=int(input("introduce una opcion: "))

    if opciones_menu == 1:
        print("Agregar Usuarios")
        ValorUsuario= input("Introduce el nombre: ")
        list_usuarios.append(obj.get_name(in_name=ValorUsuario))
        print(list_usuarios)

    elif opciones_menu == 2:
        print("Eliminar Usuarios")
        try :
            to_remove_name=input("Ingresa el usuario a eliminar: ")
            list_usuarios.remove(to_remove_name)
            list_usuarios.sort()
            print (list_usuarios)
            print("Eliminado.")
        except Exception as notfound:
            print("el usuario no existe")

    elif opciones_menu == 3:
        print("Actualizar Usuarios")
        print (list_usuarios)
        valor_id = input("que valor deseas actualizar? ")
        
        valor_id_index = list_usuarios.index(valor_id)

        actualizado = input("ingresa la actualizacion: ")

        list_usuarios.insert(valor_id_index,actualizado)

        list_usuarios.remove(valor_id)

        print("actualizado.. ")

    elif opciones_menu == 3:
        print("Mostrar datos")
        print(list_usuarios)

    else:
        print("Saliendo..")
        break

