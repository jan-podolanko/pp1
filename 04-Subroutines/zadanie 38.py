import re

ciag = 'sFadGHJasadGadcXzcvBSgdXashIoOOpPljQ'

def wielkie_litery(x):
    tab = re.findall('[A-Z]',x)
    for i in range(len(tab)):
        print(tab[i], end='')

wielkie_litery(ciag)