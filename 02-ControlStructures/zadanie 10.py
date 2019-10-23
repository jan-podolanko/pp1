x = int(input('liczba: '))

if x > 0 and x % 2 != 0:
    print('{} jest dodatnia oraz nieparzysta'.format(x))
elif x > 0:
    print('{} jest dodatnia, ale nie jest nieparzysta'.format(x))
elif x % 2 != 0:
    print('{} jest nieparzysta, ale nie dodatnia'.format(x))
else:
    print('{} nie jest ani nieparzysta ani dodatnia'.format(x))

