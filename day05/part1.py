import sys
from itertools import combinations, takewhile

rules = {
    tuple(int(x) for x in line.rstrip().split("|"))
    for line in takewhile(lambda l: l != "\n", sys.stdin)
}

total = 0

for line in sys.stdin:
    pages = [int(x) for x in line.rstrip().split(",")]
    for c in combinations(pages, 2):
        if c[::-1] in rules:
            break
    else:
        total += pages[len(pages) // 2]

assert total == 4996
