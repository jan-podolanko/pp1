def pole_prostokata(a,b):
    if type(a) != float:
        if type(a) != int:
            raise TypeError('a isnt an int or a float')
    if type(b) != float:
        if type(b) != int:
            raise TypeError('b isnt an int or a float')
    if a <= 0:
        raise ValueError('a smaller than 0')
    if b <= 0:
        raise ValueError('b smaller than 0')
    c = a * b
    return c

print(pole_prostokata(3,4))
print(pole_prostokata(3,4))
print(pole_prostokata(3,'4'))
print(pole_prostokata(3,-2))

    