cena_b = float(input('Podaj cene brutto: '))
if type(cena_b) != float:
    if type(cena_b) != int:
        raise TypeError('type isnt float or int')
    elif cena_b < 0:
        raise ValueError('int value lower than 0')
elif cena_b < 0:
    raise ValueError('value lower than 0')
print(f'Cena netto wynosi {round(cena_b * 1.23, 2)} zł')
