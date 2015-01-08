import unittest
from composite import composite_order

class CompositeOrderTest(unittest.TestCase):
    def test_composite_order(self):
        list_list = [
        [1,3,2], [8,6,3], [9,7,8] 
        ]
        self.assertEqual(
        composite_order(list_list), [1,2,3,3,6,7,8,8,9]
        ) 
        



if __name__ == '__main__':
    unittest.main()