import math

a = float(input('Podaj bok "a" trójkąta: '))
b = float(input('Podaj bok "b" trójkąta: '))
c = float(input('Podaj bok "c" trójkąta: '))

#połowa obwodu
p = (math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (- a + b + c)))/4


print('Pole trójkąta wynosi {}'.format(p))
