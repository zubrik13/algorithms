from math import log2 as log
from n_lgn import size, list_a
from factorial import fctorial, instr

ins_per_sec = 10 ** 6

# time
second = 1
minute = 60
hour = 60 * minute
day = 24 * hour
month = 30 * day
year = 365 * day
century = 100 * year

time = [second, minute, hour, day, month, year, century]

instructions = []

for t in time:
    i = "{:.2e}".format(t * ins_per_sec)
    instructions.append(i)

# size of n for **lg n**
lg_n = []
for ins in instructions:
    n = f"10^({ins})"
    lg_n.append(n)
print(f"lg_n {lg_n}")

# size of n for **sqrt n**
sqrt_n = []
for ins in instructions:
    n = "{:.2e}".format(float(ins) ** 2)
    sqrt_n.append(n)
print(f"sqrt_n {sqrt_n}")

# size of n for **n**
n = instructions
print(f"n {n}")
#
# size of n for **n lg n**
n_lg_n = size(list_a)
print(f"n_lg_n {n_lg_n}")

# size of n for **n^2**
n_2 = []
for ins in instructions:
    n = "{:.2e}".format(float(ins) ** 0.5)
    n_2.append(n)
print(f"n_2 {n_2}")

# size of n for **n^3**
n_3 = []
for ins in instructions:
    n = "{:.2e}".format(float(ins) ** (1/3))
    n_3.append(n)
print(f"n_3 {n_3}")

# size of n for **2^n**
two_n = []
for ins in instructions:
    n = "{:.2e}".format(log(float(ins)))
    two_n.append(n)
print(f"two_n {two_n}")

# size of n for **n!**
factorial_n = fctorial(instr)
print(f"factorial_n {factorial_n}")



