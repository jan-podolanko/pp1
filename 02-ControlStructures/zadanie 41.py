i = 1
x = []
count = 0

while i > 0:
    y = int(input('Podaj liczbę: '))
    if y == 0:
        break
    else:
        x.append(y)
        count += 1
        
print(f'REZULTAT: Liczb={count}, Suma={sum(x)}, Średnia={(sum(x))/count}')
        

        