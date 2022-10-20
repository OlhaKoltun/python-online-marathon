class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def __str__(self):
        return f'Price: {self.price}, price after discount: {self.price_after_discount()}'

    def price_after_discount(self):
        if self.discount_strategy:
            return self.discount_strategy(self)
        else:
            return self.price


def on_sale_discount(order):
    return order.price / 2


def twenty_percent_discount(order):
    return order.price - order.price * 0.2
