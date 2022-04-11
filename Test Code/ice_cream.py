import unittest
import ice_cream as ic

class TestBrands(unittest.TestCase):
   
    expected = ['White Chocolate Raspberry Truffle Ice Cream', 'Banana Peanut Butter Chip Ice Cream', 'Bourbon Praline Pecan Ice Cream']
    result = ['White Chocolate Raspberry Truffle Ice Cream', 'Banana Peanut Butter Chip Ice Cream', 'Bourbon Praline Pecan Ice Cream']
        
    def test_count_eq(self):
        self.assertEqual(len(self.expected), len(self.result))
        
    def test_list_eq(self):
        self.assertListEqual(self.expected, self.result)

if __name__ == '__main__':
      unittest.main()