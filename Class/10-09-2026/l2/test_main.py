import unittest
from main import add 
from main import password

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_pass(self):
        self.assertEqual(password('Sasa1223m+'), True)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
result = unittest.TextTestRunner(verbosity=0).run(suite)
assert result.wasSuccessful()