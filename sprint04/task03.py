# Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. 
# Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.

class Employee:
    def __init__(self, name, **kwargs):
        self.name = name[:name.index(' ')]
        self.lastname = name[name.index(' ')+1:]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
