
"""
A customer in real estate store makes an order
The store provides multiple type of discounts.
If the discount is applicable, then provide the best discount to customer.
Assume three discount. Bulk purchase discount, coupen discount, festival discount
The best discount is the one, that minimizes the sales order net price
"""

from itertools import *

class Product:

    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount

class Cart :
    def __init__(self,products):
        self.products = products

    def getNetAmount(self):
        total = 0
        for item in self.products:
            total = total + item.price - item.discount(item)
        return total


def bulkDiscount(order):
    if order is None:
        return 0

    if order.price > 100:
        return order.price * 0.10
    else:
        return 0

cart = Cart([Product("banana",12, bulkDiscount), Product("Diaper", 200,bulkDiscount)])
print(cart.getNetAmount())
