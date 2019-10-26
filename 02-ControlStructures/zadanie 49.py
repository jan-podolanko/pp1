nrDniaTygodnia=2
print("| PN | WT | SR | CZ | PT | SB | ND |")
print('|',end='')
i=0    
while nrDniaTygodnia>0:
    print('    |',end='')
    nrDniaTygodnia-=1
    i+=1
for j in range(1,31):
    if j < 10:
        print(f' {j}  |',end='')
        i+=1
        if i%7==0:
            print()
            print('|',end='')
            i=0
    if j >= 10:
        print(f' {j} |',end='')
        i+=1
        if i%7==0:
            print()
            print('|',end='')
            i=0

