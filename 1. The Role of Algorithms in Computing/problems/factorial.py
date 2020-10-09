from math import factorial

instr = [1.00e+06, 6.00e+07, 3.60e+09, 8.64e+10, 2.59e+12, 3.15e+13, 3.15e+15]


def fctorial(instr):
    number = []

    for i in instr:
        n = 0
        f = 1
        while f <= int(i):
            f = factorial(n)
            n += 1
        number.append(n-2)
    return number

