"""
    File: ice_cream.py
    Author: Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, and Charlie Ney
    Course: CS 257, Software Design, Prof Anya Vostinar
    Description: This program takes in two csv files of 241 ice creams 
    and their reviews and load the datasets as a nested list. It allows user 
    to interact with the datasets to get information about ice creams (details are provdided
    in usage statement below). 
"""

import sys
import csv
from os import path, system
from functools import reduce
from operator import attrgetter
import random

class IceCream:
    def __init__(self, reviews_file_name, brand_key:str, name:str, description:str, 
                avg_rating:float, rating_count:int, ingredients:str):
        self.brand_key = brand_key
        self.name = name
        self.description = description
        self.avg_rating = avg_rating
        self.avg_rating_int = int(avg_rating)
        self.avg_rating_decimal = avg_rating-int(avg_rating)
        self.rating_count = rating_count
        self.ingredients = ingredients
        self.reviews = self.get_reviews(reviews_file_name)

    def get_reviews(self, reviews_file_name):
        """
            @description: Returns a list of reviews for this ice cream. Read the file named 
            review_file_name and iterate through it to fetch reviews for this ice
            cream. Each element of this returning list is Review object that 
            contains its attributes/fields.
            @params: reviews_file_name - the name of the file containing the reviews
            @return: Reviews_list - the list of the reviews corresponding to this ice cream
        """
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

    def __eq__(self, other):
        """
            @description: This is the default comparison method for python so that we can 
            compare ice creams
            @params: self - this ice cream
                    other - the other ice cream to be compared
            @return: True if the two ice creams have the exact same set of fields
                    False if otherwsie
        """
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
        # load datasets and create a nested list 
        self.ice_cream_data_source = [[],[],[],[]] 
        self.load_products_data(products_file_name, reviews_file_name)
    
    # Loading data
    def load_products_data(self, products_file_name, reviews_file_name):
        """
            @description: Takes in products_file_name and load the data to create a nested
            list containing ice creams, where each inside list represents a brand 
            @params: products_file_name - a file containing 241 ice creams with details
                    reviews_file_name - a file containing reviews for each ice cream 
            @returns: None
        """
        file_path = path.relpath("../Data/" + products_file_name)
        reviews_file = open(file_path, "r")
        reader = csv.reader(reviews_file)
        next(reader)

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
                ice_cream_ratings_count = int(line[6])
            
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
    def is_valid_brand_input(self, input) -> str:
        """
            @description: Returns None if input is invalid. Returns the corresponding
            brand key of input if input is valid. 
            @params: input - a user input for brand search
            @return: brand_name - the brand name associated with input
                    None - if user input is not valid
        """
        bj_list = ["bj", "ben and jerry's", "b&j", "ben and jerrys", "BJ", "Ben and Jerry's", \
                    "B&J", "Ben and Jerrys"]
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

    def search_by_brands(self, input):
        """
            @description: Returns a list of ice creams from the brand specified by 
            input. Returns an empty list if input is not valid.
            @params: input - valid user input for brand search
            @return: result - a list containing ice creams from input brand
        """
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
    def is_valid_rating_input(self, input) -> int:
        """
            @description: Returns -1 if input is invalid (not a number between 0 and 5 - 
            can be float). Returns int type version of input if it is valid.
            @params: input - a user input for ratings search
            @return: float(input) - float type input for a valid input
                -1 - for invalid input
        """
        input_num = -1
        try:
            if 0 <= float(input) and float(input) <= 5:
                input_num = float(input)
            else:
                print("ERROR: input out of range - please try again!")
        except ValueError:
            print("ERROR: invalid number - please try again!")
        return input_num
        
    def search_by_ratings(self, input):
        """
            @description: Returns a list of ice creams with the rating greater than or
            equal to input.
            @params: input - a valid user input (float between 0 and 5)         
            @return: result - a list containing ice creams with rating higher or equal 
            to input
        """
        rating = self.is_valid_rating_input(input)
        result = []

        if rating == -1:
            return result
        for brand in self.ice_cream_data_source:
            for ic in brand:
                if ic.avg_rating >= rating:
                    result.append(ic)
        
        return result
 
    def sort_by_ratings(self, top_num):
        """
            @description: Returns the list of top N=top_num ice creams sorted by 
            their avg_ratings
            @params: top_num - a integer representing the number of best ice creams
            that a user wants to display
            @return: result - a list containing top top_num ice creams for valid input
                    [] - an empoty list for any invalid input
        """
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

    def search_by_name(self, name):
        """
            @description: Returns the specified ice cream with name
            @params: name - a string indicating the name of an ice cream
            @return: [ic] - the specified ice cream object in a list, returns [] if ice cream
                with the name does not exist (improvement needed)
        """
        for brand in self.ice_cream_data_source:
            for ic in brand:
                if ic.name == name:
                    return [ic]
        
        return []

    def random_ice_cream(self):
        """
            @description: Returns a randomly selected ice cream
            @params: None
            @return: randomly selected ice cream
        """
        r_brand = random.randint(0, 3)
        r_ic = 0
        if r_brand == 0:
            r_ic = random.randint(0, len(self.ice_cream_data_source[0])-1)
        elif r_brand == 1:
            r_ic = random.randint(0, len(self.ice_cream_data_source[1])-1)
        elif r_brand == 2:
            r_ic = random.randint(0, len(self.ice_cream_data_source[2])-1)
        else:
            r_ic = random.randint(0, len(self.ice_cream_data_source[3])-1)

        return self.ice_cream_data_source[r_brand][r_ic]

