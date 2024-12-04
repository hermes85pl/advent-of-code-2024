import sys

MAS = "MAS"


def match(s: str) -> bool:
    return s == MAS or s == MAS[::-1]


total = 0

m = [line.rstrip() for line in sys.stdin]

for i in range(len(m) - len(MAS) + 1):
    for j in range(len(m[0]) - len(MAS) + 1):
        if not match("".join(m[i + k][j + k] for k in range(len(MAS)))):
            continue
        if not match("".join(m[i + k][j + len(MAS) - 1 - k] for k in range(len(MAS)))):
            continue
        total += 1

assert total == 1866
