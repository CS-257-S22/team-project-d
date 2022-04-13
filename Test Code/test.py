'''
Author@ Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, and Charlie Ney
Course@ CS 257, Software Design, Prof Anya Vostinar

test.py

This program conatins all the test cases required to 
ensure the two functionalities supported by ice_cream.py:

1) Search by brands
2) Search by ratings

This program uses dummy datasets "dummy_products.cvs" and "dummy_reviews.cvs", 
which are subsets of actual datasets used for this project. "dummy_products.cvs"
conatins two ice creams from the four brands, and "dummy_reviews.cvs" contains
the corresponding reviews for these 8 ice creams.
'''

import unittest
import ice_cream as ic

class TestBrands(unittest.TestCase):
    def setUp(self):
        self.products_data = ic.icecream_data_source("dummy_products.csv")
        self.reviews_data = ic.icecream_data_source("dummy_products.csv")
    
    def tearDown(self):
        pass

    def test_count_eq(self):
        self.assertEqual(len(self.expected), len(self.result))
        
    def test_list_eq(self):
        self.assertListEqual(self.expected, self.result)

if __name__ == '__main__':
      unittest.main()