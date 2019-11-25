def suma_parzyste(x):
    list = []
    for i in x:
        if i % 2 == 0:
            list.append(i)
        else:
            continue
    suma = sum(list)
    return suma

def suma_parzyste2(y):
    z = lambda b: bool(b % 2 == 0)
    return sum(filter(z, y))
    

tablica = [1,2,3,4,5,6,7,8,9,10]
print(suma_parzyste(tablica))
print(suma_parzyste2(tablica))
