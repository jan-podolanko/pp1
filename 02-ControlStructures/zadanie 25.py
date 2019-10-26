x = [1, 2, 3]

#mało eleganckie rozwiązanie
for i in x:
    print('*******')
#bardziej eleganckie rozwiązanie  
for j in range(3):
    for k in range(7):
        print('*', end='')
    print()
        