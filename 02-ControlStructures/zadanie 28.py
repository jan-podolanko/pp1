a=int(input('Podaj bok "a" trójkąta: '))
b=int(input('Podaj bok "b" trójkąta: '))

print('*' * a)
for i in range(1,b-1):
    print('*' + ' ' * (b-2) + '*')   
print('*' * a)
