import sys
from functools import cmp_to_key
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
        continue
    pages.sort(key=cmp_to_key(lambda a, b: -1 if (b, a) in rules else 0))
    total += pages[len(pages) // 2]

assert total == 6311
