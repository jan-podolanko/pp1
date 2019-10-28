x = 0
with open('C:/Users/s-115-09/Desktop/pp1/03-FileHandling/numbers.txt') as n:
    for line in n:  
        line = int(line)
        x += line
print(x)