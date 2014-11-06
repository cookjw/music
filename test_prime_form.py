import unittest
from prime_form import find_prime_form

class PrimeFormTest(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(find_prime_form([1,1,2]), [0,1])
        self.assertEqual(find_prime_form([8,0,4,6]), [0,2,4,8])
        self.assertEqual(find_prime_form([2,4,5,7,9]), [0,2,3,5,7])
        self.assertEqual(find_prime_form([0,5,6]), [0,1,6])
        #Forte, not Rahn-Morris:
        self.assertEqual(find_prime_form([0,1,5,6,8]), [0,1,3,7,8])


if __name__ == '__main__':
    unittest.main() 