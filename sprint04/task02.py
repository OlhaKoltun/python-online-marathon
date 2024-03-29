# Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza flavours.

class Pizza:
    order_counter = 0

    def __init__(self, ingredients):
        Pizza.order_counter += 1
        self.order_number = Pizza.order_counter
        self.ingredients = ingredients

    def hawaiian():
        return Pizza(['ham', 'pineapple'])

    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])

    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])
