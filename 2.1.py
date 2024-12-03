with open('2.txt', 'r') as f:
    data = f.read()

reports = data.split('\n')

reports = [
    [
        int(pair.strip())
        for pair in line.split(' ')
    ]
    for line in reports]

S = 0

for report in reports:
    diffs = [report[i] - report[i+1] for i in range(len(report)-1)]

    increasing = all(d > 0 and d <= 3 for d in diffs)
    decreasing = all(d < 0 and d >= -3 for d in diffs)
    S += increasing or decreasing

print(S)
