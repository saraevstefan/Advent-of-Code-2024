from collections import defaultdict

with open('1.txt', 'r') as f:
    data = f.read()

numbers = [
    list(line.strip().split('   '))
    for line in data.split('\n')]

numbers = [[int(pair[0].strip()), int(pair[1].strip())]
           for pair in numbers]

left, right = zip(*numbers)

# default value 0
dct_freq = defaultdict(int)

for x in right:
    dct_freq[x] = dct_freq[x] + 1

S = sum(l * dct_freq[l] for l in left)

print(S)
