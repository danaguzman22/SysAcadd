import unittest
import os
from flask import current_app
from app import create_app
from app.models import Autoridad, Cargo, Categoria, TipoDedicacion

class AutoridadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        self.__new_object(autoridad, cargo)

        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "abc@gmail.com")
        self.assertEqual(autoridad.facultad, "Facultad Regional San Rafael")

        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.cargo.puntos, "80")

        self.assertIsNotNone(autoridad.cargo.tipo_dedicacion)
        self.assertEqual(autoridad.cargo.tipo_dedicacion.nombre, "Tipo Dedicacion 1")
        self.assertEqual(autoridad.cargo.tipo_dedicacion.observaciones, "Observaciones 1")

        self.assertIsNotNone(autoridad.cargo.categoria_cargo)
        self.assertEqual(autoridad.cargo.categoria_cargo.nombre, "Categoria 1")

    def __new_object(self, autoridad, cargo):
        categoria = Categoria()
        categoria.nombre = "Categoria 1"

        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Tipo Dedicacion 1"
        tipo_dedicacion.observaciones = "Observaciones 1"

        cargo.nombre = "Decano"
        cargo.puntos = "80"
        cargo.categoria_cargo = categoria
        cargo.tipo_dedicacion = tipo_dedicacion

        autoridad.nombre = "Juan Perez"
        autoridad.telefono = "123456789"
        autoridad.email = "abc@gmail.com"
        autoridad.facultad = "Facultad Regional San Rafael"
        autoridad.cargo = cargo


if __name__ == "__main__":
    unittest.main()
