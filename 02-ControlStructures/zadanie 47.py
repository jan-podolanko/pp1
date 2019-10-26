zł = int(input('Podaj ilość pieniędzy: '))

pięć = zł // 5
dwa = (zł % 5)//2
jeden = (dwa % 2)

if zł == 1:
    print(f'Kwota {zł} w monetach: ')
    print(f'5 zł - 0 szt')
    print(f'2 zł - 0 szt')
    print(f'1 zł - 1 szt')
elif zł == 2:
    print(f'Kwota {zł} w monetach: ')
    print(f'5 zł - 0 szt')
    print(f'2 zł - 1 szt')
    print(f'1 zł - 0 szt')
else:
    print(f'Kwota {zł} w monetach: ')
    print(f'5 zł - {pięć} szt')
    print(f'2 zł - {dwa} szt')
    print(f'1 zł - {jeden} szt')


print('Podaj kwote w zl: ')
x47=int(input())
print(f'5zl: {x47//5}')
print(f'2zl: {(x47%5)//2}')
print(f'1zl: {((x47%5)%2)//1}')