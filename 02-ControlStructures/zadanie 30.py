pin = '0805'

input_pin = input('Podaj kod PIN: ')

if input_pin == pin:
    print('Pomyślne logowanie.')
else:
    print('Kod PIN niepoprawny. Pozostały dwie próby.')
    input_pin = input('Podaj kod PIN: ')
    if input_pin == pin:
        print('Pomyślne logowanie.')
    else:
        print('Kod PIN niepoprawny. Pozostała jedna próba.')
        input_pin = input('Podaj kod PIN: ')
        if input_pin == pin:
            print('Pomyślne logowanie.')
        else:
            print('Kod PIN niepoprawny. Karta płatnicza zostaje zablokowana.')
    