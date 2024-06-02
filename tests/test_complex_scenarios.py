import unittest
from app import app, db
from models import Scenario, Option

class ComplexScenarioTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_complex_scenario(self):
        response = self.app.post('/api/scenarios', json={
            'question': 'Test Complex Question?',
            'options': [
                {'text': 'Option 1', 'next_scenario_id': 2},
                {'text': 'Option 2', 'conclusion': 'Complex Conclusion'}
            ]
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Scenario created', response.get_data(as_text=True))

    # Additional tests...

if __name__ == '__main__':
    unittest.main()
