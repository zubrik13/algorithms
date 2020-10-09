from math import log10 as lg
list_a = [7.778, 9.556, 10.936, 12.413, 13.498, 15.498]



def size(list_a):
    size = []
    for x in list_a:
        num = 0.1
        i = 0
        while i != x:
            i = round(num + lg(num), 3)
            num += 0.001
        a = round(num, 3)
        size.append("{:.2e}".format(10 ** a))
    return size
