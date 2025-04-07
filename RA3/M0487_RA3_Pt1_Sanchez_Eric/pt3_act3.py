import os

def comptar_lletres(text):
    return sum(1 for c in text if c.isalpha())

def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as fo:
            return fo.read()
    except FileNotFoundError:
        print("Error: El fitxer no existeix.")
        return None

def mostrar_menu():
    print("\nMenú:")
    print("1) Comptar línies")
    print("2) Comptar paraules")
    print("3) Comptar lletres")
    print("0) Sortir")

def analitzar_fitxer(nom_fitxer):

    contingut = llegir_fitxer(nom_fitxer)
    if contingut is None:
        return

    print(f"\nContingut del fitxer {nom_fitxer}:")
    print(contingut)

    while True:
        mostrar_menu()
        opcio = input("Escull una opció: ")

        if opcio == "0":
            print("Sortint del programa.")
            break
        elif opcio == "1":
            print(f"Nombre de línies: {len(contingut.splitlines())}")
        elif opcio == "2":
            print(f"Nombre de paraules: {len(contingut.split())}")
        elif opcio == "3":
            print(f"Nombre de lletres: {comptar_lletres(contingut)}")
        else:
            print("Opció no vàlida! Torna-ho a intentar.")

if __name__ == "__main__":
    nom_fitxer = input("Introdueix el nom del fitxer a analitzar: ")
    analitzar_fitxer(nom_fitxer)
