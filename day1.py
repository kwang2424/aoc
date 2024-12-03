from collections import Counter

with open('./inputs/day1.txt') as f:
    data = f.read().splitlines()

def mapdata(line):
    return line.split('   ')

def part1():
    first, second = [], []
    for l in data:
        split_line = l.split('   ')
        first.append(int(split_line[0]))
        second.append(int(split_line[1]))

    first = sorted(first)
    second = sorted(second)
    res = 0
    for i in range(len(first)):
        res += abs(first[i] - second[i])
    print(res)

def part2():
    mapped = list(map(mapdata, data))
    second_cnt = Counter([int(x[1]) for x in mapped])
    first_map = {}
    res = 0
    for x in mapped:
        v = int(x[0])
        if v not in first_map:
            first_map[v] = v * second_cnt[v]
        res += first_map[v]
    return res

print(part2())
