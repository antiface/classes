# coding=utf-8

# refactored unit tests for basket2
import unittest
from basket2 import Product, Basket

# create class to run unit tests for the Product and Basket classes and methods
class BasketTests(unittest.TestCase):
    # add parameters needed for each test in setUp
    def setUp(self):
        # define instance Product and Basket classes
        self.product = Product("Lego", "Test Lego toy", 4.55)
        self.basket = Basket()

    # create test for the display details method for the Product class
    def display_product_details_test(self):
        # assign the result of the display_details method to a variable
        result = self.product.display_product_details()
        self.assertEqual("Product: Lego, Description: Test Lego toy, Price: £4.55", result)