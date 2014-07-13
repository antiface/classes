# coding=utf-8
# unit tests for basket4.py

import unittest
from basket4 import Basket, Product

# create class for unit tests for Basket4.py
class BasketTests(unittest.TestCase):

    # assign instance of Product and Basket classes to variables for setUp
    def setUp(self):
        self.product = Product("Lego1", "Test Lego Toy", 7.50)
        self.basket = Basket()

    # create test to add product to basket adding the quantity as a separate dictionary key item
    def add_product_to_basket_test(self):
        # add product without specifying quantity which adds a default quantity of 1
        self.basket.add_product(self.product)
        # check for product item and quantity values in basket (dictionary)
        for item, quantity in self.basket.basket_items.values():
            self.assertEqual("Lego1", item.name)
            self.assertEqual(7.50, item.price)
            # check quantity = 1
            self.assertEqual(1, quantity)

    # create test to remove product from basket
    def remove_product_from_basket_test(self):
        # first add product to basket
        self.basket.add_product(self.product)
        # confirm item added to basket
        self.assertEqual(1, len(self.basket.basket_items))
        self.basket.remove_product(self.product)
        self.assertEqual(0, len(self.basket.basket_items))

    # create test to update quantity of product
    def update_product_quantity_test(self):
        # first add product to basket and specify quantity
        self.basket.add_product(self.product, 2)
        # update product quantity to 3
        self.basket.update_product_quantity(self.product, 3)
        # verify product quantity has been updated
        for item, quantity in self.basket.basket_items.values():
            self.assertEqual(3, quantity)
