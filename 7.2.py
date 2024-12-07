import functools

import numpy as np

with open("7.txt", "r") as f:
    data = f.read()

lines = data.split("\n")

equations = []

for line in lines:
    left, right = line.split(": ")
    equations.append((int(left), [int(x) for x in right.split(" ")]))


@functools.lru_cache(maxsize=None)
def get_operator_arrangements(n, nr_ops=2):
    lst_arrangements = []
    for i in range(nr_ops**n):
        np.base_repr(i, base=nr_ops)
        lst_arrangements.append([int(x) for x in np.base_repr(i, base=nr_ops).zfill(n)])
    return lst_arrangements


def check_equations(equations, nr_ops=2):
    S = 0
    for sol, numbers in equations:
        for ops in get_operator_arrangements(len(numbers) - 1, nr_ops):
            result = numbers[0]
            for i in range(len(ops)):
                if ops[i] == 0:
                    result += numbers[i + 1]
                elif ops[i] == 1:
                    result *= numbers[i + 1]
                elif ops[i] == 2:
                    result = int(str(result) + str(numbers[i + 1]))
            if result == sol:
                S += sol
                break
    return S


print(check_equations(equations, 3))
