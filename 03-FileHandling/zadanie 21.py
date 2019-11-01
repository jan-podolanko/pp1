with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/numbersinrows.txt', 'r') as num:
    list = []
    for i in num:
        i.strip('\n')
        if ',' in i:
            j = i.split(',')
            for k in j:
                k = int(k)
                list.append(k)
        else:
            i = int(i)
            list.append(i)

length = len(list)
print(length)
suma = sum(list)
print(suma)