# Define a class Employee. In the class Employee implement the instance attributes as firstname, lastname and salary.
# Create the static method from_string() which parses a string containing these attributes and assigns them to the correct properties. 
# Properties will be separated by a dash.

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(source):
        data = source.split('-')
        return Employee(data[0], data[1], int(data[2]))
