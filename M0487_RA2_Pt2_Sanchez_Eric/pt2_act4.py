def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplica(a, b): return a * b
def divideix(a, b): return a / b if b != 0 else "Error: Divisió per zero"

def calculadora():
    while True:
        print("\n1. Suma\n2. Resta\n3. Multiplicació\n4. Divisió\n0. Sortir")
        opcio = input("Escull una opció: ")
        
        if opcio == "0":
            break
        
        try:
            a = float(input("Introdueix el primer nombre: "))
            b = float(input("Introdueix el segon nombre: "))
            operacions = {"1": suma, "2": resta, "3": multiplica, "4": divideix}
            print("Resultat:", operacions[opcio](a, b) if opcio in operacions else "Opció no vàlida")
        except ValueError:
            print("Error: Entrada no vàlida")

calculadora()
