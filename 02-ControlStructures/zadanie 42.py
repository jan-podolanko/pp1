a = int(input('Podaj liczbę dzieloną: '))
b = int(input('Podaj liczbę dzielącą: '))

if b == 0 or a == 0:
    print('Dzielenie przez zero!')
else:
    print(f'{a} / {b} = {a/b}')