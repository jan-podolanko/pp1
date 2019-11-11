jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
wartosci = [61,47,37,32,26,18,14,14,9,7]
ilosc = len(jezyki)
for i in range(0,ilosc):

    print(f'{jezyki[i]:>12}: ' + '#' * wartosci[i])