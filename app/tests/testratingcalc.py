# Use unittest library to create a unit test method to test the calc_avg_rating function created in the ratingscalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
from src.Review import review
from src.ratingscalc import cal_avg_rating
import unittest as ut
class test_rating(ut.TestCase):

    def test_cal_avg_rating(self):
        reviews = []
        reviews.append(review('HappyPlace', 'Best Restaurant To Eat', 'Great', 5))
        reviews.append(review('Pizzzaaa', 'Best Restaurant To Eat', 'Bad', 1))
        reviews.append(review('sweetworld', 'Best Restaurant To Eat', 'ok', 2.5))
        reviews.append(review('goodtimes', 'Best Restaurant To Eat', 'worst', 0))
    result = cal_avg_rating(reviews)
    self.assertEqual(0, result(rating))
