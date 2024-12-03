with open('1.txt', 'r') as f:
    data = f.read()

numbers = [
    list(filter(lambda x: x != '', line.strip().split(' ')))
    for line in data.split('\n')]

numbers = [[int(pair[0].strip()), int(pair[1].strip())] for pair in numbers]
left, right = zip(*numbers)

left = sorted(left)
right = sorted(right)

S = 0

for i in range(len(left)):
    S += abs(left[i] - right[i])
    
print(S)