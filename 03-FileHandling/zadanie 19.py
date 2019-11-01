with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/universities.txt', 'r') as l:
    lista = [line.strip() for line in l]
    lista.sort()
    print(lista)
with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/universities.txt', 'a') as l:
    for i in lista:
        l.write(i)