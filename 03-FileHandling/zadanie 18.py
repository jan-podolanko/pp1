with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/numbers.txt', 'r') as l:
    lista = [line.strip() for line in l]
    lista.sort()
print(lista)