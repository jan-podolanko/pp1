import re
with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/numbersinrows.txt', 'r') as num2:
    l = 0
    for i in num2:
        x = re.findall(r'\d{2}', i)
        if x > 1:
            b = sum(x)
            l += b
        else:
            l += x
    print(l)