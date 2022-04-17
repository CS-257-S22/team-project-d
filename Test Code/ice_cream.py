"""
    File@ ice_cream.py
    Author@ Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, and Charlie Ney
    Course@ CS 257, Software Design, Prof Anya Vostinar
"""

import sys
import csv
from os import path, system
from functools import reduce
from operator import attrgetter


class IceCream:
    def __init__(self, reviews_file_name, brand_key:str, name:str, description:str, 
                avg_rating:float, rating_count:int, ingredients:str):
        self.brand_key = brand_key
        self.name = name
        self.description = description
        self.avg_rating = avg_rating
        self.rating_count = rating_count
        self.ingredients = ingredients
        self.reviews = self.get_reviews(reviews_file_name)

    """
        Returns a list of reviews for this ice cream. Read the file named 
        review_file_name and iterate through it to fetch reviews for this ice
        cream. Each element of this returning list is Review object that 
        contains its attributes/fields.
    """
    def get_reviews(self, reviews_file_name):
        file_path = path.relpath("../Data/" + reviews_file_name)
        reviews_file = open(file_path, "r")
        reader = csv.reader(reviews_file)
        next(reader)
        reviews_list = []

        for line in reader:
            if line[1] == self.brand_key:
                # rating (if the column is empty)
                review_rating = -1
                if line[4] != "":
                    review_rating = int(line[4])

                review = Review(review_rating, line[8], line[3])
                reviews_list.append(review)
        
        reviews_file.close()

        return reviews_list
    """
        This is the default comparison method for python so that we can compare ice creams
    """
    def __eq__(self, other):
        return (self.brand_key == other.brand_key) and (self.name == other.name) \
        and (self.description == other.description) and (self.avg_rating == other.avg_rating) \
        and (self.rating_count == other.rating_count) and (self.ingredients == other.ingredients)

class Review:
    def __init__(self, rating:int, comment:str, date:str):
        self.rating = int(rating)
        self.comment = comment
        self.date = date


