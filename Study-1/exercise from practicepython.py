import random

x = random.randrange(1,101)
y = input('is the guess too high, too low or correct?')

if y != 'correct':
    if y == 'too high':
        x = random.randrange(1,x)
        continue
    elif y == 'too low':
        x = random.randrange(x+1,101)
        continue
    else:
        print('answer with "too high", "too low" or "correct"')
    
