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

    # create test to add product to basket
    def add_product_to_basket_test(self):
        self.basket.add_product(self.product)
        # display items in basket and compare the expected results
        for key, item in self.basket.basket.items():
            self.assertEqual("Lego", item.name)
            self.assertEqual("Test Lego toy", item.description)
            self.assertEqual(4.55, item.price)
            self.assertEqual(1, item.quantity)

    # create test to remove item from basket
    def remove_product_from_basket_test(self):
        # first add item to basket and confirm item in basket
        self.basket.add_product(self.product)
        self.assertEqual(1, len(self.basket.basket))
        # then remove item from basket and confirm item removed from basket
        self.basket.remove_product(self.product)
        self.assertEqual(0, len(self.basket.basket))

    # create test to raise name error if product not in basket
    def raise_error_if_item_not_in_basket_test(self):
        self.assertRaises(NameError, self.basket.remove_product, self.product)

    # create test to update quantity of product in basket
    def update_product_quantity_in_basket_test(self):
        # first add product to basket
        self.basket.add_product(self.product)
        # update the quantity of the product in the basket
        for key, item in self.basket.basket.items():
            if self.product.name == item.name:
                self.basket.update_product_quantity(self.product, 3)
                self.assertEqual(3, item.quantity)

    # create test to raise exception if non-integer is passed as quantity when adding product to basket
    def add_product_to_basket_quantity_test(self):
        # add product to basket and specify quantity which is a non-integer
        self.assertRaises(ValueError, self.basket.add_product, self.product, "2")

    # create test to raise exception if update quantity is not between 1-50
    def update_product_quantity_value_test(self):
        # first add product to basket
        self.basket.add_product(self.product)
        # raise value error if quantity specified is not between 1-50
        self.assertRaises(ValueError, self.basket.update_product_quantity, self.product, "3")