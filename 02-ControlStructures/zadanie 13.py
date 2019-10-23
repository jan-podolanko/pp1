x = int(input('podaj wartosc x: '))
y = int(input('podaj wartosc y: '))

if x==0 and y==0:
    print('punkt ({}, {}) znajduje się na początku ukladu wspolrzednych'.format(x, y))
elif x>0 and y>0:
    print('punkt ({}, {}) znajduje się w pierwszej cwiartce ukladu wspolrzednych'.format(x, y))
elif x>0 and y<0:
    print('punkt ({}, {}) znajduje się w drugiej cwiartce ukladu wspolrzednych'.format(x, y))
elif x<0 and y<0:
    print('punkt ({}, {}) znajduje się w trzeciej cwiartce ukladu wspolrzednych'.format(x, y))
elif x<0 and y>0:
    print('punkt ({}, {}) znajduje się w czwartej cwiartce ukladu wspolrzednych'.format(x, y))
