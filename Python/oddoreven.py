# Inputs integer and outputs if it is odd or if it is even
def even_or_odd(number):
    if type(number) == int:
        if int(number) % 2 == 0:
            return ("Even")
        else:
            return ("Odd")
