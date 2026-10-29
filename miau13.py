palabra= str(input("Ingrese una palabra: "))
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
for letra in palabra:
    if letra in vocales:
        count = palabra.count(letra)
        print(f"La letra '{letra}' aparece {count} veces en la palabra.")
        total = sum(palabra.count(v) for v in vocales)
print(f"En total tiene {total} vocales.")