import unittest
from flask import current_app
from app import create_app
from app.models import Universidad
from app.services import UniversidadService
from app import db
import os

class UniversidadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self): 
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        

    def test_universidad_creation(self):
        universidad = self.__nuevaUniversidad()
        self.assertIsNotNone(universidad)
        self.assertEqual(universidad.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad.sigla, "UNLP")
       

    def test_crear_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_Universidad(universidad)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, "Universidad Nacional de La Plata")
        
    def test_universidad_busqueda(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_Universidad(universidad)
        universidad_encontrada = UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNotNone(universidad_encontrada)
        self.assertEqual(universidad_encontrada.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad_encontrada.sigla, "UNLP")
    
    def test_buscar_universidades(self):
        universidad1 = Universidad(nombre="Universidad Nacional de La Plata", sigla="UNLP")
        universidad2 = Universidad(nombre="Universidad Nacional del Sur", sigla="UNS")
        UniversidadService.crear_Universidad(universidad1)
        UniversidadService.crear_Universidad(universidad2)
        universidades = UniversidadService.buscar_todos()
        self.assertIsNotNone(universidades)
        self.assertEqual(len(universidades), 2)
        
    def test_actualizar_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_Universidad(universidad)
        universidad.nombre = "Universidad Nacional del Sur"
        universidad_actualizada = UniversidadService.actualizar_Universidad(universidad.id, universidad)
        self.assertIsNotNone(universidad_actualizada)
        self.assertEqual(universidad_actualizada.nombre, "Universidad Nacional del Sur")


    def test_borrar_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_Universidad(universidad)
        db.session.delete(universidad)
        db.session.commit()
        universidad_borrada = UniversidadService.borrar_por_id(universidad.id)
        self.assertIsNone(universidad_borrada)
        
    def __nuevaUniversidad(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Nacional de La Plata"
        universidad.sigla = "UNLP"
        return universidad
    
if __name__ == '__main__':
    unittest.main()
