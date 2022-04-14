'''
    File@ test.py
    Author@ Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, and Charlie Ney
    Course@ CS 257, Software Design, Prof Anya Vostinar

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
        self.data_source = ic.IceCreamDataSource("dummy_products.csv")

    def tearDown(self):
        pass

    # tests for brand search
    # test for get_reviews(string file_name)

    # test for is_valid_brand_input(string input) helper method
    def is_valid_brand_input_success_bj(self):
        bj_valid_names = ["bj", "ben and jerry's", "b&j", "ben and jerrys", "BJ", "Ben and Jerry's", "B&J", "Ben and Jerrys"]
        for name in bj_valid_names:
            self.assertTrue(ic.is_valid_brand_input(name), True)

    # test for is_valid_brand_input(string input) help method
    def is_valid_brand_input_success_hd(self):
        hd_valid_names = ["hd", "haagen-dazs", "haagen dazs", "Haagen Dazs", "Haagen-Dazs"]
        for name in hd_valid_names:
            self.assertTrue(ic.is_valid_brand_input(name), True)

    # test for is_valid_brand_input(string input) help method
    def is_valid_brand_input_success_breyers(self):
        breyers_valid_names = ["breyers", "Breyers"]
        for name in breyers_valid_names:
            self.assertTrue(ic.is_valid_brand_input(name), True)

    # test for is_valid_brand_input(string input) help method
    def is_valid_brand_input_success_talenti(self):
        talenti_valid_names = ["talenti", "Talenti"]
        for name in talenti_valid_names:
            self.assertTrue(ic.is_valid_brand_input(name), True)

    def is_invalid_brand_input(self):
        invalid_names = ["1235", " ", "", "Bj", "#$%^&*)(*&", "talen"]
        for name in invalid_names:
            self.assertTrue(ic.is_invalid_brand_input(name), True)
    
    # tests for rating search
    # test for is_valid_rating_input

if __name__ == '__main__':
    unittest.main()