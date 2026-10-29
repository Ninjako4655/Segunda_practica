puntos = [10, -5, 20, -3, 15]
total = 0
 
for p in puntos:
    if p < 0:
        continue
    print("Puntos ganados:", p)
    total += p
 
print("Total:", total)