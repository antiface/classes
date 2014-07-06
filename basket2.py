# coding=utf-8
# Refactor Product and Basket classes

class Product(object):

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    # method to display product details
    def display_product_details(self):
        '''
            This method displays the name, description and price of a product
        '''
        return "Product: {0}, Description: {1}, Price: £{2:.2f}".format(self.name, self.description,
                                                                   self.price)

class Basket(object):

    def __init__(self):
        # initialize instance of Basket class with an empty dictionary
        self.basket = {}

    def add_product(self, product, quantity=1):
        '''
            This method adds a product to the basket dictionary of an instance of the Basket class
            The default quantity is 1 unless specified
        '''
        # set the attribute product.name to variable to use as the dictionary
        product_name = product.name
        # set the product quantity to the parameter quantity
        # if quantity not an integer, raise exception
        if (isinstance(quantity, int)) and (0 < quantity <= 50):
            product.quantity = quantity
        else:
            raise ValueError("Quantity is not a valid number, please enter a quantity between 1 - 50")
        # set the product_name variable as the key for the product
        self.basket[product_name] = product

        return "{} added to basket".format(product_name)


    def remove_product(self, product):
        '''
            This method removes a product from the dictionary of an instance of the Basket class
            It takes in the product of the parameter which it then removes
        '''
        # Match the product in the dictionary by using the product name
        product_name = product.name
        # del key from dictionary that matches product_name
        # raise NameError if product_name not in dictionary
        if product_name in self.basket.keys():
            del self.basket[product_name]
        else:
            raise NameError("No such product in basket")

        return "{} removed from basket".format(product_name)

    def update_product_quantity(self, product, quantity):
        '''
            This method updates the quantity of a product in the dictionary of an instance of the Basket class
            It takes in the product and quantity as parameters
        '''
        # Get the product name and match it to the product in the dictionary
        product_name = product.name
        # if product name is matched then update product quantity in basket with passed quantity value
        # raise and error if quantity specified as update is a not an integer between 1-50
        if product_name in self.basket.keys():
            previous_quantity = product.quantity
            # raise exception if non-integer between 1-50
            if (isinstance(quantity, int) and (0 < quantity <= 50)):
                product.quantity = quantity
            else:
                raise ValueError("Quantity is not a valid number, please enter a quantity between 1 - 50")


        return "{0} product quantity updated from {1} to {2}".format(product_name, previous_quantity, quantity)



