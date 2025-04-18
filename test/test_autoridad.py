import unittest
from flask import current_app
from app import create_app
from app.models import Autoridad 
import os

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
        autoridad.nombre = "Juan Perez"
        autoridad.cargo = "Decano"
        autoridad.telefono = "123456789"
        autoridad.email = ""
        autoridad.facultad = "Facultad Regional San Rafael"
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertEqual(autoridad.cargo, "Decano")
        self.assertEqual(autoridad.facultad, "Facultad Regional San Rafael")


if __name__ == '__main__':
    unittest.main()
