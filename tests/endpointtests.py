from unittest import TestCase
import json
from src.endpoint import app
from src.inmemorystorage import InMemoryStorage

class EndpointTests(TestCase):

    def setUp(self):
        app.config['STORAGE'] = InMemoryStorage()
        app.testing = True
        self.app = app.test_client()

    def test_addition(self):
        response = self.app.get('/execute/2.8/addition/9.2')
        self.assertEqual(12.0, float(response.data))

    def test_subtraction(self):
        response = self.app.get('/execute/2/subtraction/9')
        self.assertEqual(-7.0, float(response.data))

    def test_multiplication(self):
        response = self.app.get('/execute/2/multiplication/9')
        self.assertEqual(18.0, float(response.data))

    def test_division(self):
        response = self.app.get('/execute/7.5/division/2')
        self.assertEqual(3.75, float(response.data))

    def test_history_is_kept(self):
        self.app.get('/execute/2/addition/9')
        response = self.app.get('/history')
        [operation] = json.loads(response.data)
        self.assertEqual(11.0, operation['result'])
        self.assertEqual(2.0, operation['operand1'])
        self.assertEqual(9.0, operation['operand2'])
        self.assertEqual('addition', operation['calculation'])

    def test_history_can_be_cleared(self):
        self.app.get('/execute/2/addition/9')
        self.app.delete('/history')
        response = self.app.get('/history')
        self.assertListEqual([], json.loads(response.data))
