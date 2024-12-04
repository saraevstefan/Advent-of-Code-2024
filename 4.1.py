with open('4.txt', 'r') as f:
    data = f.read()

lines = data.split('\n')

L = len(lines)
C = len(lines[0])


def check(i, j):
    cnt = 0
    # check horizontal
    if j < C - 3:
        word = lines[i][j] + lines[i][j+1] + \
          lines[i][j+2] + lines[i][j+3]
        if word == "XMAS" or word == "SAMX":
            # print(i, j, "horizontal")
            cnt += 1

    # check vertical
    if i < L - 3:
        word = lines[i][j] + lines[i+1][j] + \
          lines[i+2][j] + lines[i+3][j]
        if word == "XMAS" or word == "SAMX":
            # print(i, j, "vertical")
            cnt += 1

    # check diagonal
    if i < L - 3 and j < C - 3:
        word = lines[i][j] + lines[i+1][j+1] + \
            lines[i+2][j+2] + lines[i+3][j+3]
        if word == "XMAS" or word == "SAMX":
            # print(i, j, "diagonal right")
            cnt += 1

    if i < L - 3 and j > 2:
        word = lines[i][j] + lines[i+1][j-1] + \
            lines[i+2][j-2] + lines[i+3][j-3]
        if word == "XMAS" or word == "SAMX":
            # print(i, j, "diagonal left")
            cnt += 1

    return cnt


S = 0
for i in range(L):
    for j in range(C):
        S += check(i, j)

print(S)
