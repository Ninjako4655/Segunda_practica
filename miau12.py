secreto = 7
intentos = 0
while intentos < 3:
    respuesta = int(input("Adivina el número del 1 al 10: "))
    intentos += 1
    if respuesta == secreto:
        print("¡Acertaste!")
        break
    else:
        if respuesta < secreto:
            print("Muy bajo")
        else:
            print("Muy alto")