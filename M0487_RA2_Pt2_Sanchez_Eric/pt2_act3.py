import string

def format_string(text, option):
    if option == "1":
        return text.upper()
    elif option == "2":
        return text.lower()
    elif option == "3":
        return text.capitalize()
    return None

while True:
    text = input("Introdueix un text: ")
    print("1. Majúscules\n2. Minúscules\n3. Només primera majúscula\n0. Sortir")
    opcio = input("Escull una opció: ")
    
    if opcio == "0":
        break
    
    resultat = format_string(text, opcio)
    if resultat:
        print("Resultat:", resultat)
