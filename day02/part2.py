from common import safe

total = 0

with open("input.txt") as f:
    while l := f.readline().strip():
        levels = [int(x) for x in l.split()]
        for i in range(len(levels)):
            if v := safe(levels[:i] + levels[i + 1 :]):
                total += v
                break

assert total == 493
