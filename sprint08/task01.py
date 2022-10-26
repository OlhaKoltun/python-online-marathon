import unittest

DISCOUNT_BY_COUNT = {(0, 4): 0.0,
                     (5, 6): 0.05,
                     (7, 9): 0.10,
                     (10, 19): 0.20,
                     (20, 20): 0.30,
                     (21, ): 0.50
                     }


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f'Product: {self.name}, price: {self.price} - count {self.count}'

    def get_discount(self):
        for each in DISCOUNT_BY_COUNT:
            if len(each) == 2 and each[0] <= self.count <= each[1]:
                return DISCOUNT_BY_COUNT[each]
            elif len(each) == 1 and self.count >= each[0]:
                return DISCOUNT_BY_COUNT[each]

    def get_total_with_discount(self):
        return self.price * self.count \
               - self.price * self.count * self.get_discount()


class Cart:

    def __init__(self, products):
        if products:
            self.products = list(products)
        else:
            self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.get_total_with_discount()

        return total_price


class CartTest(unittest.TestCase):
    def test_get_total_price(self):
        expected = 515
        products = (Product('p1', 10, 4),
                    Product('p2', 100, 5))
        cart = Cart(products)
        actual = cart.get_total_price()
        self.assertEqual(actual, expected)
