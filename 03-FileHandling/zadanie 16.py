import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
cyfry = [int(i) for i in cyfry]
y=len(cyfry)
x=sum(cyfry)
print(x/y)