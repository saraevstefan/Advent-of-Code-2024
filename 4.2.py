with open('4.txt', 'r') as f:
    data = f.read()

lines = data.split('\n')

L = len(lines)
C = len(lines[0])


def check(i, j):
    if j < C - 2 and i < L - 2:
        w1 = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2]
        w2 = lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j]
        if (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM"):
            return 1

    return 0


S = 0
for i in range(L):
    for j in range(C):
        S += check(i, j)

print(S)
