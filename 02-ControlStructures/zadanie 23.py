oceny = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący']

o = int(input('Podaj ocenę: '))

print(f'Ocena słownie: {oceny[o-1]}')