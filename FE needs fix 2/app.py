'''
    @assignment: Front End Team D Assignment
    @author: Daisuke Yamada, Shoko Ishikawa, Jake Jasmer, Chrlie Ney
    @course CS257, Softare Design
    @usage: To run this program please use:

                python3 app.py

            while having html "templates" folder and the javascript/css/images 
            "static" folder in the same directory as this file. 
'''
from flask import Flask, render_template, request
import ice_cream as ic
from os import system
app = Flask(__name__)
system('clear')
print('Processing.....')
ic_data_source = ic.DataSource('products.csv', 'reviews.csv')
system('clear')

@app.route('/')
def homepage():
    '''
        DESCRIPTION: Creates a route for the homepage and returns/uses render_template to 
                     display the page content 
        PARAMETERS: NONE
        RETURNS: page rendered by the html file 'homepage.html'
    '''
    random_ic_link = request.base_url + 'ic_name=' + ic_data_source.random_ice_cream().name
    return render_template('homepage.html', random_ic_link=random_ic_link)

@app.route('/feature=rating_sort')
def sort_result_page():
    '''
        DESCRIPTION: Creates a route to the ice creams sort result page that displays
                     a list of ice creams resulted from a user's search. This function is used 
                     when user uses rating sort to get ice creams
        PARAMETERS: None
        RETURNS: page rendered by the html file 'result.html' 
    '''
    input = request.args["input"]
    ic_list = ic_data_source.sort_by_ratings(input)
    random_ic_link = request.root_url + 'ic_name=' + ic_data_source.random_ice_cream().name
    return render_template('result.html', header1="Top " + input + " Ice Creams" , ic_list=ic_list,\
        random_ic_link=random_ic_link)

@app.route('/feature=<feature>/input=<input>')
def search_result_page(feature, input):
    '''
        DESCRIPTION: Creates a route to the ice creams search result page that displays
                     a list of ice creams resulted from a user's search. This function is used 
                     when user uses brand_search and rating_search to get ice creams.
        PARAMETERS: feature - a string indicating search feature (either brand_search or rating_search)
                    input - a string indicating user's input keyword used for their search
        RETURNS: page rendered by the html file 'result.html' 
    '''
    header1 = ''
    ic_list = []
    if feature == 'brand_search':
        ic_list = ic_data_source.search_by_brands(input)
        if input == 'bj':
            header1 = 'Ben & Jerry\'s'
        elif input == 'hd':
            header1 = 'Häagen-Dazs'
        elif input == 'talenti':
            header1 = 'Talenti'
        elif input == 'breyers':
            header1 = 'Breyers'
    elif feature == 'rating_search':
        ic_list = ic_data_source.search_by_ratings(input)
        header1 = input + '-Star Ice Creams'

    random_ic_link = request.root_url + 'ic_name=' + ic_data_source.random_ice_cream().name
    return render_template('result.html', header1=header1, ic_list=ic_list,\
        random_ic_link=random_ic_link)


@app.route('/feature=keyword_search')
def keyword_search_result_page():
    '''
        DESCRIPTION: Creates a route to the ice creams search result page that displays
                     a list of ice creams resulted from a user's search. This function is used 
                     when user uses the search bar to do keyword_search.
        PARAMETERS: NONE
        RETURNS: page rendered by the html file 'result.html'
    '''
    input = request.args["keyword"]
    ic_list = ic_data_source.search_by_keyword(input)
    random_ic_link = request.root_url + 'ic_name=' + ic_data_source.random_ice_cream().name
    return render_template('result.html', header1='Keyword: '+input, ic_list=ic_list,\
        random_ic_link=random_ic_link)
    
@app.route('/ic_name=<name>')
def ice_cream_page(name):
    '''
        DESCRIPTION: Creates another route to the individual ice cream page. This route will be 
                    used when a user clicks/types the link directly rather than using the search bar. 
        PARAMETERS: name - a string indicating the name of specific ice cream 
        RETURNS: page rendered by the html file 'ice_cream.html'
    '''
    ic_list = ic_data_source.search_by_name(name)
    if ic_list == []:
        return render_template('error.html')
    ic = ic_list[0]
    image = '..\static\photos\\' + ic.brand_key + '.png'
    random_ic_link = request.root_url + 'ic_name=' + ic_data_source.random_ice_cream().name
    return render_template('ice_cream.html', image=image, ic=ic,\
        random_ic_link=random_ic_link)

@app.errorhandler(404)
def page_not_found(e):
    '''
        DESCRIPTION: Creates a route to the 404 error page. 
        PARAMETERS: e - a signal that evokes the error
        RETURNS: output - rendered by the html file 'error.html'
    '''
    random_ic_link = request.root_url + 'ic_name=' + ic_data_source.random_ice_cream().name
    return render_template('error.html', random_ic_link=random_ic_link)

@app.errorhandler(500)
def python_bug(e):
    '''
        DESCRIPTION: Creates a route to the 500 error page. 
        PARAMETERS: e - a signal that evokes the error
        RETURNS: output string
    '''
    return '500 Error: Internal Issue'

if __name__ == '__main__':
    app.run()