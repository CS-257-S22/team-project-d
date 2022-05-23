'''
    AUTHORS: Daisuke Yamada, Jake Jasmer, Charlie Ney, Shoko Ishikawa
    COURSE: CS 257 - Software Design
    DESCRIPTION: This program uses psycopg2 module to connect to the databse
    specified by "config.py". It then executes some queries to get data
    from the tables in the databse "products" and "reviews". 
'''
import psycopg2
import config
import random

class IceCream:
    '''
        This class creates an IceCream object that represnets an individual ice cream. 
        (Just for the readability of our code)
    '''
    def __init__(self, brand_key:str, name:str, description:str, rating:float,\
                rating_count:int, ingredients:str, reviews):
        self.brand_key = brand_key
        self.name = name
        self.description = description
        self.rating = rating
        self.int_rating = int(rating)
        self.rating_count = rating_count
        self.ingredients = ingredients
        self.reviews = reviews

class Review:
    '''
        This class creates a Review object that represnets an individual review
        for some ice cream. (Just for the readability of our code)
    '''
    def __init__(self, date:str, rating:int, title:str, comment:str):
        self.date = date
        self.rating = int(rating)
        self.title = title
        self.comment = comment

class DataSource:    
    def __init__(self):
        '''
            The constructor that instanciates the connection using cnnect()
        '''
        self.connection = self.connect()

    def connect(self):
        '''
            DESCRIPTION: Try to connect to the database and returns the connection if succeeds
            PARAMS: NONE
            RETURNS: connection - the resulting connection
        '''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("ERROR while connecting to the database: ", e)
            exit()
        return connection

    def execute_query(self, query, query_arg=None):
        '''
            DESCRIPTION: Try to create a cursor, execute the query that is passed in, and display the 
            query output.
            PARAMS: query - the query to be execuuted
                    query_arg - None by default, indicating the parameter used for this query 
            RETURNS: the list of output that matchs the input query
        '''
        try:
            # Set up a cursor
            cursor = self.connection.cursor()
            # Execute the query with or without argument
            if(query_arg == None):
                cursor.execute(query)
            else:
                cursor.execute(query, (query_arg, ))
            # Fetch the query output and append to a list
            output = cursor.fetchall()
            query_result = []
            for row in output:
                query_result.append(row)    
        except Exception as e:
            print("ERROR while executing a query:", e)
            return []
        return query_result

    def change_to_IceCream(self, ic_list):
        '''
            DESCRIPTION: Given a list of ice creams (strings), turns it into a list
            of IceCream objects so that it is easy to manipulate, and then returns 
            the list.
            PARAMS: ic_list - a list of ice creams to be changed (represented by strings)
            RETURNS: icecream_list - a list of ice creams (repreented by IceCream objects)
        '''
        icecream_list = []
        for ic in ic_list:
            # Obtain a list of reviews that correspond this ice cream's key
            reviews_list = self.get_reviews(ic[1])
            reviews = []
            # Change each reviews in Review object
            for review in reviews_list:
                reviews.append(Review(review[1], review[2], review[3], review[4]))
            # Change this ice cream 
            icecream_list.append(IceCream(ic[1], ic[2], ic[3], ic[4], ic[5], ic[6], reviews))
        return icecream_list

    def search_by_brands(self, brand_name):
        '''
            DESCRIPTION: Return a list of ice creams from the "brand_name" brand. It first
            creates a query that gets matching ice creams from the "prducts" table and uses execute_query()
            to execute it.
            PARAMS: brand_name - a string indicating the name of the brand
            RETURNS: output - a list output by the execute_query()
        '''
        query = "SELECT * FROM products WHERE brand = %s"
        query_result = self.execute_query(query, brand_name)
        return self.change_to_IceCream(query_result)

    def search_by_ratings(self, rating):
        '''
            DESCRIPTION: Return a list of ice creams whose rating is equal to "rating" or higher. 
            It first creates a query that gets matching ice creams from the "prducts" table 
            and uses execute_query() to execute it.
            PARAMS: rating - a decimal indicating the rating
            RETURNS: output - a list output by the execute_query()
        '''
        query_result = []
        try:
            if float(rating) >= 0:
                query = "SELECT * FROM products WHERE rating >= %s"
                query_result = self.execute_query(query, rating)
        except:
            return []
        return self.change_to_IceCream(query_result)
    
    def sort_by_ratings(self, number):
        '''
            DESCRIPTION: Return a list of ice creams that are included top "number" rated ice creams. 
            It first creates a query that gets matching ice creams from the "prducts" table 
            and uses execute_query() to execute it.
            PARAMS: number - a decimal indicating how many top rated ice creams user wants to display
            RETURNS: output - a list output by the execute_query()
        '''
        query_result = []
        try:
            if int(number) > 0:
                query = "SELECT * FROM products ORDER BY rating DESC LIMIT %s"
                query_result = self.execute_query(query, number)
        except:
            query_result = []
        return self.change_to_IceCream(query_result)

    def search_by_keyword(self, keyword):
        '''
            DESCRIPTION: Return a list of ice creams whose name contains "keyword". 
            It first creates a query that gets matching ice creams from the "prducts" table 
            and uses execute_query() to execute it.
            PARAMS: keyword - a string indicating the keyword on which the search is based
            RETURNS: output - a list output by the execute_query()
        '''
        query = "SELECT * FROM products WHERE LOWER(ic_name) LIKE %s"
        query_result = self.execute_query(query, '%'+keyword.lower()+'%')
        return self.change_to_IceCream(query_result)
    
    def search_by_name(self, name):
        '''
            DESCRIPTION: Return a list of ice creams whose name is "name". 
            PARAMS: name - a string indicating the name of ice cream
            RETURNS: output - a single-element list output by the execute_query()
        '''
        query = "SELECT * FROM products WHERE ic_name = %s"
        query_result = self.execute_query(query, name)
        return self.change_to_IceCream(query_result)

    def random_ice_cream(self):
        '''
            DESCRIPTION: Return a randomly selected ice cream 
            PARAMS: NONE
            RETURNS: icecream - a randomly slected icecream IceCReam() object
        '''
        query = "SELECT * FROM products ORDER BY RANDOM() LIMIT 1"
        query_result = self.execute_query(query)
        return self.change_to_IceCream(query_result)[0]

    def get_reviews(self, brand_key):
        '''
            DESCRIPTION: Given a brand key of some ice cream, returns a list of the 
            corresponding reviews. 
            PARAMS: ic_name - a string indicating the brand key of the ice cream
            RETURNS: output - a list output by the execute_query()
        '''
        query = "SELECT * FROM reviews WHERE brand_key = %s"
        return self.execute_query(query, brand_key)