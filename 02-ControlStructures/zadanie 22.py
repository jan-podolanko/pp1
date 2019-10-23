suma = 0
x = [15, 8, 31, 47, 2, 19]
n = 0

for i in x:
    if i % 2 != 0:
        suma += i
        n += 1
print(f'srednia wynosi: {suma/n}')
