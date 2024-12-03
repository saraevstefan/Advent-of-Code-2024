with open('1.txt', 'r') as f:
    data = f.read()

numbers = [
    list(line.strip().split('   '))
    for line in data.split('\n')]

numbers = [[int(pair[0].strip()), int(pair[1].strip())]
           for pair in numbers]

left, right = zip(*numbers)
left, right = sorted(left), sorted(right)

S = sum(abs(l-r) for l, r in zip(left, right))

print(S)
