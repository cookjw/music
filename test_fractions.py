import unittest
from fractions import Fraction

class FractionTest(unittest.TestCase):
    def test_display(self):
        self.assertEqual(str(Fraction(3,4)), "3/4")
        
    def test_comparison(self):
        x = Fraction(1,2)
        y = Fraction(1,3)
        self.assertTrue(x > y)
        self.assertFalse(x < y)
        self.assertTrue(x >= y)
        self.assertFalse(x <= y)
        
    
    def test_addition(self):
        x = Fraction(1,2)
        y = Fraction(1,3)  
        self.assertEqual(str(x+y), "5/6")  

    def test_subtraction(self):
        x = Fraction(1,2)
        y = Fraction(1,3) 
        self.assertEqual(str(x-y), "1/6")
        
    def test_multiplication(self):
        x = Fraction(1,2)
        y = Fraction(1,3) 
        self.assertEqual(str(x*y), "1/6")

    def test_division(self):
        x = Fraction(1,2)
        y = Fraction(1,3)
        self.assertEqual(str(x/y), "3/2")            

    def test_reciprocal(self):
        self.assertEqual(str(Fraction(1,2).reciprocal()), "2")
        self.assertEqual(str(Fraction(2,3).reciprocal()), "3/2")        
        
    



if __name__ == '__main__':
    unittest.main()    


