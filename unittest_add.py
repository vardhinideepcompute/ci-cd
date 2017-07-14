import unittest
from addprog import arith

class testarithmetic(unittest.TestCase):
    def setUp(self):
        self.test_arith = arith()
    def test_add(self):
        self.assertEqual(10, self.test_arith.add(1,9))

if __name__ == '__main__':
     unittest.main()
