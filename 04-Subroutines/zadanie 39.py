def czy_jest_w_przedziale(n,x,y):
    if n >= x and n <= y or n <= x and n >= y:
        print('n miesci sie w przedziale zamknietym')
    else:
        print('n nie miesci sie w przedziale')

czy_jest_w_przedziale(3,3,5)