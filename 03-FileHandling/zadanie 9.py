i = 0
with open ('C:/Users/s-115-09/Desktop/pp1/03-FileHandling/NoEducation.txt', 'r') as f:
    for line in f:
        i += 1
        print(f'{i}. {line}', end='')