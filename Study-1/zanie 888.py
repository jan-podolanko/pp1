from zadanie8 import Sala
from zadanie8 import Sale
x = Sale()
x.dodaj_sale(Sala('Nowa Aula',80))
x.dodaj_sale(Sala('Hala Sportowa',500))
x.dodaj_sale(Sala('Lab. komputerowe 115',35))
x.dodaj_sale(Sala('Sala 053',45))
x.dodaj_sale(Sala('Sala G',70))
print(x.liczba_sal())
print(x.razem_miejsc())
print(x.liczba_miejsc('Nowa Aula'))
print(x.liczba_miejsc('Sala 000000'))
print(x.liczba_sal_przedzial(35,70))