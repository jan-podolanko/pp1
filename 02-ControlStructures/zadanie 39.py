fibonacci = 50
n1 = 0
n2 = 1
liczba = 0
while liczba < fibonacci:
    print(n1,end=' , ')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    liczba += 1    
print()

    