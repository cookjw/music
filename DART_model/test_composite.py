import unittest
from composite import composite_order, get_onset_times

class CompositeOrderTest(unittest.TestCase):
    def test_composite_order(self):
        list_list = [
        [1,3,2], [8,6,3], [9,7,8] 
        ]
        self.assertEqual(
        composite_order(list_list), [1,2,3,3,6,7,8,8,9]
        ) 
    
class OnsetTimeTest(unittest.TestCase):
    def test_onset_times(self):
        self.assertEqual(
        get_onset_times([1,1,1,1]), [0,1,2,3]
        )
        self.assertEqual(
        get_onset_times([1,2,1,1]), [0,1,3,4]
        )
        



if __name__ == '__main__':
    unittest.main()