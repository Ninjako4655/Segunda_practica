suma = 0
nota = 0
cantidad = 0
while nota != -1 and nota < 6:
    nota = int(input("Ingrese una nota (-1 para salir): "))
    suma += nota
    cantidad += 1
    continue
if suma < 1:
    print("No se ingresaron notas válidas.")
else: 
    if nota == -1:
        suma += 1
        cantidad -= 1
        suma = suma/cantidad
        print("La suma es:", suma)