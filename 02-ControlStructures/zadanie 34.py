pesel = input('Podaj PESEL: ')

rok = int(pesel[0:2])
wiek = 118 - rok

if int(pesel[2:4]) > 12:
    wiek_2 = 18 - rok
    print(f'PESEL: {pesel}')
    print(f'Wiek: {wiek_2}')
    if int(pesel[9]) % 2 == 0:
        print('Płeć: kobieta')
    else:
        print('Płeć: mężczyzna')
else:
    print(f'PESEL: {pesel}')
    print(f'Wiek: {wiek}')
    if int(pesel[9]) % 2 == 0:
        print('Płeć: kobieta')
    else:
        print('Płeć: mężczyzna')