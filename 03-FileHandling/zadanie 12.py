with open('C:/Users/s-115-09/Desktop/pp1/03-FileHandling/shoppinglist.txt', 'a') as sl:
    i = 0
    while i > -1:
        i += 1
        p = input('Podaj następny produkt: ')
        sl.write(f'{i}.{p}\n')
        if p == '':
            break
