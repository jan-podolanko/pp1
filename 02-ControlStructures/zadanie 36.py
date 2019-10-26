x = 0
while x > -1:
    x += 1
    if x % 7 == 0:
        if x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1:
            print(f'Znaleziono liczbę podzielną przez 7 oraz dającą resztę 1 z dzielenia przez 2, 3, 4, 5 i 6, jest to {x}')
            break