class DataSource:
    def __init__(self, products_file_name, reviews_file_name):
        file_path = path.relpath("../Data/" + products_file_name)
        reviews_file = open(file_path, "r")
        reader = csv.reader(reviews_file)
        next(reader)
        
        self.ice_cream_data_source = [[],[],[],[]] # nested list containing ice creams, sorted by brands (as a list)
    
        for line in reader:
            # brand key
            ice_cream_key = line[1]
            # average rating
            ice_cream_avg_rating = -1
            if line[5] != "":
                ice_cream_avg_rating = float(line[5])
            # rating count
            ice_cream_ratings_count = -1
            if line[6] != "":
                ice_cream_ratings_count = float(line[6])
            
            # make an IceCream instance and append it to the list
            ice_cream = IceCream(reviews_file_name, ice_cream_key, line[2], line[4], 
                                ice_cream_avg_rating, ice_cream_ratings_count, line[7])
            if ice_cream_key[-2:] == "bj":
                self.ice_cream_data_source[0].append(ice_cream)
            elif ice_cream_key[-2:] == "hd":
                self.ice_cream_data_source[1].append(ice_cream)
            elif ice_cream_key[-2:] == "ti":
                self.ice_cream_data_source[2].append(ice_cream)
            else:
                self.ice_cream_data_source[3].append(ice_cream)
    
    # Search by brands
    """
        Returns None if input is invalid. Returns the corresponding
        brand key of input if input is valid. 
    """
    def is_valid_brand_input(self, input) -> str:
        bj_list = ["bj", "ben and jerry's", "b&j", "ben and jerrys", "BJ", "Ben and Jerry's", "B&J", "Ben and Jerrys"]
        hd_list = ["hd", "haagen-dazs", "haagen dazs", "Haagen Dazs", "Haagen-Dazs"]
        breyers_list = ["breyers", "Breyers"]
        talenti_list = ["talenti", "Talenti"]
        if input in bj_list:
            return "bj"
        elif input in hd_list:
            return "hd"
        elif input in talenti_list:
            return "ti"
        elif input in breyers_list:
            return "br"

        return None

    """
        Returns a list of ice creams from the brand specified by 
        input. Returns an empty list if input is not valid.
    """
    def search_by_brands(self, input):
        brand = self.is_valid_brand_input(input)

        result = []
        if brand == None:
            print("ERROR: invalid brand name - please try again!")
        elif brand == "bj":
            result = self.ice_cream_data_source[0]
        elif brand == "hd":
            result = self.ice_cream_data_source[1]
        elif brand == "ti":
            result = self.ice_cream_data_source[2]
        else:
            result = self.ice_cream_data_source[3]
        return result
            
    # Search by ratings
    """
        Returns -1 if input is invalid (not a number between 0 and 5 - can be float). 
        Returns int type version of input if it is valid. 
    """
    def is_valid_rating_input(self, input) -> int:
        input_num = -1
        try:
            if 0 <= float(input) and float(input) <= 5:
                input_num = float(input)
        except ValueError:
            print("ERROR: invalid number - please try again!")
        return input_num
        
    """
        Returns a list of ice creams with the rating greater than or
        equal to input.
    """
    def search_by_ratings(self, input):
        rating = self.is_valid_rating_input(input)
        result = []

        if rating == -1:
            return result
        for brand in self.ice_cream_data_source:
            for ic in brand:
                if ic.avg_rating >= rating:
                    result.append(ic)
        
        return result
    
    # Search by ingredients
    """
        Returns a list of ice creams with the rating greater than or
        equal to input.
    """
    def search_by_ingredients(self, input):
        print("Not Yet Implemeted")

    '''
        Returns the list of top N=top_num ice creams sorted by their avg_ratings
    '''
    def sort_by_ratings(self, top_num):
        single_list = reduce(lambda x, y: x+y, self.ice_cream_data_source)
        try:
            top_num = int(top_num)
            if top_num < 0:
                print("ERROR: input out of range")
                return []
        except ValueError:
            print("ERROR: non-numeric input")
            return []

        result = sorted(single_list, key=attrgetter('avg_rating'), reverse=True)
        if len(single_list) >= top_num:
            result = result[0: top_num]

        return result
        
    '''
        Help function which provides descriptions and examples of functions
    '''
    def help(self):
        print("--------------------------------------------------------------------------------------")
        print("Functions:")
        print("\t-b(brand name")
        print("\tDescription: Use this function to search for a specific ice cream using its flavor name.")
        print()
        print("\t-r(rating)")
        print("\tDescription: Use this function to search for ice cream flavors that have a specified rating or higher.")
        print()
        print("\t-s(number of ice creams)")
        print("\t Description: Use this function to return of list of x ice creams with the highest reviews.")
        print("--------------------------------------------------------------------------------------")

'''
    Displays the resulting list's name, brand key, srats, and review count. We are omitting the 
    "description" and "ingredients" columns for simplicity, but we will still use these 
    information in the final product. 
'''
def display_result(list):
    for ic in list:
        print(ic.name, '|', ic.brand_key, '|', ic.avg_rating, 'stars |', ic.rating_count, "reviews")

def main():
    system("clear")
    if len(sys.argv) != 3:
        if len(sys.argv) == 1:
            # We're using simple one character functions because the end result will be cllicking on a 
            # button which won't involve the command line at all
            print("ERROR: No function entered, examples of functions include [-b], [-r], and [-s].")
        elif len(sys.argv) == 2:
            print("ERROR: No argument entered. Please give an argument to use for the method.")
        elif len(sys.argv) > 3:
            print("ERROR: Too many arguments entered.")
        print("Please refer to the help command [-help] for additional information")
        exit()
    print("Processing...")
    data_source = DataSource("products.csv", "reviews.csv")
    system("clear")
    if sys.argv[1] == "-b":
        display_result(data_source.search_by_brands(sys.argv[2]))
    elif sys.argv[1] == "-r":
        display_result(data_source.search_by_ratings(sys.argv[2]))
    elif sys.argv[1] == "-s":
        display_result(data_source.sort_by_ratings(sys.argv[2]))
    elif sys.argv[1] == "-help": 
        help()
    

if __name__=="__main__":
    main()