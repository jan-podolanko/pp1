n = int(input('Podaj liczbę: '))
list=[]
list2=[]
while n > 0:
    x = n%2
    list2.append(x)
    list.insert(0,x)
    n=n//2

print(list)
print(list2)