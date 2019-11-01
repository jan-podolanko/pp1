list = [32, 16, 5, 8, 24, 7]
with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/zadanie 13.txt', 'w') as l:
    i = -1
    while i > -2:
        i += 1
        l.write(f'{list[i]}\n')
        if i == 5:
            break