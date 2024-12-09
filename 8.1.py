with open("8.txt", "r") as f:
    data = f.read()

lines = data.split("\n")

C = len(lines[0])
L = len(lines)

dct_nodes = {}

for i in range(L):
    for j in range(C):
        if lines[i][j] != ".":
            if lines[i][j] not in dct_nodes:
                dct_nodes[lines[i][j]] = []
            dct_nodes[lines[i][j]].append((i, j))

lst_antinodes = []

# count the number of antinodes in the map
for node, lst_points in dct_nodes.items():
    if len(lst_points) == 1:
        continue

    Lp = len(lst_points)
    for i in range(Lp - 1):
        for j in range(i + 1, Lp):

            y1, x1 = lst_points[i]
            y2, x2 = lst_points[j]

            x_off = x2 - x1
            y_off = y2 - y1

            x3 = x2 + x_off
            y3 = y2 + y_off
            if 0 <= x3 < C and 0 <= y3 < L:
                lst_antinodes.append((x3, y3))

            x4 = x1 - x_off
            y4 = y1 - y_off
            if 0 <= x4 < C and 0 <= y4 < L:
                lst_antinodes.append((x4, y4))

print(len(list(set(lst_antinodes))))
