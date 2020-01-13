wiek = int(input('Podaj wiek: '))
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek > 120:
    raise ValueError('wiek wiekszy od 120')
print(f'Masz {wiek} lat')