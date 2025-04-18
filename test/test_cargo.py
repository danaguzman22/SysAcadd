import unittest
from flask import current_app
from app import create_app
from app.models import Categoria, Cargo, TipoDedicacion 
import os

class CargoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_cargo_creation(self):
        cargo = Cargo ()
        cargo.nombre = "Decano"
        cargo.puntos = "80"
        self.assertIsNotNone(cargo)
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos , "80")

    def test_categoria_creation(self):
        categoria = Categoria()
        categoria.nombre = "Categoria 1"
        self.assertIsNotNone(categoria)
        self.assertEqual(categoria.nombre, "Categoria 1")

    def test_tipo_dedicacion_creation(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Tipo Dedicacion 1"
        tipo_dedicacion.observaciones = "Observaciones 1"
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Tipo Dedicacion 1")
        self.assertEqual(tipo_dedicacion.observaciones, "Observaciones 1")

if __name__ == '__main__':
    unittest.main()
