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

    if increasing or decreasing:
        S += 1
    else:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            new_diffs = [new_report[i] - new_report[i+1]
                         for i in range(len(new_report)-1)]
            new_increasing = all(d > 0 and d <= 3 for d in new_diffs)
            new_decreasing = all(d < 0 and d >= -3 for d in new_diffs)
            if new_increasing or new_decreasing:
                S += 1
                break

print(S)
