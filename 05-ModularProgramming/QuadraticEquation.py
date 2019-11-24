import math
def czytajWspolczynniki():
    a = float(input('podaj a:'))
    b = float(input('podaj b:'))
    c = float(input('podaj c:'))
    return [a,b,c]

def obliczDelte(a,b,c):
    delta = float(b ** 2 - 4 * a * c)
    return delta

def obliczPierwiastki(a,b,c):
    deltaRownania = obliczDelte(a,b,c)
    if deltaRownania < 0:
        return []
    elif deltaRownania == 0:
        x0 = round(-b/2*a, 2)
        return [x0]
    else:
        x1 = round((-b-math.sqrt(deltaRownania))/2*a, 2)
        x2 = round((-b+math.sqrt(deltaRownania))/2*a, 2)
        return [x1,x2]
    
def wyswietlPierwiastki(a,b,c):
    deltaRownania = obliczDelte(a,b,c)
    if deltaRownania < 0:
        return []
        print('Brak pierwiastków')
    elif deltaRownania == 0:
        x0 = round(-b/2*a, 2)
        return [x0]
        print(f'Pierwiastkiem rownania jest x0 = {x0}')
    else:
        x1 = round((-b-math.sqrt(deltaRownania))/2*a, 2)
        x2 = round((-b+math.sqrt(deltaRownania))/2*a, 2)
        return [x1,x2]
        print(f'Pierwiastkiami rownania sa x1 = {x1} i x2 = {x2}')