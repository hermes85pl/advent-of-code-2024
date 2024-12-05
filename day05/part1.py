import sys
from itertools import combinations

rules = set()

for line in sys.stdin:
    if line == "\n":
        break
    a, b = [int(x) for x in line.rstrip().split("|")]
    rules.add((a, b))

total = 0

for line in sys.stdin:
    pages = [int(x) for x in line.rstrip().split(",")]
    for c in combinations(pages, 2):
        if c[::-1] in rules:
            break
    else:
        total += pages[len(pages) // 2]

assert total == 4996
