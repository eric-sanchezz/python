km=1

while km!=0:
    km = float(input("Escriu els kilòmetres --> "))
    if km == 0:
        print("Fins la pròxima!")
        break
    milles = km * 0.6214
    print(f"{km} Km són {milles:.2f} mi")