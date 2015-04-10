from yelpapi import YelpAPI
import argparse

yelp_api = YelpAPI('YHCrqm_IqYkgHPBqo9EQxg', 'En-U8vg4KoOxneV9aZIWYjaQp20', 'tLJOWY-6farmlNePqXo_1r3lzI1wJPoi', 'X6S7BdmgaX18Z0cw7sLvnMruNJk')


###asking for input in terminal, but didnt get it work yet#####
#parser = argparse.ArgumentParser(description='Example')
#parser.add_argument('term', type=str, help='Search term (default: %(default)s)')
#parser.add_argument('location',  type=str, help='Search location (default: %(default)s)')
#input_values = parser.parse_args()
#response = yelp_api.search_query(term=input_values.term, location=input_values.location, sort=2, limit=20)


####Can input user information here:####
mterm='Ice Cream'
mlocation='Mission District, San Francisco, CA'
#Sort by: 0=Best matched, 1=Distance, 2=Highest Rated
msort=2
mlimit=20


print 'Searching','\t', mterm, '\t', 'in','\t', mlocation
response = yelp_api.search_query(term=mterm, location=mlocation, sort=msort, limit=mlimit)

print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
for business in response['businesses']:
    print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'],
                                                                           business['review_count'], ', '.join(business['location']['display_address'])))







print('\n-------------------------------------------------------------------------\n')


####user input information here:####
mcategory='bikerentals'
#Categories can be found: https://www.yelp.com/developers/documentation/v2/all_category_list
mbounds='37.769164,-122.424754|37.768723,-122.406472'
#Sort by: 0=Best matched, 1=Distance, 2=Highest Rated
msort=2
mlimit=20

"""
    Example search by bounding box and category. See http://www.yelp.com/developers/documentation/v2/all_category_list for an official
    list of Yelp categories. The bounding box definition comes from http://isithackday.com/geoplanet-explorer/index.php?woeid=12587707.

Sunny: bounding box for Mission distric: 37.769164,-122.424754|37.768723,-122.406472
"""
print 'Searching','\t',mcategory, 'in','\t', mbounds,'\n', "yelp_api.search_query(category_filter=", mcategory,'bounds=', mbounds,')'
response = yelp_api.search_query(category_filter=mcategory, bounds=mbounds, limit=20)
for business in response['businesses']:
    print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'],
                                                                           business['review_count'], ', '.join(business['location']['display_address'])))








print('\n-------------------------------------------------------------------------\n')

"""
    Example business query. Look at http://www.yelp.com/developers/documentation/v2/business for
    more information.
"""

####user can input business id here:
mid='amys-ice-creams-austin-3'

print "***** selected reviews for", mid, "*****", '\n',  "yelp_api.business_query(id=",mid,')'
business = yelp_api.business_query(id=mid)
for review in business['reviews']:
    print('rating: %d\nexcerpt: %s\n' % (review['rating'], review['excerpt']))

print('\n-------------------------------------------------------------------------\n')






"""
    Example erronious search query.
"""
print('***** sample erronious search query *****\n%s\n' % "yelp_api.search_query(term='ice cream', location='austin, tx', sort=3)")
try:
    # sort can only take on values 0, 1, or 2
    yelp_api.search_query(term='ice cream', location='austin, tx', sort=3)
except YelpAPI.YelpAPIError as e:
    print(e)

print('\n-------------------------------------------------------------------------\n')


"""
    Example erronious business query.
"""
print('***** sample erronious business query *****\n%s\n' % "yelp_api.business_query(id='fake-business')")
try:
    yelp_api.business_query(id='fake-business')
except YelpAPI.YelpError as e:
    print(e)
