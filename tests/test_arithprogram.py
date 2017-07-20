import unittest
import arithmetic

class testarithmetic(unittest.TestCase):
    def setUp(self):
        self.test_arith = arith()
    def test_add(self):
        self.assertEqual(10, self.test_arith.add(1,9))
    def test_mul(self):
        self.assertEqual(50, self.test_arith.mul(10))
if __name__ == '__main__':
     unittest.main()
