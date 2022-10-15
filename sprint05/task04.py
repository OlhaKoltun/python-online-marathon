# Write  the function solve_quadric_equation(a, b, c) the three input parameters of which are numbers. 

import cmath

def solve_quadric_equation(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a == 0.0:
            raise ZeroDivisionError()

        disc = b ** 2 - 4 * a * c

        x1 = (-b - cmath.sqrt(disc)) / 2 * a
        x2 = (-b + cmath.sqrt(disc)) / 2 * a

        return f'The solution are x1={x1} and x2={x2}'
    except ZeroDivisionError:
        return 'Zero Division Error'
    except ValueError:
        return 'Could not convert string to float'
