class Stos():
    def __init__(self):
        self.stos = []
        self.karty = ['as','król','dama','walet',10,9,8,7,6,5,4,3,2]
    def wstaw(self,nazwa_karty):
        if nazwa_karty in self.karty:
            self.stos.append(nazwa_karty)
    def zdejmij(self):
        return self.stos.pop()
    def jest_pusty(self):
        if self.stos:
            print('Stos nie jest pusty')
        else:
            print('Stos jest pusty')
            
            
z = Stos()
z.wstaw('król')
z.wstaw(6)
z.wstaw(130)
print(z.zdejmij())
z.jest_pusty()
z.zdejmij()
z.jest_pusty()
