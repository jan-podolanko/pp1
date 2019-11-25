x = lambda a: bool(a % 2 == 0)
print(x(2))
tablica = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(x, tablica)))

y = lambda b: bool(b % 5 == 1)
print(list(filter(y, tablica)))
