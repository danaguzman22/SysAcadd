import unittest
from flask import current_app
from app import create_app
from app.models import Facultad, Universidad
import os

class FacultadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_facultad_creation(self):
        facultad=Facultad()
        facultad.universidad=Universidad()
        facultad.nombre = "Facultad Regional San Rafael"
        facultad.universidad.nombre = "Universidad Tecnológica Nacional"
        facultad.directorio = "Ciencias Exactas"
        facultad.universidad.sigla = "UTN"
        facultad.abreviatura = "FRSR"
        facultad.codigoPostal = "12345"
        facultad.ciudad = "San Rafael"
        facultad.domicilio = "Urquiza 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Juan Perez"
        facultad.email ="abc@gmail.com"
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, "Facultad Regional San Rafael")
        self.assertEqual(facultad.universidad.nombre, "Universidad Tecnológica Nacional")
        self.assertEqual(facultad.universidad.sigla, "UTN")

if __name__ == '__main__':
    unittest.main()
