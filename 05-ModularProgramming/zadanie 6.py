import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(0,len(row)):
            print(f'{row[i]:<15}', end=' ')
        print()
import statistics
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    list = []
    y = 0
    for row in reader:
        y += 1
        x = row[2]
        if x == 'age':
            print()
        else:
            x = int(x)
            list.append(x)
        
    print(f'srednia = {statistics.mean(list)}')
