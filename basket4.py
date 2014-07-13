# coding=utf-8
# refactor Basket and Product classes using quantity as a separate item in dictionary

class Product(object):

    # initialise class object with the following
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_product_details(self):
        '''
            Function that displays the product name, description and price
        '''
        return "Product: {0}, Description: {1}, Price: £{2:.2f}".format(self.name, self.description,
                                                                        self.price)

class Basket(object):

    # initialise instance of basket with an empty dictionary for items
    def __init__(self):
        self.basket_items = {}

    def add_product(self, product, quantity=1):
        '''
            This function adds a product to the basket. if the quantity is not specified, it adds 1 as default
        '''
        # set the product dictionary key to the name of the product
        product_name = product.name

        # add product to dictionary if product quantity specified is between 1 - 50, else raise error
        if (0 < quantity <= 50):
            self.basket_items[product_name] = (product, quantity)
        else:
            raise ValueError("Your product or quantity entered is not valid, please enter valid value(s)")

        return "{} product added to basket".format(product_name)

    def remove_product(self, product):
        '''
            Function removes a specific product from the basket
        '''
        product_name = product.name
        # check if product_name in basket and remove if found, if not raise an error
        if product_name in self.basket_items:
            del self.basket_items[product_name]
        else:
            raise ValueError("No such product in basket")

        return "{} product removed from basket".format(product_name)

    def update_product_quantity(self, product, quantity):
        '''
            Function updates the quantity of a specific product with a new specified quantity
        '''
        # set product name to variable
        product_name = product.name
        # if key in dictionary, update quantity
        if (product_name in self.basket_items) and (0 < quantity <= 50):
            #for product in self.basket_items:
            previous_quantity = self.basket_items[product_name][1]
            # update  product item in basket with quantity passed in
            self.basket_items[product_name] = (product, quantity)

        else:
            raise ValueError("Quantity entered is not valid, please enter a number between 1 - 50")

        return "{0} product quantity has been updated from {1} to {2}".format(product_name, previous_quantity, quantity)




