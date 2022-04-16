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
        self.data_source = ic.DataSource("dummy_products.csv", "dummy_reviews.csv")

    def tearDown(self):
        pass

    # test for get_reviews(review_file_name) in IceCream class
    def test1_get_reviews(self):
        test_ic1 = ic.IceCream('dummy_reviews.csv', '0_bj', 'Salted Caramel Core', 'random description', 3, 208, 'ingredients')
        test_ic1_reviews_list = test_ic1.reviews
        self.assertEqual(len(test_ic1_reviews_list), 2)
        self.assertIsInstance(test_ic1_reviews_list[0], ic.Review)
        self.assertEqual(test_ic1_reviews_list[0].rating, 3)
        self.assertEqual(test_ic1_reviews_list[0].date, '2017-04-15')

    def test2_get_reviews_empty_columns(self):
        test_ic2 = ic.IceCream('dummy_reviews.csv', '5_hd', 'Caramel Soft Dipped Ice Cream Bar', 'random description', 4.9, 208, 'some ingredients')
        test_ic2_reviews_list = test_ic2.reviews
        self.assertEqual(len(test_ic2_reviews_list), 2)
        self.assertIsInstance(test_ic2_reviews_list[1], ic.Review)
        self.assertEqual(test_ic2_reviews_list[1].rating, -1)
        self.assertEqual(test_ic2_reviews_list[1].comment, '')
        self.assertEqual(test_ic2_reviews_list[1].date, '')

    # tests for brand search
    # test for is_valid_brand_input(string input) helper method
    def is_valid_brand_input_success_bj(self):
        bj_valid_names = ["bj", "ben and jerry's", "b&j", "ben and jerrys", "BJ", "Ben and Jerry's", "B&J", "Ben and Jerrys"]
        for name in bj_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), 'bj')

    # test for is_valid_brand_input(string input) help method
    def is_valid_brand_input_success_hd(self):
        hd_valid_names = ["hd", "haagen-dazs", "haagen dazs", "Haagen Dazs", "Haagen-Dazs"]
        for name in hd_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), 'hd')

    # test for is_valid_brand_input(string input) help method
    def is_valid_brand_input_success_breyers(self):
        breyers_valid_names = ["breyers", "Breyers"]
        for name in breyers_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), 'breyers')

    # test for is_valid_brand_input(string input) help method
    def is_valid_brand_input_success_talenti(self):
        talenti_valid_names = ["talenti", "Talenti"]
        for name in talenti_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), 'talenti')

    def is_invalid_brand_input(self):
        invalid_names = ["1235", " ", "", "Bj", "#$%^&*)(*&", "talen"]
        for name in invalid_names:
            self.assertTrue(self.data_source.is_valid_brand_input(name), None)
    
    # tests for rating search
    # test for is_valid_rating_input

if __name__ == '__main__':
    unittest.main()