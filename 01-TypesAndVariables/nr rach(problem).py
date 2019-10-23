import locale
locale.setlocale(locale.LC_ALL, '')

nr_rach = input('Podaj numer rachunku: ')

print(nr_rach[0:2] + ' ' + nr_rach[2:6] + ' ' + nr_rach[6:10] + ' ' + nr_rach[10:14] + ' ' + nr_rach[14:18] + ' ' + nr_rach[18:22] + ' ' + nr_rach[22:27])