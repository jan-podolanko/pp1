import math

try:
    number = float(input('Enter any number: '))
    if number == 0:
        raise Exception
    print (f'sqrt({number}) = {math.sqrt(number)}' )
except:
    print('Please enter a valid number greater than 0')