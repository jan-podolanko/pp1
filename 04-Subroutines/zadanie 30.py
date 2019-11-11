import random
def random_n_from_1_to_50():
    return random.randrange(1,51)
lista = []
for i in range(1,1001):
    x = random_n_from_1_to_50()
    lista.append(x)
parzyste = []
nieparzyste = []
for i in lista:
    if i % 2 == 0:
        parzyste.append(i)
    elif i % 2 != 0:
        nieparzyste.append(i)


print(f'Liczby parzyste: {(len(parzyste)/1000)*100}%') 
print(f'Liczby nieparzyste: {(len(nieparzyste)/1000)*100}%') 