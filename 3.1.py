import re

with open('3.txt', 'r') as f:
    data = f.read()

numbers = list(re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data))

numbers = [[int(pair[0]), int(pair[1])] for pair in numbers]

S = sum(l * r for l, r in numbers)

print(S)
