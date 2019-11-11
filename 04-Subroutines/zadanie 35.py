
def suma_cyfr(x):
    list1 = []
    x = str(x)
    for i in range(len(x)):
        list1.append(x[i])
    list1 = [int(j) for j in list1]
    return sum(list1)

liczba = 1035
print(liczba)
print(suma_cyfr(liczba))