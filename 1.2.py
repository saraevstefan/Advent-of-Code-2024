with open('1.txt', 'r') as f:
    data = f.read()

numbers = [
    list(filter(lambda x: x != '', line.strip().split(' ')))
    for line in data.split('\n')]

numbers = [[int(pair[0].strip()), int(pair[1].strip())] for pair in numbers]
left, right = zip(*numbers)

left = sorted(left)
right = sorted(right)

dct_freq = {}

for x in right:
    if x not in dct_freq:
        dct_freq[x] = 0
    dct_freq[x] += 1
    
S = 0
    
for x in left:
    if x not in dct_freq:
        continue
    S += x * dct_freq[x]
    
print(S)