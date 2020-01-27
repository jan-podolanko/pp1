try:
    with open('NoEducation.txt','r') as txt:
        for i in txt:
            print(i)
except:
    print('File cannot be opened.')