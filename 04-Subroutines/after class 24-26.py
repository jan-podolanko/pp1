#zadanie 24
def miesiąc(n24):
    miesiace = ['styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień']
    print(miesiace[n24-1])

miesiąc(7)
miesiąc(9)

#zadanie 25

def jestimie(imie = input('Podaj imie: ')):
    imiona =  ['Janek', 'Ania', 'Wojtek', 'Zosia']
    if imie in imiona:
        print('imie zawarte w tabeli')
    else:
        print('imie nie jest zawarte w tabeli')

jestimie()

#zadanie 26

def podatek(dochod=float(input('Podaj dochod: '))):
    x26 = dochod * 0.17
    
    print(f'Podatek nalezny: {round(x26, 2)}')

podatek()
