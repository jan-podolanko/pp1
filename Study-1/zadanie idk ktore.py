tablica = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('tablica.csv','w') as x:
    x.write('imie,nazwisko,email\n')
    for i in tablica:
        for j in i:
            x.write(j)
            if j == i[-1]:
                break
            else:
                x.write(',')
        x.write('\n')