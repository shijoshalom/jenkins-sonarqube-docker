import unittest
from app import greet

class TestGreeting(unittest.TestCase):

    def test_greet_name(self):
        self.assertEqual(greet("Shijo"), "Hello, Shijo!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello, Guest!")

if __name__ == "__main__":
    unittest.main()
