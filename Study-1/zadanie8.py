class Sala():
    def __init__(self,nazwa,liczba):
        self.nazwa = nazwa
        self.liczba_miejsc = liczba
class Sale(Sala):
    def __init__(self):
        self.sale = []
    def dodaj_sale(self,Sala):
        self.sale.append(Sala)
    def liczba_sal(self):
        return len(self.sale)
    def razem_miejsc(self):
        l_miejsc = 0
        for i in self.sale:
            l_miejsc += i.liczba_miejsc
        return l_miejsc
    def liczba_miejsc(self,nazwa_sali):
        for j in self.sale:
            if nazwa_sali == j.nazwa:
                return j.liczba_miejsc
        else:
            return 0
    def liczba_sal_przedzial(self,od,do):
        l_sal = 0
        for k in self.sale:
            if k.liczba_miejsc >= od and k.liczba_miejsc <= do:
                l_sal += 1
        return l_sal