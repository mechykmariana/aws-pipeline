import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        # Capture the output
        with self.assertLogs(level='INFO') as log:
            main()
            self.assertIn('Hello, World!', log.output[0])

if __name__ == "__main__":
    unittest.main()
