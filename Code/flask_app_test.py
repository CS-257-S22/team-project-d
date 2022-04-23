from flask_app import app
import unittest

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_route_homepage(self):
        '''
            test if the route for homepage works and displays the correct output 
        '''
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Instructions for navigating our website', response.data) 

    def test_route_brand_search_valid_icecreams(self):
        '''
            test if the route for brand search works and displays the correct ice creams 
        '''
        response = self.app.get('/feature=brand_search/input=bj', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'reviews')
        self.assertEqual(count, 57)
        # test for first icecream
        self.assertIn(b'Salted Caramel Core', response.data) 
        # test for second icecream     
        self.assertIn(b'Netflix', response.data)   
    
    def test_route_brand_search_invalid_icecreams(self):
        '''
            test if the route for brand search works and does not displays the wrong icecreams
        '''
        response = self.app.get('/feature=brand_search/input=bj', follow_redirects=True)
        # test for first ice cream that should not be included
        self.assertNotIn(b'White Chocolate Raspberry Truffle Ice Cream', response.data) 
        # test for second ice cream that should not be included 
        self.assertNotIn(b'Caramel Soft Dipped Ice Cream Bar', response.data)   

    def test_route_rating_search_valid_icecreams(self):
        '''
            test if the route for rating search works and displays the correct ice creams 
        '''
        response = self.app.get('/feature=rating_search/input=4.9', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'reviews')
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
        self.assertNotIn(b'Natural Vanilla', response.data) 
        # test for second ice cream that should not be included 
        self.assertNotIn(b'Homemade Vanilla', response.data) 
    
    def test_route_rating_sort_valid_icecreams(self):
        '''
            test if the route for rating sort works and displays the correct icecreams
        '''
        response = self.app.get('/feature=rating_sort/input=3', follow_redirects=True)
        # test if response outputs the correct number of ice creams
        count = response.data.count(b'reviews')
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
        response = self.app.get('/feature=rating/input=3', follow_redirects=True)
        # test for first ice cream that should not be included
        self.assertNotIn(b'Honey Salted Caramel Almond Ice Cream', response.data) 
        # test for second ice cream that should not be included 
        self.assertNotIn(b'Peppermint Bark Ice Cream', response.data) 
        # test for third ice cream that should not be included 
        self.assertNotIn(b'Peppermint Bark Ice Cream Bar', response.data) 

    def test_route_invalid_input(self):
        '''
            test if the app responses to some invalid links by displaying the error and suggestions
        '''
        response1 = self.app.get('/feature=nonexisting_command/input=bj', follow_redirects=True)
        self.assertIn(b'Something Went Wrong', response1.data) 
        response2 = self.app.get('/feature=brand_search/input=wrong_brand', follow_redirects=True)
        self.assertIn(b'Something Went Wrong', response2.data)
        response3 = self.app.get('/r/o/n/d/o/m', follow_redirects=True)
        self.assertIn(b'Page Not Found', response3.data)

if __name__ == "__main__":
    unittest.main()