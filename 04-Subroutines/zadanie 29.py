#zadanie 29
import statistics
lista =  [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
#gorsza wersja, ale szkoda usunac
def med_i_dom():
    lista =  [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
    lista.sort()
    dlug = len(lista)
    if dlug % 2 != 0:
        l_mediana = int(dlug/2)
        mediana = (lista[l_mediana])
        print(f'lista: {lista}')
        print(f'mediana: {mediana}')
    elif dlug % 2 == 0:
        l_mediana = int(dlug/2)
        mediana = (lista[l_mediana-1] + lista[l_mediana])/2
        print(f'lista: {lista}')
        print(f'mediana: {mediana}')
    print(f'dominanta: {statistics.mode(lista)}')

#lepsza wersja
def med_i_dom2():
    lista =  [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
    lista.sort()
    print(f'mediana: {statistics.median(lista)}')
    print(f'dominanta: {statistics.mode(lista)}')
med_i_dom()
med_i_dom2()