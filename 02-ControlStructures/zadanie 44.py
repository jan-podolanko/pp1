limit = int(input('Podaj limit prędkości (w km/h): '))
pred = int(input('Podaj prędkość (w km/h): '))

if pred < limit:
    print('Brak mandatu')
elif pred > limit and pred - limit <= 10:
    roznica = pred - limit
    mandat = roznica * 5
    print(f'Mandat wynosi: {mandat} zł')
elif pred > limit and pred - limit > 10:
    roznica = pred - limit
    mandat = roznica * 5
    mandat2 = (roznica-10) * 10
    mandat_final = mandat + mandat2
    print(f'Mandat wynosi: {mandat_final} zł')