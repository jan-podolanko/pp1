x = lambda a: bool(a % 2 == 0)
print(x(2))
tablica = [1,2,3,4,5,6,7,8]
print(list(filter(x, tablica)))