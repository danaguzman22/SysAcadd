import unittest
from flask import current_app
from app import create_app
from app.models import Alumno
import os

class AlumnoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_alumno_creation(self):
        alumno=Alumno()
        alumno.apellido = "Guzman"
        alumno.nombre = "Dana"
        alumno.nroDocumento = "12345678"
        alumno.tipoDocumento = "DNI"
        alumno.fechaNacimiento = "0000-00-00"
        alumno.sexo = "F"
        alumno.nroLegajo = "123456"
        alumno.fechaIngreso = "0000-00-00"
        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.nombre, "Dana")
        self.assertEqual(alumno.nroDocumento, "12345678")
        self.assertEqual(alumno.nroLegajo, "123456")

if __name__ == '__main__':
    unittest.main()
