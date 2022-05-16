'''
    AUTHORS: Daisuke Yamada, Jake Jasmer, Charlie Ney, Shoko Ishikawa
    COURSE: CS 257 - Software Design
    DESCRIPTION: This program contains a test suite providing a comprehensive
    test cases for datasource.py. 
'''

import unittest
import datasource as ds

class TestIceCreamDataSource(unittest.TestCase):
    def setUp(self):
        # data_source used for the rest of tesing
        self.datasource = ds.DataSource()
        # eight ice creams (only names) used to compare our results to the datasets above
        self.bj_ic0 = "Salted Caramel Core" # rating 3.7
        self.bj_ic1 = "Netflix & Chilll'd™" # rating 4.0
        self.hd_ic0 = "White Chocolate Raspberry Truffle Ice Cream" # rating 4.9
        self.hd_ic1 = "Caramel Soft Dipped Ice Cream Bar" # rating 4.7
        self.talenti_ic0 = "ALPHONSO MANGO SORBETTO" # rating 4.7
        self.talenti_ic1 = "BANANA CARAMEL CRUNCH" # rating 4.2
        self.breyers_ic0 = "Natural Vanilla" # rating 4.1
        self.breyers_ic1 = "Homemade Vanilla" # rating 4.4

    def tearDown(self):
        pass

    # tests for get_reivews() method
    def test_valid_get_reviews(self):
        """
            test for get_reviews() with valid input 
        """
        reviews_list = self.datasource.get_reviews("0_bj")
        self.assertEqual(len(reviews_list), 208)
        self.assertEqual(reviews_list[0][2], 3)
        self.assertEqual(reviews_list[0][1], "2017-04-15")
        self.assertEqual(reviews_list[0][3], "Not enough brownies!")

    def test_invalid_get_reviews(self):
        """
            test for get_reviews() with invalid input 
        """
        reviews_list = self.datasource.get_reviews("invalid")
        self.assertEqual(reviews_list, [])

    # tests for search_by_brands() method
    def test_search_by_brands_bj(self):
        """
            test search_by_brands() method with "bj"
        """
        bj_result = self.datasource.search_by_brands("bj")
        self.assertEqual(len(bj_result), 57)
        self.assertIsInstance(bj_result[0], ds.IceCream)
        self.assertEqual(bj_result[0].name, self.bj_ic0)
        self.assertIsInstance(bj_result[1], ds.IceCream)
        self.assertEqual(bj_result[1].name, self.bj_ic1)

    def test_search_by_brands_hd(self):
        """
            test search_by_brands() method with "hd"
        """
        hd_result = self.datasource.search_by_brands("hd")
        self.assertEqual(len(hd_result), 70)
        self.assertIsInstance(hd_result[1], ds.IceCream)
        self.assertEqual(hd_result[1].name, self.hd_ic0)
        self.assertIsInstance(hd_result[6], ds.IceCream)
        self.assertEqual(hd_result[6].name, self.hd_ic1)

    def test_search_by_brands_talenti(self):
        """
            test search_by_brands() method with "talenti"
        """
        talenti_result = self.datasource.search_by_brands("talenti")
        self.assertEqual(len(talenti_result), 45)
        self.assertIsInstance(talenti_result[0], ds.IceCream)
        self.assertEqual(talenti_result[0].name, self.talenti_ic0)
        self.assertIsInstance(talenti_result[1], ds.IceCream)
        self.assertEqual(talenti_result[1].name, self.talenti_ic1)

    def test_search_by_brands_breyers(self):
        """
            test search_by_brands() method with "breyers"
        """
        breyers_result = self.datasource.search_by_brands("breyers")
        self.assertEqual(len(breyers_result), 69)
        self.assertIsInstance(breyers_result[0], ds.IceCream)
        self.assertEqual(breyers_result[0].name, self.breyers_ic0)
        self.assertIsInstance(breyers_result[2], ds.IceCream)
        self.assertEqual(breyers_result[2].name, self.breyers_ic1)

    def test_search_by_brands_invalid(self):
        """
            test search_by_brands() method with some invalid inputs
        """
        invalid_result1 = self.datasource.search_by_brands("invalid")
        invalid_result2 = self.datasource.search_by_brands("100")
        invalid_result3 = self.datasource.search_by_brands("1.000")
        self.assertEqual(invalid_result1, [])
        self.assertEqual(invalid_result2, [])
        self.assertEqual(invalid_result3, [])    

    # tests for search_by_ratings method() 
    def test_search_by_ratings_0_stars(self):
        """
            test search_by_ratings with input "0"
        """
        result = self.datasource.search_by_ratings("0")
        self.assertEqual(len(result), 241)

    def test_search_by_ratings_3_stars(self):
        """
            test search_by_ratings with input "3"
        """
        result = self.datasource.search_by_ratings("3.0")
        self.assertEqual(len(result), 229)
        # check if bj_ic0 is included (should be)
        is_bj_ic0_included = False
        for ic in result:
            if ic.name == self.bj_ic0:
                is_bj_ic0_included = True
                break
        self.assertTrue(is_bj_ic0_included)

    def test_search_by_ratings_4_stars(self):
        """
            test search_by_ratings with input "4"
        """
        result = self.datasource.search_by_ratings("4.0")
        self.assertEqual(len(result), 185)
        # check if bj_ic0 is included (should not be)
        is_bj_ic0_included = False
        for ic in result:
            if ic.name == self.bj_ic0:
                is_bj_ic0_included = True
                break
        self.assertFalse(is_bj_ic0_included)
        # check if bj_ic1 is included (should be)
        is_bj_ic1_included = False
        for ic in result:
            if ic.name == self.bj_ic1:
                is_bj_ic1_included = True
                break
        self.assertTrue(is_bj_ic1_included)

    def test_search_by_ratings_5_stars(self):
        """
            test search_by_ratings with input "5"
        """
        result = self.datasource.search_by_ratings("5.0")
        self.assertEqual(len(result), 8)
        # check if bj_ic1 is included (should not be)
        is_bj_ic1_included = False
        for ic in result:
            if ic.name == self.bj_ic1:
                is_bj_ic1_included = True
                break
        self.assertFalse(is_bj_ic1_included)

    def test_search_by_ratings_invalid(self):
        """
            test search_by_ratings with some invalid inputs
        """
        result = self.datasource.search_by_ratings("5.0")
        self.assertEqual(len(result), 8)

    # tests for sort_by_ratings method()
    def test_sort_by_ratings(self):
        """
            test sort_by_ratings() with some valid input
        """
        result1 = self.datasource.sort_by_ratings("1")
        result2 = self.datasource.sort_by_ratings("100")
        result3 = self.datasource.sort_by_ratings("300")
        self.assertEqual(len(result1), 1)
        self.assertEqual(len(result2), 100)
        self.assertEqual(len(result3), 241)

    def test_sort_by_ratings_invalid(self):
        """
            test sort_by_ratings() with some invalid input
        """
        result1 = self.datasource.sort_by_ratings("-1")
        result2 = self.datasource.sort_by_ratings("1.0")
        result3 = self.datasource.sort_by_ratings("string")
        self.assertEqual(len(result1), 0)
        self.assertEqual(len(result2), 0)
        self.assertEqual(len(result3), 0)

    # tests for search_by_keyword method()
    def test_search_by_keyword_caramel(self):
        """
            test search_by_keyword with input "caramel" (lower and upper)
        """
        result1 = self.datasource.search_by_keyword("caramel")
        result2 = self.datasource.search_by_keyword("CARAMEL")
        self.assertEqual(len(result1), 28)
        self.assertEqual(len(result2), 28)
        # check if bj_ic0 is included (should be)
        is_bj_ic0_included = False
        for ic in result1:
            if ic.name == self.bj_ic0:
                is_bj_ic0_included = True
                break
        self.assertTrue(is_bj_ic0_included)
    
    def test_search_by_keyword_invalid(self):
        """
            test search_by_keyword with input invalid input
        """
        result = self.datasource.search_by_keyword("invalid input")
        self.assertEqual(len(result), 0)

    # tests for search_by_name() method
    def test_search_by_name(self):
        """
            test search_by_name with input "Salted Caramel Core"
        """
        ic = self.datasource.search_by_name("Salted Caramel Core")[0]
        self.assertIsInstance(ic, ds.IceCream)
        self.assertEqual(ic.name, self.bj_ic0)

    def test_search_by_name_invalid(self):
        """
            test search_by_name with an invalid input
        """
        ic = self.datasource.search_by_name("invalid name")
        self.assertEqual(ic, [])

    # test for random_ice_cream() method
    def test_get_random_ice_cream(self):
        """
            test random_ice_cream()
        """
        for i in range(100):
            result = self.datasource.random_ice_cream()
            self.assertIsInstance(result, ds.IceCream)

if __name__ == "__main__":
    unittest.main()