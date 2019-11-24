def wspak(string1):
    return string1[len(string1)::-1]

def rozstrzelony(string1):
    for i in range(len(string1)):
        print(string1[i],end=' ')
import re
def wielkie(string1):
    lista = re.split('\s', string1)
    lista2 = []
    for i in range(len(lista)):
        x = lista[i].capitalize()
        lista2.append(x)   
    return ' '.join(lista2)