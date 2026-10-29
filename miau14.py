opcion = ""

while opcion != "Salir" and opcion != "salir":
    opcion = input("Ingrese Hola o Salir: ")
    if opcion != "Hola" and opcion != "hola" and opcion != "Salir" and opcion != "salir":
        print("Opción no válida")
    else:
        if opcion == "Hola" or opcion == "hola":
            print("¡Hola, mucho gusto!")
        else:
            if opcion == "Salir" or opcion == "salir":
                print("¡Hasta luego!")
                break