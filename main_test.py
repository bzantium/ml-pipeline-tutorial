import unittest
import main


class MainTest(unittest.TestCase):
    def test_hello_world(self):
        ret = main.hello_world("Minho")
        self.assertEqual(ret, "Hello World!, Minho")


if __name__ == "__main__":
    unittest.main()