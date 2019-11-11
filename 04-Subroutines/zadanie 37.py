tab1 = [1, 2, 3, 3, 5, 6, 6]

def suma_liczb_niepowt(tab):
    list37 = []
    for i in tab:
        if tab.count(i) == 1:
            list37.append(i)
        elif tab.count(i) > 1:
            continue
    return list37

print(suma_liczb_niepowt(tab1))