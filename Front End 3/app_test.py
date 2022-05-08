'''
    @assignment: Flask App Team Assignment
    @author: Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, Charlie Ney
    @course CS257, Softare Design
    @usage: To run this program please use:

                python3 app_test.py

            while having html templates, ice_cream.py, and flask_app.py in the same directpry 
            as this file. It might take a few seconds to run as we have not implmented 
            our database. 
'''

from app import app
import unittest

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        '''
            set up a (global) variable app using flask's build-in test_client()
        '''
        self.app = app.test_client()

    # test if the home page is displayed as expected
    def test_route_homepage(self):
        '''
            test if the route for homepage works and displays the correct output 
        '''
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Quest for the Best Ice Cream', response.data) 
        self.assertIn(b'About Us', response.data) 
        self.assertIn(b'Editor\'s Choice', response.data) 
        self.assertIn(b'Ben & Jerry\'s', response.data) 

    # the following two tests are for brand search for Ben and Jerry's (right/wrong)
    def test_route_brand_search_right_icecreams_bj(self):
        '''
            test if the route for brand search works and displays the correct ice creams 
        '''
        response = self.app.get('/feature=brand_search/input=bj', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'See Product')
        self.assertEqual(count, 57)
        # test for first bj icecream
        self.assertIn(b'Salted Caramel Core', response.data) 
        # test for second bj icecream     
        self.assertIn(b'Chip Happens', response.data)
    
    def test_route_brand_search_wrong_icecreams_bj(self):
        '''
            tests if the route for brand search works and does not displays the wrong ice creams
            for Ben and Jerry's
        '''
        response = self.app.get('/feature=brand_search/input=bj', follow_redirects=True)
        # test for first ice cream (from hd) that should not be included
        self.assertNotIn(b'Banana Peanut Butter Chip Ice Cream', response.data) 
        # test for second ice cream (from talenti) that should not be included 
        self.assertNotIn(b'BANANA CARAMEL CRUNCH', response.data) 
        # test for third ice cream (from breyers) that should not be included 
        self.assertNotIn(b'Homemade Vanilla', response.data) 

    # the following two tests are for brand search for Haagen Dazs (right/wrong)
    def test_route_brand_search_right_icecreams_hd(self):
        '''
            tests if the route for brand search works and displays the correct ice creams
            for Haagen Dazs
        '''
        response = self.app.get('/feature=brand_search/input=hd', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'See Product')
        self.assertEqual(count, 70)
        # test for first hd icecream
        self.assertIn(b'White Chocolate Raspberry Truffle Ice Cream', response.data) 
        # test for second hd icecream     
        self.assertIn(b'Banana Peanut Butter Chip Ice Cream', response.data)

    def test_route_brand_search_wrong_icecreams_hd(self):
        '''
            tests if the route for brand search works and does not displays the wrong ice creams
            for Haagen Dazs
        '''
        response = self.app.get('/feature=brand_search/input=hd', follow_redirects=True)
        # test for first ice cream (from bj) that should not be included
        self.assertNotIn(b'Chip Happens', response.data) 
        # test for first ice cream (from talenti) that should not be included 
        self.assertNotIn(b'BANANA CARAMEL CRUNCH', response.data) 
        # test for first ice cream (from breyers) that should not be included
        self.assertNotIn(b'Homemade Vanilla', response.data)

    # the following two tests are for brand search for Talenti (right/wrong)
    def test_route_brand_search_right_icecreams_talenti(self):
        '''
            test if the route for brand search works and displays the correct ice creams 
        '''
        response = self.app.get('/feature=brand_search/input=talenti', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'See Product')
        self.assertEqual(count, 45)
        # test for first Talenti icecream
        self.assertIn(b'ALPHONSO MANGO SORBETTO', response.data) 
        # test for second Talenti icecream
        self.assertIn(b'BANANA CARAMEL CRUNCH', response.data)

    def test_route_brand_search_wrong_icecreams_talenti(self):
        '''
            tests if the route for brand search works and does not displays the wrong ice creams
            for Talenti
        '''
        response = self.app.get('/feature=brand_search/input=talenti', follow_redirects=True)
        # test for first Ben and Jerry's ice cream that should not be included
        self.assertNotIn(b'Chip Happens', response.data) 
        # test for first Haagen Dazs ice cream that should not be included
        self.assertNotIn(b'Banana Peanut Butter Chip Ice Cream', response.data)
        # test for first Breyers ice cream that should not be included
        self.assertNotIn(b'Homemade Vanilla', response.data)

    # the following two tests are for brand search for Breyers (right/wrong)
    def test_route_brand_search_right_icecreams_breyers(self):
        '''
            test if the route for brand search works and displays the correct ice creams
            for Breyers
        '''
        response = self.app.get('/feature=brand_search/input=breyers', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'See Product')
        self.assertEqual(count, 69)
        # test for first Breyers icecream
        self.assertIn(b'Natural Vanilla', response.data) 
        # test for second Breyers icecream
        self.assertIn(b'Homemade Vanilla', response.data)   

    def test_route_brand_search_wrong_icecreams_breyers(self):
        '''
            tests if the route for brand search works and does not displays the wrong ice creams
            for Breyer's
        '''
        response = self.app.get('/feature=brand_search/input=breyers', follow_redirects=True)
        # test for first Ben and Jerry's ice cream that should not be included
        self.assertNotIn(b'Chip Happens', response.data) 
        # test for first Haagen Dazs ice cream that should not be included
        self.assertNotIn(b'Banana Peanut Butter Chip Ice Cream', response.data)
        # test for first Talenti ice cream that should not be included
        self.assertNotIn(b'BANANA CARAMEL CRUNCH', response.data) 

    # the following two tests are for rating search
    def test_route_rating_search_valid_icecreams(self):
        '''
            test if the route for rating search works and displays the correct ice creams 
        '''
        response = self.app.get('/feature=rating_search/input=4.9', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'See Product')
        self.assertEqual(count, 19)
        # test for first icecream
        self.assertIn(b'Peanut Butter Half Baked', response.data) 
        # test for second icecream     
        self.assertIn(b'Chocolate Peanut Butter Split', response.data)   
    
    def test_route_rating_search_invalid_icecreams(self):
        '''
            test if the route for rating search works and does not displays the wrong icecreams
        '''
        response = self.app.get('/feature=rating_search/input=4.8', follow_redirects=True)
        # test for first ice cream that should not be included
        self.assertNotIn(b'Extra Creamy Vanilla', response.data) 
        # test for second ice cream that should not be included 
        self.assertNotIn(b'Homemade Vanilla', response.data) 
    
    # the following two tests are for rating sort
    def test_route_rating_sort_valid_icecreams(self):
        '''
            test if the route for rating sort works and displays the correct icecreams
        '''
        response = self.app.get('/feature=rating_sort?input=3', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'See Product')
        self.assertEqual(count, 3)
        # test for first icecream
        self.assertIn(b'Chocolate Peanut Butter Split', response.data) 
        # test for second icecream     
        self.assertIn(b'Ice Cream Sammie', response.data) 
        # test for thrid icecream     
        self.assertIn(b'Chocolate Fudge Non-Dairy Bar', response.data)    
    
    def test_route_rating_sort_invalid_icecreams(self):
        '''
            test if the route for rating sort works and does not displays the wrong icecreams
        ''' 
        response = self.app.get('/feature=rating_sort?input=3', follow_redirects=True)
        # test for first ice cream that should not be included
        self.assertNotIn(b'Honey Salted Caramel Almond Ice Cream', response.data) 
        # test for second ice cream that should not be included 
        self.assertNotIn(b'Peppermint Bark Ice Cream', response.data) 
        # test for third ice cream that should not be included 
        self.assertNotIn(b'Peppermint Bark Ice Cream Bar', response.data) 

    # tests for invalid feature/input/link
    def test_route_invalid_feature(self):
        '''
            test if the app responses to some invalid feature
        '''
        response1 = self.app.get('/feature=stupid_feature/input=bj', follow_redirects=True)
        self.assertIn(b'No ice creams found for your search', response1.data) 
    
    def test_route_invalid_input(self):
        '''
            test if the app responses to some invalid input
        '''
        response1 = self.app.get('/feature=brand_search/input=wrong_rating', follow_redirects=True)
        self.assertIn(b'No ice creams found for your search', response1.data) 
        response2 = self.app.get('/feature=rating_search/input=wrong_rating', follow_redirects=True)
        self.assertIn(b'No ice creams found for your search', response2.data)
        response3 = self.app.get('/feature=rating_sort?input=wrong_input', follow_redirects=True)
        self.assertIn(b'No ice creams found for your search', response3.data)

    def test_route_error_404(self):
        '''
            test the error_handler for ERROR 404 page (any invalid links should go here)
        '''
        response1 = self.app.get('/r/a/n/d/o/m', follow_redirects=True)
        self.assertIn(b'The page you are looking for doesn\'t exist', response1.data)
        response2 = self.app.get('/invalid/link/is/here!', follow_redirects=True)
        self.assertIn(b'The page you are looking for doesn\'t exist', response2.data)

if __name__ == "__main__":
    unittest.main()