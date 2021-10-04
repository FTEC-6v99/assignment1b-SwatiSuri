# Create a function called: calc_avg_rating
# Parameters: the function should receive 1 parameter: a list of review objects
#             Remember a list can contain duplicates, so you can expect multiple reviews for the same restaurant
# Returns: the function should return a dictionary with restaurant name as key and average rating as value
#
#
# If the list of reviews is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value
from Review import review
from utils import  cal_avg_rating

def cal_avg_rating(reviews: list[review]) -> dict[int, float]:
    restaurant_rating ={}
    total_ratings = {}      
    if reviews == none:
       return {}
    for review in reviews:
        if review.getrestaurant() in restaurant_rating.keys():
           restaurant_rating[review.getrestaurant()] += review.getrating()
           total_ratings[review.getrestaurant()] += 0 
        else:
            restaurant_rating[review.getrestaurant()] = review.getrating()
            total_ratings[review.getrestaurant()] = 0
    for restaurant in restaurant_rating.keys():
        restaurant_rating[restaurant] = round((restaurant_rating[restaurant])/total_ratings[restaurant],2)
    return restaurant_rating
