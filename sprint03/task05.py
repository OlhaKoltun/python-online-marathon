# Create decorator logger. 
# The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.
# Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function. 

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        args_str = ''
        for item in args:
            args_str += str(item) + ', '

        for item in kwargs.values():
            args_str += str(item) + ', '

        args_str = args_str[:len(args_str) - 2]
        
        print(f'Executing of function {func.__name__} with arguments {args_str}...')
        
        return result

    return wrapper


@logger
def concat(*args, **kwargs):
    result = ''
    for item in args:
        result += str(item)

    for item in kwargs.values():
        result += str(item)

    return result
