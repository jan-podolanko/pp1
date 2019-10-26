n = int(input('Podaj liczbę: '))
list=[]
while n > 0:
    x = n%2
    list.insert(0,x)
    n=n//2
print(list)
