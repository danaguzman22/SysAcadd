import unittest
import os
from flask import current_app
from app import create_app
from app.models import Categoria, Cargo, TipoDedicacion

class CargoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_cargo_creation(self):
        cargo = Cargo()
        cargo.nombre = "Decano"
        cargo.puntos = "80"
        cargo.categoria_cargo = self.build_categoria()
        cargo.tipo_dedicacion = self.build_tipo_dedicacion()

        self.assertIsNotNone(cargo)
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, "80")
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertIsNotNone(cargo.tipo_dedicacion)
        self.assertEqual(cargo.tipo_dedicacion.nombre, "Tipo Dedicacion 1")
        self.assertEqual(cargo.tipo_dedicacion.observaciones, "Observaciones 1")

    def test_categoria_creation(self):
        categoria = self.build_categoria()
        self.assertIsNotNone(categoria)
        self.assertEqual(categoria.nombre, "Categoria 1")

    def test_tipo_dedicacion_creation(self):
        tipo_dedicacion = self.build_tipo_dedicacion()
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Tipo Dedicacion 1")
        self.assertEqual(tipo_dedicacion.observaciones, "Observaciones 1")

    def build_tipo_dedicacion(self):
        tipo = TipoDedicacion()
        tipo.nombre = "Tipo Dedicacion 1"
        tipo.observaciones = "Observaciones 1"
        return tipo

    def build_categoria(self):
        categoria = Categoria()
        categoria.nombre = "Categoria 1"
        return categoria

if __name__ == '__main__':
    unittest.main()
