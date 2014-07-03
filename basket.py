# coding=utf-8
# program that adds products to a shopping basket and displays total

class Product(object):

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    # method to display details of product
    def display_product_details(self):
        return "Product name: {0}, Desc: {1}, Price: £{2:.2f}".format(self.name, self.description, self.price)


class Basket(object):

    def __init__(self):
        self.basket_items = []
        self.basket = {}

    # method to add product to basket items list
    def add_product(self, product):
        self.basket_items.append(product.name)
        self.basket_items.append(product.description)
        self.basket_items.append(product.price)

        return self.basket_items

    def add_prods(self, prod, quantity=1):
        '''
            This function adds a product to the basket which is a dictionary.
            The default quantity is set to 1
        '''
        # set the first item in basket to have a key = 1
        basket_key = 1
        # increment basket_keys if already in self.basket
        while basket_key in self.basket.keys():
            basket_key += 1
        # set value of key 1 in basket to a list of the product name, description, and price
        self.basket[basket_key] = [prod.name, prod.description, prod.price, quantity]

        return self.basket

    def remove_item(self, product):
        '''
            This function removes an item from the basket
        '''
        # Iterate through items in basket and delete item that matches product.name


        for key, product_name in self.basket.items():
            if product_name[0] == product.name:
                del self.basket[key]
            else:
                continue

        # raise exception if product not found in basket
        if product.name not in self.basket.items():
            #print "{} product not in basket".format(product.name)
            raise NameError("{} product not in basket".format(product.name))

        return self.basket


    def update_item(self, product, quantity):
        '''
            This function updates the quantity field of a product in the basket
            step 1 get the product item (key) - if self.basket[product.name] == product.name
            step 2 update the quantity with new quantity - product.quantity = quantity
        '''
        pass


def main():

    product1 = Product("Jam", "Marmalade", 2.45)
    product2 = Product("Lurpak", "Butter", 5.00)
    product3 = Product("Ariel", "Soap", 3.63)
    basket1 = Basket()
    basket1.add_prods(product1)
    basket1.add_prods(product2)
    #basket1.add_prods(product3, 5)

    print "Before ", basket1.basket

    basket1.remove_item(product3)

    print "After ", basket1.basket


if __name__ == "__main__":
    main()


