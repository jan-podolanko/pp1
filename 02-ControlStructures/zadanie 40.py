import random
list = []
for i in range(1,101):
    j = random.randrange(1,7)
    list.append(j)
    num1=list.count(1)
    num2=list.count(2)
    num3=list.count(3)
    num4=list.count(4)
    num5=list.count(5)
    num6=list.count(6)
print(f'Jedynek wypadło: {num1}')
print(f'Dwójek wypadło: {num2}')
print(f'Trójek wypadło: {num3}')
print(f'Czwórek wypadło: {num4}')
print(f'Piątek wypadło: {num5}')
print(f'Szóstek wypadło: {num6}')

