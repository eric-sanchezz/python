import math

def potencia(a, b): return a ** b
def arrel_quadrada(a): return math.sqrt(a) if a >= 0 else "Error: Nombre negatiu"
def modul(a): return abs(a)

def calculadora():
    while True:
        print("\n1. Potència\n2. Arrel quadrada\n3. Mòdul\n0. Sortir")
        opcio = input("Escull una opció: ")
        
        if opcio == "0":
            break
        
        try:
            if opcio == "2":
                a = float(input("Introdueix un nombre: "))
                print("Resultat:", arrel_quadrada(a))
            else:
                a = float(input("Introdueix el primer nombre: "))
                b = float(input("Introdueix el segon nombre: ")) if opcio == "1" else None
                operacions = {"1": potencia, "3": modul}
                print("Resultat:", operacions[opcio](a, b) if opcio in operacions else "Opció no vàlida")
        except ValueError:
            print("Error: Entrada no vàlida")

calculadora()
