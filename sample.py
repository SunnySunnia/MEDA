# -*- coding: utf-8 -*-
"""
Yelp API v2.0 code sample.

This program demonstrates the capability of the Yelp API version 2.0
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.

Please refer to http://www.yelp.com/developers/documentation for the API documentation.

This program requires the Python oauth2 library, which you can install via:
`pip install -r requirements.txt`.

Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
import argparse
import json
import pprint
import sys
import urllib
import urllib2

import oauth2


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'
bounds='37.748060,-122.424754'|'37.768723,-122.406472'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = 'YHCrqm_IqYkgHPBqo9EQxg'
CONSUMER_SECRET = 'En-U8vg4KoOxneV9aZIWYjaQp20'
TOKEN = '4nYh93QiTtcug1LXAkb3UjXin_GkYKs0'
TOKEN_SECRET = '1PLw3FQyAz84B-3tA8XH49uoWUI'


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

#def search(term, location):
#    """Query the Search API by a search term and location.
#
#    Args:
#        term (str): The search term passed to the API.
#        location (str): The search location passed to the API.
#
#    Returns:
#        dict: The JSON response from the request.
#    """
    
 #   url_params = {
  #      'term': term.replace(' ', '+'),
 #       'location': location.replace(' ', '+'),
 #       'limit': SEARCH_LIMIT
 #   }
 #   print url_params
 #   return request(API_HOST, SEARCH_PATH, url_params=url_params)


def search(term, bounds):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    
    url_params = {
        'term': term.replace(' ', '+'),
        'bounds': bounds.replace(' ', '%'),
        'limit': SEARCH_LIMIT
    }
    print url_params
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def get_business(business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)

def query_api(term, bounds):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, bounds)

    businesses = response.get('businesses')

    if not businesses:
        print u'No businesses for {0} in {1} found.'.format(term, bounds)
        return

    for index in range(len(businesses)):

        business_id = businesses[index]['id']

        #print u'{0} businesses found, querying business info for the top result  ...'.format(len(businesses),business_id)

        response=get_business(business_id)

        print 'Result for business "{0}" found:'.format(business_id)
        pprint.pprint(response, indent=3)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM, type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--bounds', dest='bounds', default=bounds, type=int, help='Search bounds(default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.bounds)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))


if __name__ == '__main__':
    main()

