wiek = int(input('Podaj wiek psa w ludzkich latach: '))

if wiek <= 2:
    print(f'Wiek psa w psich latach to {wiek * 10.5} lata.')
elif wiek > 2:
    print(f'Wiek psa w psich latach to {21 + (wiek - 2) * 4} lata.')