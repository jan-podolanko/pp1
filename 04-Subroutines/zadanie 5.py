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