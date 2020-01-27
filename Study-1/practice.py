class Ulamek():
    def __init__(self,x,y):
        self.licznik = x
        self.mianownik = y
        if y == 0:
            raise ValueError('Mianownik nie może być równy zeru')
    def zmien_ulamek(self,nowy_l,nowy_m):
        self.licznik = nowy_l
        self.mianownik = nowy_m
        if nowy_m == 0:
            raise ValueError('Mianownik nie może być równy zeru')
    def uprosc(self):
        if self.mianownik > self.licznik:
            for i in range(self.mianownik,1,-1):
                if self.licznik % i == 0 and self.mianownik % i == 0:
                    self.licznik /= i
                    self.mianownik /= i
                    self.licznik = int(self.licznik)
                    self.mianownik = int(self.mianownik)
        else:
            for i in range(self.licznik,1,-1):
                if self.licznik % i == 0 and self.mianownik % i == 0:
                    self.licznik /= i
                    self.mianownik /= i
                    self.licznik = int(self.licznik)
                    self.mianownik = int(self.mianownik)

    def view(self):
        print(f'{self.licznik}/{self.mianownik}')

class Kostka():
    def rzuc_kostka(self):
        import random
        self.rzut = random.randrange(1,6)
        return self.rzut
    
x = Kostka()
z = 0
for i in range(3):
    rzut = x.rzuc_kostka()
    print(rzut)
    z += rzut
print(z)
            