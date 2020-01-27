import random
class arrays():
    seperator = ','
    @staticmethod
    def change_seperator(sep):
        arrays.seperator = sep
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_table(array):
        n = 1
        for i in array:  
            if n < len(array):
                print(i,end=f'{arrays.seperator} ')
                n += 1
            else:
                print(i)
    @staticmethod
    def create_list_a(n_of_elements,value_of_e):
        list_a = []
        for i in range(n_of_elements):
            list_a.append(value_of_e)
        return list_a
    @staticmethod
    def create_list_b(n_of_elements, val_from, val_to):
        list_b = []
        for j in range(n_of_elements):
            list_b.append(random.randrange(val_from,val_to))
        return list_b
    @staticmethod
    def n_of_element_in_list(list_c, val_from2, val_to2):
        n_of_elements = 0
        for k in list_c:
            if k >= val_from2 and k <= val_to2:
                n_of_elements += 1
            else:
                continue
        return n_of_elements