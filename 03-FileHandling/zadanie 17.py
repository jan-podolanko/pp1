import re
tekst = 'To be, or not to be, that is the question'
ilosc = re.findall('a|e|i|o|u',tekst)
print(len(ilosc))