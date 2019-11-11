X = [[1, 2, 0], 
     [0, 0, 3], 
     [5, 1, 1]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
def transpozycja(X):
    # iterate through rows
    for i in range(len(X)):
    # iterate through columns
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    for r in result:
        print(r)
print('macierz: ')
for k in range(len(X)):
    print(X[k])
print('transponowana macierz: ')
transpozycja(X)