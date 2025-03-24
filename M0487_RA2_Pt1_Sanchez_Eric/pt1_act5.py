musicat = []

musicat.append('La Fumiga')
musicat.append('The Tyets')
musicat.append('Ginestà')
print(f"Pas 2: {musicat}")

nou_grup1 = input("Nou grup: ")
nou_grup2 = input("Nou grup: ")
musicat.append(nou_grup1)
musicat.append(nou_grup2)
print(f"Pas 3: {musicat}")

del musicat[-1]
del musicat[-1]
print(f"Pas 4: {musicat}")

musicat.insert(0, 'La iaia')
print(f"Pas 5: {musicat}")
