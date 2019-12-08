import statistics
class Statystyka():
    def __init__(self):
        self.zbior_liczb = []
    def dodaj_liczbe(self):
        self.liczba = int(input('Podaj liczbe dodawana do zbioru: '))
        self.zbior_liczb.append(self.liczba)
    def wyswietl(self):
        for i in self.zbior_liczb:
            print(i, end=' ')
    def wyznacz_najwyzsza_l(self):
        self.najw_l = max(self.zbior_liczb)
        print(f'Najwyzsza liczba zbioru jest {self.najw_l}')
    def wyznacz_najnizsza_l(self):
        self.najn_l = min(self.zbior_liczb)
        print(f'Najnizsza liczba zbioru jest {self.najn_l}')
    def oblicz_srednia(self):
        self.srednia = statistics.mean(self.zbior_liczb)
        print(f'Srednia zbioru wynosi {self.srednia}')
    def oblicz_mediane(self):
        self.mediana = statistics.median(self.zbior_liczb)
    def pokaz_dane(self):
        print(f'Wielkosci statystyczne dla zbioru {self.zbior_liczb}: srednia = {self.srednia}, mediana = {self.mediana}, najnizsza liczba = {self.najn_l}, najwyzsza liczba = {self.najw_l}')

x = Statystyka()
x.dodaj_liczbe()
x.dodaj_liczbe()
x.dodaj_liczbe()
x.dodaj_liczbe()
x.dodaj_liczbe()
x.wyswietl()
x.wyznacz_najnizsza_l()
x.wyznacz_najwyzsza_l()
x.oblicz_mediane()
x.oblicz_srednia()
x.pokaz_dane()