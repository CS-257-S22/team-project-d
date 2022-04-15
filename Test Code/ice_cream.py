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
        self.reviews = self.get_reviews(reviews_file_name)

    '''
        Returns a list of reviews for this ice cream. Read the file named 
        review_file_name and iterate through it to fetch reviews for this ice
        cream. Each element of this returning list is Review object that 
        contains its attributes.
    '''
    def get_reviews(self, reviews_file_name):
        file_path = path.relpath('../Data/' + reviews_file_name)
        reviews_file = open(file_path, 'r')
        reader = csv.reader(reviews_file)
        next(reader)
        reviews_list = []

        for line in reader:
            if line[1] == self.brand_key:
                # rating
                review_rating = -1
                if line[4] != '':
                    review_rating = int(line[4])

                review = Review(review_rating, line[8], line[3])
                reviews_list.append(review)
        
        reviews_file.close()

        return reviews_list

class Review:
    def __init__(self, rating=None, comment='', date=''):
        self.rating = int(rating)
        self.comment = comment
        self.date = date

class DataSource:
    def __init__(self, products_file_name, reviews_file_name):
        file_path = path.relpath('../Data/' + products_file_name)
        reviews_file = open(file_path, 'r')
        reader = csv.reader(reviews_file)
        next(reader)
        ice_cream_data_source = [[],[],[],[]] # nested list containing ice creams, sorted by barnds (as a list)
    
        for line in reader:
            # brand key
            ice_cream_key = line[1]
            # average rating
            ice_cream_avg_rating = -1
            if line[5] != '':
                ice_cream_avg_rating = float(line[5])
            # rating count
            ice_cream_ratings_count = -1
            if line[6] != '':
                ice_cream_ratings_count = float(line[6])
            
            # make an IceCream instance and append to the list
            ice_cream = IceCream(reviews_file_name, ice_cream_key, line[2], line[4], 
                                ice_cream_avg_rating, ice_cream_ratings_count, line[7])
            if ice_cream_key[-2:] == 'bj':
                ice_cream_data_source[0].append(ice_cream)
            elif ice_cream_key[-2:] == 'hd':
                ice_cream_data_source[1].append(ice_cream)
            elif ice_cream_key[-2:] == 'ti':
                ice_cream_data_source[2].append(ice_cream)
            else:
                ice_cream_data_source[3].append(ice_cream)
    
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