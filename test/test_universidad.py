import unittest
from flask import current_app
from app import create_app
from app.models import Universidad
import os

class UniversidadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_universidad_creation(self):
        universidad_ = Universidad()
        universidad_.nombre_universidad = "Universidad Nacional de La Plata"
        universidad_.sigla = "UNLP"
        self.assertIsNotNone(universidad_)
        self.assertEqual(universidad_.nombre_universidad, "Universidad Nacional de La Plata")
        self.assertEqual(universidad_.sigla, "UNLP")

if __name__ == '__main__':
    unittest.main()
