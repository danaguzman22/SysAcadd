import unittest
from flask import current_app
from app import create_app
from app.models import Especialidad, TipoEspecialidad
import os

class EspecialidadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_especialidad_creation(self):
        especialidad = Especialidad ()
        especialidad.nombre = "Ingenieria de Software"
        especialidad.letra = "S"
        especialidad.observaciones = "carrera orientada a la ingenieria"
        especialidad.tipo_especialidad = "Ingenieria"
        self.assertIsNotNone(especialidad)
        self.assertEqual(especialidad.nombre, "Ingenieria de Software")
        self.assertEqual(especialidad.tipo_especialidad, "Ingenieria")
        self.assertEqual(especialidad.letra, "S")
    
    def test_tipo_especialidad_creation(self):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = "Ingenieria"
        tipo_especialidad.nivel = "Superior"
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, "Ingenieria")
        self.assertEqual(tipo_especialidad.nivel, "Superior")

if __name__ == '__main__':
    unittest.main()