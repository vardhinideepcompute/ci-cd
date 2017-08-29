import unittest
from add import add


class SimplisticTest(unittest.TestCase):

    def test_add(self):
            self.assertTrue(add(4,5),9)
if __name__ == '__main__':
     unittest.main()
