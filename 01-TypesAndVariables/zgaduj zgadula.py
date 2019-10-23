import random

a = random.randrange(1,6)

b = int(input('Wpisz swoją odpowiedź: '))

print('Komputer wyrzucił {} oczek. Ty zgadywałeś {}.'.format(a, b))

if a == b:
    print('Zgadłeś!')
else:
    print('Nie zgadłeś!')