suma = 0
 
for i in range(3):
    nota = float(input("Ingresa una nota: "))
    suma += nota
 
promedio = suma / 3
print("Tu promedio es:", promedio)
 
if promedio >= 3:
    print("Aprobaste")
else:
    print("Reprobaste")