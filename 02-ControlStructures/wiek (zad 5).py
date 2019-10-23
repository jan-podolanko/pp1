wiek = int(input('Podaj wiek: '))

if wiek >= 21 :
    print('Osoba jest dorosła we wszystkich krajach świata i może spożywać alkohol w Ameryce.')
elif wiek == 20:
    print('Osoba jest dorosła we wszystkich krajach poza Arabią Saudyjską i Portoryko, jednak nie może legalnie spożywać alkoholu w Ameryce.')
elif wiek == 19:
    print('Osoba jest dorosła we wszystkich krajach poza Japonią, Arabią Saudyjską i Portoryko, jednak nie może legalnie spożywać alkoholu w Ameryce.')
elif wiek == 18:
    print('Osoba jest dorosła we wszystkich krajach poza niektórymi stanami USA, Koreą Południową, Kanadą, Japonią, Arabią Saudyjską i Portoryko, jednak nie może legalnie spożywać alkoholu w Ameryce.')
elif wiek == 17:
    print('Osoba jest dorosła tylko w Indonezji, Szkocji, Malcie, Iranie, Samoa Amerykańskich i Uzbekistanie.')
elif wiek == 16:
    print('Osoba jest dorosła tylko w Szkocji, Malcie, Iranie, Samoa Amerykańskich i Uzbekistanie.')
elif wiek == 15:
    print('Osoba jest dorosła tylko w Iranie, Samoa Amerykańskich i Uzbekistanie.')
elif wiek == 14:
    print('Osoba jest dorosła tylko w Samoa Amerykańskich i Uzbekistanie.')
else:
    print('Osoba nie jest dorosła.')