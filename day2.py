with open('./inputs/day2.txt') as f:
    data = f.read().splitlines()

def check(vals):
    stack = [vals[0], vals[1]]
    if 1 <= abs(vals[0] - vals[1]) <= 3:
        rel = vals[1] > vals[0]
        for v in vals[2:]:
            if v > stack[-1]:
                if not rel or v - stack[-1] > 3 or v - stack[-1] < 1:
                    return False
                stack.append(v)
            else:
                if rel or stack[-1] - v > 3 or stack[-1] - v < 1:
                    return False
                stack.append(v)
    else:
        return False
    return True

def part1():
    res = 0
    for report in data:
        vals = [int(v) for v in report.split(' ')]
        if check(vals):
            res += 1
    print(res)

def part2():
    res = 0
    for report in data:
        vals = [int(v) for v in report.split(' ')]
        for i in range(len(vals)):
            tmp = vals[:i] + vals[i+1:]
            if check(tmp):
                res += 1
                # print(report)
                break
    print(res)
part2()