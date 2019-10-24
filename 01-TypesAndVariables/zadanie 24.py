#przelicznik wzrostu na cale i stopy

w = float(input('Podaj wzrost w metrach: '))

s1 = w / 0.3048
s2 = int(w / 0.3048)
f = int((s1 - s2) * 12)

print('Twój wzrost wynosi {} stóp i {} cali.'.format(s2, f))
