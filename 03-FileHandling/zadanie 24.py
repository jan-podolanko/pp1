list = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]

with open('C:/Users/Monster/Desktop/pp1/03-FileHandling/tab.csv', 'w') as tab:
    tab.write('Imię,Nazwisko,e-mail\n')
    for i in list:
        tab.write(f'{i[0]},{i[1]},{i[2]}\n')