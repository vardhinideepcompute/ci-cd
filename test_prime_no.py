import unittest2
from prime_no import is_prime

print "Test file"
class PrimesTestCase(unittest2.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
