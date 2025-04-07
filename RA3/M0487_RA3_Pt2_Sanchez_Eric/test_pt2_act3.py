import unittest
import sqlite3
from pt2_act3 import crear_base_dades, afegir_grup, eliminar_grup, actualitzar_grup

class TestGrupsMusicals(unittest.TestCase):

    def setUp(self):
        crear_base_dades()
        afegir_grup("Txarango", 2010, "Pop", 6)

    def tearDown(self):
        conn = sqlite3.connect("grups.db")
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS grups")
        conn.commit()
        conn.close()

    def test_eliminar_grup(self):
        eliminar_grup("Txarango")
        conn = sqlite3.connect("grups.db")
        c = conn.cursor()
        c.execute("SELECT * FROM grups WHERE nom = 'Txarango'")
        self.assertIsNone(c.fetchone())
        conn.close()

    def test_actualitzar_grup(self):
        actualitzar_grup("Txarango", membres=4)
        conn = sqlite3.connect("grups.db")
        c = conn.cursor()
        c.execute("SELECT membres FROM grups WHERE nom = 'Txarango'")
        self.assertEqual(c.fetchone()[0], 4)
        conn.close()

if __name__ == '__main__':
    unittest.main()
