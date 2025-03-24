n = int(input("Introdueix l'últim nombre natural per realitzar la suma aritmètica: "))

suma = 0 

for i in range(1, n + 1):
    suma += i 

print(f"La suma aritmètica de {n} és {suma}")
