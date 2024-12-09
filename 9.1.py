with open("9.txt", "r") as f:
    data = f.read().strip()

data = [int(x) for x in data]

disk = [0] * sum(data)

index = 0
for i, x in enumerate(data):
    if i % 2 == 0:
        id_nr = i // 2 + 1
        for j in range(x):
            disk[index] = id_nr
            index += 1
    else:
        for j in range(x):
            disk[index] = 0
            index += 1

first_white = 0
last_char = len(disk) - 1

while first_white < last_char:
    if disk[first_white] != 0:
        first_white += 1
    elif disk[last_char] == 0:
        last_char -= 1
    else:
        disk[first_white], disk[last_char] = disk[last_char], disk[first_white]
        first_white += 1
        last_char -= 1

# make mul from [0 to last_char]

S = 0

for i in range(len(disk)):
    if disk[i] == 0:
        continue

    S += (disk[i] - 1) * i

print(S)
