import unittest
from flask import current_app
from app import create_app
from app.models import Persona, TipoDocumento
import os

class PersonaTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()


    def test_persona_creation(self):
        persona=Persona()
        persona.apellido = "Guzman"
        persona.nombre = "Dana"
        persona.nroDocumento = "12345678"
        persona.tipoDocumento = "DNI"
        persona.fechaNacimiento = "0000-00-00"
        persona.sexo = "F"
        self.assertIsNotNone(persona)
        self.assertEqual(persona.nombre, "Dana")
        self.assertEqual(persona.nroDocumento, "12345678")
        self.assertEqual(persona.tipoDocumento, "DNI")

    def test_tipo_documento(self):
        t_documento=TipoDocumento()
        t_documento.tipoDocumento = "DNI"
        self.assertEqual(t_documento.tipoDocumento, "DNI")


if __name__ == '__main__':
    unittest.main()
