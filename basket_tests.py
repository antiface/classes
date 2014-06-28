# unit tests for basket program
import unittest

# import the product and basket class basket module(basket.py)
from basket import Product, Basket

# define class for basket module
class Basket_tests(unittest.TestCase):

    # define setUp for tests
    def setUp(self):
        self.product = Product()
        self.basket = Basket()

    