def usage():           
    """
        @description: Help function which provides descriptions and examples of functions
        @params: None
        @return: None
    """
    print("+----------------------------------------------------------------------------------+")
    print("|                                     USAGE                                        |")
    print("+----------------------------------------------------------------------------------+")
    print("  (1) -b [brand name]: Use this command to search for ice creams from a specific \
        \n       brand. We have ice creams across four different brands: Ben and Jerry's (bj), \
        \n       Haagen-Dazs (hd), Talenti, and Breyers. [brand name] should be an alias of \
        \n       either of these four brands.                               \
        \n\n                            (ex) python3 ice_cream.py -b bj")
    print()
    print("  (2) -r [rating]: Use this command to search for ice cream flavors that have a \
        \n       specified rating or higher. [rating] should be a float/integer between 0 and 5 \
        \n       inclusive.\
        \n\n                            (ex) python3 ice_cream.py -r 4.9")
    print()
    print("  (3) -s [top x]: Use this command to return a sorted list of x ice creams with \
        \n       the highest reviews. We have 241 ice creams in total, and thus [top x] \
        \n       needs to be an integer between 0 and 241 inclusive. \
        \n\n                            (ex) python3 ice_cream.py -s 50")
    print("+---------------------------------------------------------------------------------+")

def display_result(list):
    """
        @description: Displays the resulting list's name, brand key, srats, and review count. 
        We are omitting the "description" and "ingredients" columns for simplicity, but we will
        still use these information in the final product. 
        @params: list - the list to be displayed
        @return: None
    """
    for ic in list:
        print(ic.name, '|', ic.brand_key, '|', ic.avg_rating, 'stars |', ic.rating_count, "reviews")

def main():
    system("clear")

    # no command arguments
    try:
        command = sys.argv[1]
    except IndexError:
        usage()
        exit()

    # undefined command arguments
    valid_commands = ["-b", "-r", "-s", "-n", '-ran'] 
    if len(sys.argv) != 3 or command not in valid_commands:
        usage()
        exit()

    print("Processing...")
    data_source = DataSource("dummy_products.csv", "dummy_reviews.csv")
    system("clear")
    result = []
    if command == "-b":
        result = data_source.search_by_brands(sys.argv[2])
    elif command == "-r":
        result = data_source.search_by_ratings(sys.argv[2])
    elif command == "-s":
        result = data_source.sort_by_ratings(sys.argv[2])   
    elif command == "-n":
        ic = data_source.search_by_name(sys.argv[2])
        print(ic.name, '|', ic.brand_key)
        exit(0)
    elif command == "-ran":
        ic = data_source.random_ice_cream()
        print(ic.name, '|', ic.brand_key)
        exit(0)
    display_result(result)

if __name__=="__main__":
    main()