#zadanie 27
import re
reduta = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
samogloski = ['a', 'e', 'y', 'i', 'o', 'ą', 'ę', 'u', 'ó']
ilosc = re.findall('[aeyioąęuó]', reduta)
for i in range(0,9):
    y = ilosc.count(samogloski[i])
    x = len(reduta)
    z = y/x
    print(f'Samogłoska {samogloski[i]} występuje w tekście {y} razy, z częstotliwością {z*100}%')