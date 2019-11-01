import re
list = []
with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/land.txt', 'r') as land:
    for line in land:
        list += re.findall('\d', line)
print(list)
list = [ int(i) for i in list ]
print(sum(list))