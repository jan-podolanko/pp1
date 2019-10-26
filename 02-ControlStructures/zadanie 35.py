import math

a = int(input('Podaj "a": '))
b = int(input('Podaj "b": '))
c = int(input('Podaj "c": '))

print(f'Równanie: {a}x^2 + {b}x + {c}')

delta = b**2 - 4*a*c
print(f'Delta: {delta}')

if delta < 0:
    print('Brak pierwiastków równania')
elif delta == 0:
    x0 = (-b)/(2*a)
    print(f'Jeden pierwiastek w równaniu, {x0}')
else:
    x1 = ((-b - (math.sqrt(delta)))/(2*a))
    x2 = ((-b + (math.sqrt(delta)))/(2*a))
    print(f'Dwa pierwiastki w równaniu, {x1} oraz {x2}')