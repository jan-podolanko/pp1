#zadanie 5
def NAMEprint():
    print('Jan Podolanko')

NAMEprint()
#zadanie 6
def uek():
    print(' Uniwersytet Ekonomiczny w Krakowie \n ul. Rakowicka 27 \n 31-510 Kraków')
    
uek()
uek()

#zadanie 7

def liczby():
    for i in range(0, 9, 3):
        for j in range(1,4):
            print(f' {i+j}',end='')
        print()           
liczby()

#zadanie 12

def iloczyn(x,y):
    print(x * y)
    
iloczyn(3,5)

#zadanie 13
x13 = [4,3,7,1,3]
def suma(x13):
    print(f'Tablica: {x13}')
    print(f'Suma wartości: {sum(x13)}')
    
suma(x13)

#zadanie 14
y14 = [15, 38, 7, 23, 14]
def wystepuje(x14,y14):
    if x14 in y14:
        print('Podana liczba wystepuje w tablicy')
    else:
        print('Podana liczba nie wystepuje w tablicy')
        
wystepuje(23,y14)

#zadanie 15

def multiplication(x15,y15):
    return x15*y15
print( multiplication(15,12) )

#zadanie 16 

def czytajLiczbe(x16):
    return x16
czytajLiczbe(input('podaj liczbe: '))

print(czytajLiczbe(int(input('podaj liczbe: '))) + czytajLiczbe(int(input('podaj liczbe: '))))
#zadanie 17

import random

def rzucKostka():
    x17 = random.randrange(1,7)
    y17 = random.randrange(1,7)
    z17 = random.randrange(1,7)
    print(f'Wyrzucone kosci: {x17}, {y17}, {z17}')
    print(f'Suma wyrzuconych oczek: {x17 + y17 + z17}')
    
rzucKostka()

#zadanie 19

def suma19(n19):
    x19 = 0
    for i19 in range(1,n19+1):
        x19 += i19
    print(x19)
suma19(500)

#zadanie 20

def potega20(x20,y20):
    if y20 == 0:
        return 1
    else:
        return x20 * x20 ** (y20-1)
    
print(f'potega 5 do 3 wynosi {potega20(5,3)}')
    
    
#zadanie 21

multiplication21 = lambda x21,y21: x21*y21
print( multiplication21(3,4) )

#zadanie 22

funkcja22 = lambda x22: print(bool(x22 % 2 == 0))

funkcja22(6)

#zadanie 23

funkcja23 = lambda x23,y23: print(bool(x23 > y23))

funkcja23_2 = lambda x23_2,y23_2: print(True) if x23_2 > y23_2 else print(False)

funkcja23(7,6)

funkcja23_2(7,6)
