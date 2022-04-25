'''
    @assignment: Flask App Team Assignment
    @author: Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, Charlie Ney
    @course CS257, Softare Design
    @usage: To run this program please use:

                python3 flask_app.py

            while having html templates and ice_cream.py in the same directpry 
            as this file. It might take a few seconds to run as we have not implmented 
            our database. 
'''

from flask import Flask, render_template, request
import ice_cream as ic
from os import system

# Global Variables
app = Flask(__name__)
system('clear')
print('Processing....')
ic_data_source = ic.DataSource('products.csv', 'reviews.csv')
system('clear')

@app.route('/')
def homepage():
    '''
        DESCRIPTION: Making a route for the home page
        PARAMETERS: NONE
        RETURN: a formatted string rendered from 'homepage.html' file in templates
    '''
    header1 = 'Instructions for navigating our website:'
    header2 = 'Go to the following link to search ice creams: '
    b_url = request.base_url
    return render_template('homepage.html', header1=header1, header2=header2, link=b_url)  

def get_ice_creams(feature, input):
    '''
        DESCRIPTION: a helper funcion that uses ice_cream.py's functions to get a 
        list of ice creams
        PARAMETERS: 
                    feature - a string representing which feature a user wants to use
                    input - a string indicating the user's input
        RETURN: result - a list of icecream objects resulted from the specified feature
    '''
    result = []
    if feature == 'brand_search':
        result = ic_data_source.search_by_brands(input)
    elif feature == 'rating_search':
        result = ic_data_source.search_by_ratings(input)
    elif feature == 'rating_sort':
        result = ic_data_source.sort_by_ratings(input)
    return result

@app.route('/feature=<feature>/input=<input>')
def display_ice_creams(feature, input):
    '''
        DESCRIPTION: Making a route for the three features supported by our app
        PARAMETERS: 
                    feature - a string representing which feature a user wants to use
                    input - a string indicating the user's input
                    Both of these parameters are used for the route
        RETURN: output - a formatted string rendered from 'result.html' file in templates
    '''
    result = get_ice_creams(feature, input)
    return render_template('display_ice_creams.html', header1='Ice Creams', ic_list=result)

@app.errorhandler(404)
def page_not_found(e):
    ''''
        Handles the PAGE NOT FOUND error 
    '''
    error_number = 404
    message = 'Page Not Found'
    return render_template('error.html', error_number=error_number, message=message)

@app.errorhandler(500)
def python_bug(e):
    '''
        Handles the INTERNAL ERROR
    '''
    error_number = 500
    message = 'Page Unavaiable'
    return render_template('error.html', error_number=error_number, message=message)

if __name__ == '__main__':
    app.run()