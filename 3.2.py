import re

with open('3.txt', 'r') as f:
    data = f.read()

indexes_mul = [m.start()
               for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', data)]

indexes_do = [m.start() for m in re.finditer(r'do\(\)', data)]
indexes_dont = [m.start() for m in re.finditer(r'don\'t\(\)', data)]

allowed = True

all_indexes = \
    [(i, 'm') for i in indexes_mul] + \
    [(i, 'd') for i in indexes_do] + \
    [(i, 'n') for i in indexes_dont]

all_indexes = sorted(all_indexes, key=lambda x: x[0])

good_mul = []
for i, c in all_indexes:
    if c == 'm':
        if allowed:
            good_mul.append(i)
    elif c == 'd':
        allowed = True
    elif c == 'n':
        allowed = False

index_good_mul = [i for i, g in enumerate(indexes_mul) if g in good_mul]

numbers = list(re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data))

numbers = [numbers[i] for i in index_good_mul]

numbers = [[int(pair[0]), int(pair[1])] for pair in numbers]

S = sum(l * r for l, r in numbers)

print(S)
