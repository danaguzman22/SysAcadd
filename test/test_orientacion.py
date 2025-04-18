import unittest
from flask import current_app
from app import create_app
from app.models import Orientacion
import os

class OrientacionTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_orientacion_creation(self):
        orientacion = Orientacion ()
        orientacion.nombre = "Materias Basicas"
        self.assertIsNotNone(orientacion)
        self.assertEqual(orientacion.nombre, "Materias Basicas")


if __name__ == '__main__':
    unittest.main()