'''
    File@ ice_cream.py
    Author@ Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, and Charlie Ney
    Course@ CS 257, Software Design, Prof Anya Vostinar
'''

import csv
from os import path

class IceCream:
    def __init__(self, reviews_file_name, brand_key='', name='', description='', 
                avg_rating=None, rating_count=None, ingredients=''):
        self.brand_key = brand_key 
        self.name = name 
        self.description = description
        self.avd_rating = avg_rating
        self.rating_count = rating_count
        self.ingredients = ingredients
        self.reveiws = self.get_reviews(reviews_file_name)

    '''
        Returns a list of reviews for this ice cream. Read the file named 
        review_file_name and iterate through it to fetch reviews for this ice
        cream. Each element of this returning list is Review object that 
        contains its attributes.
    '''
    def get_reviews(self, reviews_file_name):
        path_name = '../Data/' + reviews_file_name
        file_path = path.relpath(path_name)
        reviews_file = open(file_path, 'r')
        reader = csv.reader(reviews_file)
        next(reader)
        reviews_list = []

        for line in reader:
            if line[1] == self.brand_key:
                review = Review(line[4], line[8], line[3])
                reviews_list.append(review)
        
        reviews_file.close()

        return reviews_list

class Review:
    def __init__(self, rating=None, comment='', date=None):
        self.rating = rating
        self.comment = comment
        self.date = date

class DataSource:
    def __init__(self, products_file_name):
        #First, we need to make a nest list using products_file_name and IceCream class
        print('Not Yet Implemeted')

    #Brand Search
    def is_valid_brand_input(input):
        #True if input is valid
        #False if otherwise
        print('Not Yet Implemeted')

    def search_by_brands():
        print('Not Yet Implemeted')

    #Rating Search
    def is_valid_rating_input(input):
        #True if input is valid
        #False if otherwise
        print('Not Yet Implemeted')

    def search_by_ratings():
        print('Not Yet Implemeted')

    #Sort by rating and output top 10 (both overall & each brand)
    def is_valid_brand_input(input):
        print('Not Yet Implemeted')

    def sort():
        print('Not Yet Implemeted')

def main():
    print('Not Yet Implemeted')

if __name__=='__main__':
    main()