MAIN_DISH = 'main'
DESSERT = 'dessert'

ITALIAN_CUISINE = 'italian'
FRENCH_CUISINE = 'french'


class Product:
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    def __init__(self):
        self.name = 'FettuccineAlfredo'

    def cook(self):
        print(f'Italian main course prepared: {self.name}')


class Tiramisu(Product):
    def __init__(self):
        self.name = 'Tiramisu'

    def cook(self):
        print(f'Italian dessert prepared: {self.name}')


class DuckALOrange(Product):
    def __init__(self):
        self.name = 'Duck À L\'Orange'

    def cook(self):
        print(f'French main course prepared: {self.name}')


class CremeBrulee(Product):
    def __init__(self):
        self.name = 'Crème brûlée'

    def cook(self):
        print(f'French dessert prepared: {self.name}')


class Factory:
    def get_dish(self, type_of_meal) -> Product:
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == MAIN_DISH:
            return FettuccineAlfredo()
        if type_of_meal == DESSERT:
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == MAIN_DISH:
            return DuckALOrange()
        if type_of_meal == DESSERT:
            return CremeBrulee()


class FactoryProducer:
    @staticmethod
    def get_factory(type_of_factory):
        if type_of_factory == ITALIAN_CUISINE:
            return ItalianDishesFactory()
        if type_of_factory == FRENCH_CUISINE:
            return FrenchDishesFactory()