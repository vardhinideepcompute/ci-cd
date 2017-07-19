import unittest2
from prime_no import is_prime
from add import add

print "Test file"
class PrimesTestCase(unittest2.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))
class addTestCase(unittest2.TestCase):
    def testadd(self):
        self.assertEqual(add.add_num(5,5,5),15)

if __name__ == '__main__':
    unittest2.main()
