import json
import unittest
import os
import requests

#
# Your name:
# Who you worked with:
#

# generating personal API key is not requested here

def read_cache(CACHE_FNAME):
    '''
    Loads a JSON cache from CACHE_FNAME if it exists
    
    Parameters
    ----------
    CACHE_FNAME: string
        the name of the cache file to read in
    
    Returns
    -------
    dict
        if the cache exists, a dict with loaded data
        if the cache does not exist, an empty dict
    '''
    pass

def write_cache(CACHE_FNAME, CACHE):
    '''
    Encodes CACHE_DICT into JSON format and writes
    the JSON to CACHE_FNAME to save the search results

    NOTE: When you write cache into JSON format, you need 
    to unpack the second item of your dictionary, which is 
    the actual content of your item. For example: 

    {'resultCount': 2, 'results': [{*INFORMATION ABOUT EACH ITEM*}, {*INFORMATION ABOUT EACH ITEM*}]}

    In the above case, the resultCount is 2 because we set the 
    limit number to be 2. For this assignment, you expect to have resultCount to be 1. 
    
    Parameters
    ----------
    CACHE_FNAME: string
        the name of the file to write a cache to
    
    Returns
    -------
    None
        does not return anything
    '''   
    pass
    

def create_request_url(term, number=1):
    '''
    Builds a request url for an API call 
    API documentation can be found here: 
    https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html

    NOTE: consider using a formatted string (f-string)!

    Parameters
    ----------
    term: str
        a string to search in SWAPI
    
    Returns
    -------
    None
    str
        a search url for the SWAPI API
    '''
    pass
    
def get_data_with_caching(term, CACHE_FNAME):
    '''
    Uses the passed search generate a request_url using 
    the 'create_request_url' function

    If url is found in the dict return by `read_cache`, prints 
    "Using cache for {search}" and returns the url results

    If url is found in the dict return by `read_cach`, prints 
    "Fetching data for {search}" and makes a call to SWAPI to 
    get the data the search

    If request is successful, add the data to a dictionary (key is 
    the request_url, and value is part of the results) and writes
    out the dictionary to cache using `write_cache`

    Parameters
    ----------
    search: str
        a string to search in SWAPI
    CACHE_FNAME: str
        the name of the file to write a cache to
    
    Returns
    -------
    url result:
        results of a url request either from the cache or website
    None:
        if search is unsuccessful 
    '''
    pass

def sort_price(CACHE_FNAME):
    '''
    Sorts a list of iTunes collections from
    the cache by price in ascending order, 
    returning the 5 most expensive products

    Parameters
    ----------
    CACHE_FNAME: str
        the name of the cache file to read from

    Returns
    -------
    tuple
        the name of the top 5 most expensive collections
        in the iTunes cache and its price like so:
        [('collection name', 0.0), ('collection name', 0.0)]
    '''
    pass

#######################################
############ EXTRA CREDIT #############
#######################################

def itunes_counts(CACHE_FNAME):
    '''
    Reads cache file and creates a dictionary
    with a genre name as the key and the number of 
    genre occurrences as the value, then sorts the
    dictionary in descending order, returning the 
    3 most frequent genres in the dict

    Parameters
    ----------
    CACHE_FNAME
        the name of the cache to read
    
    Returns
    -------
    dict
        a dict with the three most frequent genres 
        and their counts sorted in ascending order
    '''
    pass


####################
#### TEST CASES ####
####################

class TestHomework6(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.CACHE_FNAME = dir_path + '/' + "cache_itunes.json"
        self.term_list = ["olivia+rodrigo", "ariana+grande", "drake", "tame+impala", "selena+gomez", "bruno+mars", "calvin+harris", "lorde", "imagine+dragons", "taylor+swift", "justin+bieber", "adele", "cage+the+elephant", "kanye+west", "britney+spears", "annavento", "ericayan"]
        self.cache = read_cache(self.CACHE_FNAME)

    def test_write_cache(self):
        write_cache(self.CACHE_FNAME, self.cache)
        dict1 = read_cache(self.CACHE_FNAME)
        self.assertEqual(dict1, self.cache)

    def test_create_request_url(self):
        for m in self.term_list:
            self.assertIn("term={}".format(m),create_request_url(m))
            self.assertIn("limit=1",create_request_url(m))
            self.assertNotIn("r=json",create_request_url(m))
            

    def test_get_data_with_caching(self):
        for m in self.term_list:
            dict_returned = get_data_with_caching(m, self.CACHE_FNAME)
            if dict_returned:
                self.assertEqual(type(dict_returned), type({}))
                self.assertIn(create_request_url(m),read_cache(self.CACHE_FNAME))
            else:
                self.assertIsNone(dict_returned)       
        self.assertEqual(json.loads(requests.get(create_request_url(self.term_list[0])).text)["results"][0],read_cache(self.CACHE_FNAME)[create_request_url(self.term_list[0])])

    def test_price(self):
        # IMPLEMENT
        pass

    def test_itunes_counts(self):
        self.assertEqual(itunes_counts(self.CACHE_FNAME), 
                        {'Pop': 6,
                         'Alternative': 3,    
                         'Biographies & Memoirs': 2
                        })

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FNAME = dir_path + '/' + "cache_itunes.json"

    terms = ["olivia+rodrigo", "ariana+grande", "drake", "tame+impala", "selena+gomez", "bruno+mars", "calvin+harris", "lorde", "imagine+dragons", "taylor+swift", "justin+bieber", "adele", "cage+the+elephant", "kanye+west", "britney+spears", "annavento", "ericayan"]
    [get_data_with_caching(term, CACHE_FNAME) for term in terms]
    print("________________________")
    # Fetch the data for ColdPlay!
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_with_caching('cold+play', CACHE_FNAME)
    data2 = get_data_with_caching('cold+play', CACHE_FNAME)
    print("________________________")

    # Getting the data for Post Malone!
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_with_caching('post+malone', CACHE_FNAME)
    data2 = get_data_with_caching('post+malone', CACHE_FNAME)
    print("________________________")

    # Getting the data for The Beatles
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_with_caching('the+beatles', CACHE_FNAME)
    data2 = get_data_with_caching('the+beatles', CACHE_FNAME)
    print("________________________")

    print("Get CollectionPrice for first 5 items")
    print(sort_price(CACHE_FNAME))
    print("________________________")


    # Extra Credit
    # Keep the statements commented out if you do not attempt the extra credit
    print("EXTRA CREDIT!")
    print("Analyzing the distribution of item genres")
    # itunes_list() function does not take any parameters.
    print(itunes_counts(CACHE_FNAME))
    print("________________________")
    
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)
