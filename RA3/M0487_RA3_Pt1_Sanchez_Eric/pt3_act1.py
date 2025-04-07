def obtenir_numero(missatge):
    while True:
        try:
            return float(input(missatge))
        except ValueError:
            print("Error: Has d'introduir un número vàlid.")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No es pot dividir per zero.")
        return None

def mostrar_menu():
    print("\nMenú:")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("0) Sortir")

def calcular():
    while True:
        mostrar_menu()
        opcio = input("Escull una opció: ")

        if opcio == "0":
            print("Sortint del programa.")
            break

        if opcio not in ("1", "2", "3", "4"):
            print("Opció no vàlida! Torna-ho a intentar.")
            continue

        num1 = obtenir_numero("Introdueix el primer número: ")
        num2 = obtenir_numero("Introdueix el segon número: ")

        operacions = {"1": sumar, "2": restar, "3": multiplicar, "4": dividir}
        resultat = operacions[opcio](num1, num2)

        if resultat is not None:
            print(f"Resultat: {resultat}")

if __name__ == "__main__":
    calcular()
