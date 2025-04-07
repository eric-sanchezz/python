import math

def obtenir_numero(missatge, permet_negatius=True):
    while True:
        try:
            num = float(input(missatge))
            if not permet_negatius and num < 0:
                raise ValueError("No es pot calcular l'arrel quadrada d'un número negatiu.")
            return num
        except ValueError as e:
            print(f"Error: {e}")

def calcular():
    while True:
        print("\nMenú:")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Arrel quadrada")
        print("0) Sortir")

        opcio = input("Escull una opció: ")

        if opcio == "0":
            print("Sortint del programa.")
            break
        
        if opcio in ("1", "2", "3", "4"):
            num1 = obtenir_numero("Introdueix el primer número: ")
            num2 = obtenir_numero("Introdueix el segon número: ")

            try:
                if opcio == "1":
                    print(f"Resultat: {num1 + num2}")
                elif opcio == "2":
                    print(f"Resultat: {num1 - num2}")
                elif opcio == "3":
                    print(f"Resultat: {num1 * num2}")
                elif opcio == "4":
                    print(f"Resultat: {num1 / num2}")
            except ZeroDivisionError:
                print("Error: No es pot dividir per zero.")

        elif opcio == "5":
            num = obtenir_numero("Introdueix un número per calcular l'arrel quadrada: ", permet_negatius=False)
            try:
                resultat = math.sqrt(num)
            except ValueError:
                print("Error: No es pot calcular l'arrel quadrada d'un número negatiu.")
            else:
                print(f"Resultat: {resultat}")
            finally:
                print("Càlcul d'arrel quadrada finalitzat.")

        else:
            print("Opció no vàlida! Torna-ho a intentar.")

if __name__ == "__main__":
    calcular()
