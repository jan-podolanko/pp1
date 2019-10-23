import math

'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''

# ustal promień koła i PI
r = float(input("Podaj promień koła: "))
pi = math.pi

# oblicz pole i obwód
# pole
p = pi * r ** 2
# obwód
l = 2 * pi * r

# wyświetl rezultaty

# Pole koła o promieniu ... wynosi ...
print('Pole koła o promieniu {} wynosi {}'.format(r, p))
# Obwód koła o promieniu ... wynosi ...
print('Obwód koła o promieniu {} wynosi {}'.format(r, l))