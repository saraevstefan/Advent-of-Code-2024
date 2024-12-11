import numpy as np

with open("10.txt", "r") as f:
    data = f.read().strip()


Map = np.array([[int(x) for x in line] for line in data.split("\n")])


def get_number_trails(i, j, Map):
    if Map[i][j] == 9:
        return 1

    result = 0

    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if 0 <= i + di < len(Map) and 0 <= j + dj < len(Map[0]):
            if Map[i + di][j + dj] == Map[i][j] + 1:
                result += get_number_trails(i + di, j + dj, Map)

    return result


S = 0

for i in range(len(Map)):
    for j in range(len(Map[i])):
        if Map[i][j] == 0:
            S += get_number_trails(i, j, Map)

print(S)
