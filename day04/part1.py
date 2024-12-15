import re
import sys

PATTERN = re.compile("XMAS")


def findcount(s: str) -> int:
    return len(PATTERN.findall(s)) + len(PATTERN.findall(s[::-1]))


total = 0

m = [line.rstrip() for line in sys.stdin]

hlen = len(m)
wlen = len(m[0])
mlen = min(hlen, wlen)

for i in range(hlen):
    row = m[i]
    total += findcount(row)

    backslash = "".join(m[i + j][j] for j in range(mlen - i))
    total += findcount(backslash)

    forwardslash = "".join(m[hlen - 1 - i - j][j] for j in range(mlen - i))
    total += findcount(forwardslash)

for j in range(wlen):
    column = "".join(m[i][j] for i in range(hlen))
    total += findcount(column)

    if j != 0:
        backslash = "".join(m[i][j + i] for i in range(mlen - j))
        total += findcount(backslash)

        forwardslash = "".join(m[hlen - 1 - i][j + i] for i in range(mlen - j))
        total += findcount(forwardslash)

assert total == 2534
