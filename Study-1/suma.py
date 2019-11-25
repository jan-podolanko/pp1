import re
def suma(filename):
    with open(filename,'r') as x:
        y = re.findall['\d{2,3}',x]
        list2 = []
        for j in y:
            j = int(j)
            list2.append(j)
        list = []
        for i in list2:
            if i <= 500:
                list.append(i)
            else:
                continue
        return sum(list)
suma('liczby.txt')
