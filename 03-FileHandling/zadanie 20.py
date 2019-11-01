with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/numbers.txt', 'r') as l:
    for i in l:
        i = int(i)
        if i % 2 == 0:
            with open ('C:/Users/Monster/Desktop/pp1/03-FileHandling/evennumbers.txt', 'a') as even:
                i = str(i)
                even.write(f'{i}\n')
        else:
            continue