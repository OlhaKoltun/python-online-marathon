# Create function create with one string argument. 
# This function should return anonymous function that checks if the argument of function is equals to the argument of outer function. 

def create(str):
    return lambda x: True if x == str else False
