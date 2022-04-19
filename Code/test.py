"""
    File@ test.py
    Author@ Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, and Charlie Ney
    Course@ CS 257, Software Design, Prof Anya Vostinar

    This program conatins all the test cases required to 
    ensure the three functionalities supported by ice_cream.py:

    1) Search by brands
    2) Search by ratings
    3) Sort by ratings

    This program uses dummy datasets "dummy_products.cvs" and "dummy_reviews.cvs", 
    which are simpler versions of the original datasets used for this project. "dummy_products.cvs"
    conatins two ice creams from the four brands, and "dummy_reviews.cvs" contains
    the corresponding reviews for these 8 ice creams.
"""

import unittest
import ice_cream as ic

class TestBrands(unittest.TestCase):
    def setUp(self):
        # data_source used for the rest of tesing
        self.data_source = ic.DataSource("dummy_products.csv", "dummy_reviews.csv")
        # eight ice creams used to compare our results to the datasets above
        self.bj_ic1 = ic.IceCream("dummy_reviews.csv", "0_bj", "Salted Caramel Core", \
                    "description bj 1", 3.7, 208, "ingredient 1")
        self.bj_ic2 = ic.IceCream("dummy_reviews.csv", "1_bj", "Netflix & Chilll'd™", \
                    "description bj 2", 4.0, 127, "ingredient 2")
        self.hd_ic1 = ic.IceCream("dummy_reviews.csv", "0_hd", "White Chocolate Raspberry Truffle Ice Cream", \
                    "description hd 1", 4.9, 168, "ingredient 3")  
        self.hd_ic2 = ic.IceCream("dummy_reviews.csv", "5_hd", "Caramel Soft Dipped Ice Cream Bar", \
                    "description hd 2", 4.9, 8, "ingredient 4")
        self.talenti_ic1 = ic.IceCream("dummy_reviews.csv", "0_talenti", "ALPHONSO MANGO SORBETTO", \
                    "description ti 1", 4.7, 139.0, "ingredient 5")
        self.talenti_ic2 = ic.IceCream("dummy_reviews.csv", "1_talenti", "BANANA CARAMEL CRUNCH", \
                    "description ti 2", 4.2, 25, "ingredient 6")
        self.breyers_ic1 = ic.IceCream("dummy_reviews.csv", "0_breyers", "Natural Vanilla", \
                    "description br 1", 4.1, 467.0, "ingredient 7")
        self.breyers_ic2 = ic.IceCream("dummy_reviews.csv", "1_breyers", "Homemade Vanilla", \
                    "description br 2", 4.4, 98, "ingredient 8")

    def tearDown(self):
        pass

    # tests for IceCream class and get_reivews
    def test_get_reviews(self):
        """
            test for get_reviews(review_file_name) in IceCream class
        """
        test_ic1_reviews_list = self.bj_ic1.reviews
        self.assertEqual(len(test_ic1_reviews_list), 2)
        self.assertIsInstance(test_ic1_reviews_list[0], ic.Review)
        self.assertEqual(test_ic1_reviews_list[0].rating, 3)
        self.assertEqual(test_ic1_reviews_list[0].date, "2017-04-15")

    def test_get_reviews_empty_columns(self):
        """
            test for get_reviews if there are empty columns
        """
        test_ic2_reviews_list = self.hd_ic2.reviews
        self.assertEqual(len(test_ic2_reviews_list), 2)
        self.assertIsInstance(test_ic2_reviews_list[1], ic.Review)
        self.assertEqual(test_ic2_reviews_list[1].rating, -1)
        self.assertEqual(test_ic2_reviews_list[1].comment, "")
        self.assertEqual(test_ic2_reviews_list[1].date, "")

    # tests for load_products_data in DataSource class
    def test_load_products_data_length(self):
        """
            test for load_products_date helper method for having the intended length
        """
        self.assertEqual(len(self.data_source.ice_cream_data_source), 4)
        count = 0
        for brand in self.data_source.ice_cream_data_source:
            for ic in brand:
                count += 1
        self.assertEqual(count, 8)

    def test_load_products_data_content(self):
        """
            test for load_products_date helper method's content
        """
        result = self.data_source.ice_cream_data_source
        intended_result = [[self.bj_ic1, self.bj_ic2],[self.hd_ic1, self.hd_ic2],\
                        [self.talenti_ic1, self.talenti_ic2],[self.breyers_ic1, self.breyers_ic2]]
        self.assertEqual(result, intended_result)

    # tests for brand search
    def test_is_valid_brand_input_success_bj(self):
        """
            test for is_valid_brand_input(string input) helper method
        """
        bj_valid_names = ["bj", "ben and jerry's", "b&j", "ben and jerrys", "BJ", \
                        "Ben and Jerry's", "B&J", "Ben and Jerrys"]
        for name in bj_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), "bj")

    def test_is_valid_brand_input_success_hd(self):
        """
            test for is_valid_brand_input(string input) help method
        """
        hd_valid_names = ["hd", "haagen-dazs", "haagen dazs", "Haagen Dazs", "Haagen-Dazs"]
        for name in hd_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), "hd")

    def test_is_valid_brand_input_success_breyers(self):
        """
            test for is_valid_brand_input(string input) help method
        """
        breyers_valid_names = ["breyers", "Breyers"]
        for name in breyers_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), "br")

    def test_is_valid_brand_input_success_talenti(self):
        """
            test for is_valid_brand_input(string input) help method
        """
        talenti_valid_names = ["talenti", "Talenti"]
        for name in talenti_valid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), "ti")

    def test_is_invalid_brand_input(self):
        """
            test for is_valid_brand_input(string input) help method
        """
        invalid_names = ["1235", " ", "", "Bj", "#$%^&*)(*&", "talen"]
        for name in invalid_names:
            self.assertEqual(self.data_source.is_valid_brand_input(name), None)

    # test for search_by_brands
    def test_search_by_brands_bj(self):
        """
            test brand search by bj
        """
        bj_result = self.data_source.search_by_brands("Ben and Jerry's")
        bj_intended_result = [self.bj_ic1, self.bj_ic2]
        self.assertEqual(bj_result, bj_intended_result)

    def test_search_by_brands_hd(self):
        """
            test brand search by hd
        """
        hd_result = self.data_source.search_by_brands("Haagen Dazs")
        hd_intended_result = [self.hd_ic1, self.hd_ic2]
        self.assertEqual(hd_result, hd_intended_result)

    def test_search_by_brands_ti(self):
        """
            test brand search by ti
        """
        ti_result = self.data_source.search_by_brands("Talenti")
        ti_intended_result = [self.talenti_ic1, self.talenti_ic2]
        self.assertEqual(ti_result, ti_intended_result)

    def test_search_by_brands_br(self):
        """
            test brand search by br
        """
        br_result = self.data_source.search_by_brands("Breyers")
        br_intended_result = [self.breyers_ic1, self.breyers_ic2]
        self.assertEqual(br_result, br_intended_result)

    def test_is_invalid_search_by_brands_input(self):
        """
            test invalid brand search input
        """
        invalid_result = self.data_source.search_by_brands("invalid")
        self.assertEqual(invalid_result, [])

    # tests for rating search  
    def test_is_valid_rating(self):
        """
            test valid rating inputs (typical/unit)
        """ 
        valid_ratings = ["0", "1", "2", "3", "4", "5", "0.1", "1.5", "3.785", "4.9999", 0,\
                        1, 2, 3, 4, 5, 3.5, 4.5]
        for rating in valid_ratings:
            result = self.data_source.is_valid_rating_input(rating)
            self.assertIsInstance(result, float)
            self.assertEqual(result, float(rating))

    def test_is_invalid_rating(self):
        """
            test invalid rating inputs (edge/unit)
        """
        invalid_ratings = [-3, -1, 5.1, 6, 100, "non-numeric string"]
        for rating in invalid_ratings:
            self.assertEqual(self.data_source.is_valid_rating_input(rating), -1)

    def test_search_by_ratings_0_stars(self):
        """
            test rating search output with case of 0 stars (typical/integrated for one feature)
        """
        result = self.data_source.search_by_ratings("0")
        intended_result = [self.bj_ic1, self.bj_ic2, self.hd_ic1, self.hd_ic2, self.talenti_ic1, \
                            self.talenti_ic2, self.breyers_ic1, self.breyers_ic2]
        self.assertEqual(len(result), 8)
        self.assertEqual(intended_result, result)

    def test_search_by_ratings(self):
        """
            test rating search output with 4.2 stars and 4.8 (typical/integrated)
        """
        result1 = self.data_source.search_by_ratings("4.2")
        intended_result1 = [self.hd_ic1, self.hd_ic2, self.talenti_ic1, self.talenti_ic2, self.breyers_ic2]
        self.assertEqual(len(intended_result1), 5)
        self.assertEqual(intended_result1, result1)

        result2 = self.data_source.search_by_ratings("4.8")
        intended_result2 = [self.hd_ic1, self.hd_ic2]
        self.assertEqual(len(intended_result2), 2)
        self.assertEqual(intended_result2, result2)

    def test_search_by_ratings_5_stars(self):
        """
            test rating search output with edge case of 5 stars (typical/integrated)
        """
        self.assertEqual(self.data_source.search_by_ratings("5"), [])

    def test_search_by_ratings_invalid(self):
        """
            test rating search output with edge cases of invalid rating inputs 
            (edge/integrated)
        """
        # rating out of range
        self.assertEqual(self.data_source.search_by_ratings("-1"), [])
        # rating out of range
        self.assertEqual(self.data_source.search_by_ratings("6"), [])
        # rating non-numeric
        self.assertEqual(self.data_source.search_by_ratings("non-numeric string"), [])

    def test_is_invalid_sorting(self):
        """
            test invalid input for sorting
        """
        self.assertEqual(self.data_source.sort_by_ratings("a;lfj"), [])
        self.assertEqual(self.data_source.sort_by_ratings(-1), [])

    def test_sort_by_ratings_length(self):
        """
            test valid input length
        """
        result1 = self.data_source.sort_by_ratings(0)
        self.assertEqual(len(result1), 0)
        result2 = self.data_source.sort_by_ratings(2)
        self.assertEqual(len(result2), 2)
        result2 = self.data_source.sort_by_ratings(9)
        self.assertEqual(len(result2), 8)

    def test_is_valid_sorting(self):
        """
            test correct output
        """
        result = self.data_source.sort_by_ratings(3)
        intended_result = [self.hd_ic1, self.hd_ic2, self.talenti_ic1]
        self.assertEqual(intended_result, result)

if __name__ == "__main__":
    unittest.main()