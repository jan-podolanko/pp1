def czescniewspolna(x,y):
    list = []
    for i in x:
        if i not in y:
            list.append(i)
    return sum(list)

lista1 = [1,2,3,4,6,10,20]
lista2 = [1,2,3,4,5]

print(czescniewspolna(lista1,lista2))