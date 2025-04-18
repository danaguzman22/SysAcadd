import unittest
from flask import current_app
from app import create_app
from app.models import Plan
import os

class PlanTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_plan_creation(self):
        plan = Plan ()
        plan.nombre = "Plan 2025"
        plan.fecha_inicio = "2025-01-01"
        plan.fecha_fin = "2025-12-31"
        plan.observaciones = "Plan de estudios 2025"
        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, "Plan 2025")
        self.assertEqual(plan.fecha_inicio, "2025-01-01")
        self.assertEqual(plan.fecha_fin, "2025-12-31")


if __name__ == '__main__':
    unittest.main()