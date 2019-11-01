import re

with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/students.txt', 'r') as land:
    for line in land:
        x = line.split(',')
        print(x[0], end=' ')
        print(x[1], end=' ')
        print(x[4], end=' ')

#alternatively:
#print(x[0],x[1],x[4])