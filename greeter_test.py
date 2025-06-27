import unittest
from app import app

class GreetingRouteTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_greeting_route(self):
        name = "tester"
        response = self.app.get(f"/greeting/{name}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), f"Hello {name}")

if __name__ == "__main__":
    unittest.main()
