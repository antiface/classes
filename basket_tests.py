# coding=utf-8
# unit tests for basket program
import unittest

# import the product and basket class basket module(basket.py)
from basket import Product, Basket

# define class for basket module
class Basket_tests(unittest.TestCase):

    # define setUp for tests
    def setUp(self):
        self.product = Product("Lego1", "Lego Toy", 2.50)
        self.basket = Basket()

    # create test for instance of Product class
    def product_instance_test(self):
        # create instance of product with name, description, and price attribute
        self.product = Product("test", "This is a sample", 2.50)
        # verify attributes of instance of product
        self.assertEqual("test", self.product.name)
        self.assertEqual("This is a sample", self.product.description)
        self.assertEqual(2.50, self.product.price)

    # create test for instance of Basket class
    def basket_instance_test(self):
        # create instance of basket class
        self.basket = Basket()

    # create test to display product details
    def display_product_details_test(self):
        result = self.product.display_product_details()
        self.assertEqual("Product name: Lego1, Desc: Lego Toy, Price: £2.50", result)

    # create test to add a product to the basket
    def add_product_to_basket_test(self):
        result = self.basket.add_product(self.product)
        self.assertEqual(["Lego1", "Lego Toy", 2.50], result)

    # create a test to add product using a dictionary as the container
    def add_prod_to_basket_test(self):
        result = self.basket.add_prods(self.product, 5)
        self.assertEqual({1:["Lego1", "Lego Toy", 2.50, 5]}, result)

    # create test to remove product item from basket items
    def remove_item_from_basket_test(self):
        # add product to basket first
        self.basket.add_prods(self.product)
        result = self.basket.remove_item(self.product)
        self.assertEqual({}, result)