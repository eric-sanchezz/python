import sqlite3

def crear_base_dades():
    conn = sqlite3.connect("grups.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS grups (
                 nom TEXT PRIMARY KEY,
                 any_inici INTEGER,
                 tipus TEXT,
                 membres INTEGER)''')
    conn.commit()
    conn.close()

def afegir_grup(nom, any_inici, tipus, membres):
    try:
        conn = sqlite3.connect("grups.db")
        c = conn.cursor()
        c.execute("INSERT INTO grups VALUES (?, ?, ?, ?)", (nom, any_inici, tipus, membres))
        conn.commit()
    except sqlite3.IntegrityError:
        print("El grup ja existeix.")
    finally:
        conn.close()

def mostrar_grups():
    conn = sqlite3.connect("grups.db")
    c = conn.cursor()
    for fila in c.execute("SELECT * FROM grups"):
        print(fila)
    conn.close()

def eliminar_grup(nom):
    conn = sqlite3.connect("grups.db")
    c = conn.cursor()
    c.execute("DELETE FROM grups WHERE nom = ?", (nom,))
    conn.commit()
    conn.close()

def actualitzar_grup(nom, any_inici=None, tipus=None, membres=None):
    conn = sqlite3.connect("grups.db")
    c = conn.cursor()
    if any_inici:
        c.execute("UPDATE grups SET any_inici = ? WHERE nom = ?", (any_inici, nom))
    if tipus:
        c.execute("UPDATE grups SET tipus = ? WHERE nom = ?", (tipus, nom))
    if membres:
        c.execute("UPDATE grups SET membres = ? WHERE nom = ?", (membres, nom))
    conn.commit()
    conn.close()
